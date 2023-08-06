import os, sys
import requests
import tempfile
import logging
import boto3
import time
import json
from shutil import copyfileobj

# from redshift_connector import SUPER
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import awswrangler as wr
import pandas as pd
import inspect
from inspect import signature
from urllib.parse import urlparse
import ast
from datetime import datetime
from random import randint
from http.client import IncompleteRead as http_incompleteRead
from urllib3.exceptions import IncompleteRead as urllib3_incompleteRead

# os.environ["PYTHONWARNINGS"] = 'ignore'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class NoTraceBackWithLineNumber(Exception):
    def __init__(self, msg):
        try:
            ln = sys.exc_info()[-1].tb_lineno
        except AttributeError:
            ln = inspect.currentframe().f_back.f_lineno
        self.args = "{0.__name__} (line {1}): {2}".format(type(self), ln, msg),
        sys.exit(self)

class Error(NoTraceBackWithLineNumber):
    pass

class DataPlate:
    """
    Initializes Data Access API client.

    Parameters
    -----------
    access_key : str (optional)
        Your own private key that can be obtained through DataPlate Data Access Portal. Default value is taken from the
        `DA_KEY` environment variable.

    dataplate_uri : str (optional)
        DataPlate Portal URI. If not specified, the value is taken from the `DA_URI` environment variable.
    """
    def __init__(self, access_key=None, dataplate_uri=None):
        if dataplate_uri is None:
            if not 'DA_URI' in os.environ:
                raise Error(ValueError(
                    'Can\'t find DA_URI environment variable, dataplate_uri parameter is not provided either!'
                ))
            dataplate_uri = os.environ['DA_URI']

        if access_key is None:
            if not 'DA_KEY' in os.environ:
                raise Error(ValueError(
                    'Can\'t find DA_KEY environment variable, access_key parameter is not provided either!'
                ))
            access_key = os.environ['DA_KEY']

        self.access_key = access_key
        self.session = requests.sessions.Session()
        retry = Retry(total=5,
                      read=5,
                      connect=5,
                      backoff_factor=0.3,
                      status_forcelist=(500, 502, 504))
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.base_url = '/'.join(dataplate_uri.split('/')[0:3])
        self.emr = self._EMR(self)

    def _set_proxy_if_needed(self, proxy):
        os.environ.pop('HTTP_PROXY', None)
        try:
            self.session.head('{}/version'.format(self.base_url))
        except requests.exceptions.ConnectionError:
            self.session.proxies = {'http': proxy}
            self.session.head('{}/version'.format(self.base_url))

    def _get_list_of_files(self, s3_client, bucket, prefix, suffix='json.gz'):
        next_token = ''
        base_kwargs = {
            'Bucket': bucket,
            'Prefix': prefix,
        }
        keys = []
        while next_token is not None:
            kwargs = base_kwargs.copy()
            if next_token != '':
                kwargs.update({'ContinuationToken': next_token})
            results = s3_client.list_objects_v2(**kwargs)
            contents = results.get('Contents')
            for i in contents:
                k = i.get('Key')
                if k[-1] != '/' and k.endswith(suffix):
                    keys.append(k)
            next_token = results.get('NextContinuationToken')
        logging.info('Got the following files: {}'.format(keys))

        return keys

    def _read_file(self, s3_client, bucket, key):
        kwargs = {'Bucket': bucket, 'Key': key}
        return s3_client.get_object(**kwargs)['Body']

    def _download_files_as_one(self, s3_client, bucket, keys, output_file):
        with open(output_file, 'wb') as out:
            for key in keys:
                fh = self._read_file(s3_client, bucket, key)
                while True:
                    chunk = fh.read(8192)
                    out.write(chunk)
                    if len(chunk) <= 0:
                        break

    def _files_to_df(self, bucket, prefix, **kwargs):
        import pandas as pd
        with tempfile.NamedTemporaryFile(suffix='.gz') as t:
            output_file = t.name
            s3 = boto3.client('s3')
            files = self._get_list_of_files(s3, bucket, prefix)
            self._download_files_as_one(s3, bucket, files, output_file)
            with open(output_file, 'rb') as fh:
                return pd.read_json(fh, compression='gzip', lines=True, **kwargs)

    def query(self,
              query,
              output_file,
              refresh=False,
              async_m=None,
              request_timeout=None,
              es_index_type=None,
              es_node=None,
              ops_include_fields=None,
              bucket_suffixes=None,
              bucket_filter=None,
              deep_source_url=None,
              force_scheme_change=False,
              recursive_lookup_no_partitions=False,
              use_spark=True,
              grace_seconds=30,
              retries=1,
              max_retries_sleep_seconds=60):
        """
        Executes remote SQL query, and saves results to the specified file.

        Parameters
        ----------
        query : str
            SQL query supported by Apache Spark
        output_file : str
            Full path to the file where results will be saved (results are represented by JSON records separated by the newline)
        refresh : boolean
            Whether to use force running query even cached results already exist (default: False)
        async_m : int
            How many minutes should the client poll the server.
        request_timeout : int/tuple
            requests timeout parameter for a single request.
            https://requests.readthedocs.io/en/master/user/advanced/#timeouts
        es_index_type: str
            elasticSearch/openSearch option - dynamically add/change the dataset es.resource (index/type) for the allowed cluster [e.g.: index1/type1,index2/type2] ,to search for all types in index ignore the type name (default: None)
        es_node: str
            elasticSearch/openSearch option - dynamically change host/cluster/node name - use this in case you've defined a regex based es.nodes in the source url of the dataset
        ops_include_fields: str
            openSearch option - dynamically include only the specified fields (comma separated string) , will reduce run time. e.g.: field1,field2,field3
        bucket_suffixes: str
            bucket option - bucket path suffix added to your dataset path name, [e.g.: MyPathSuffix1,MyPathSuffix2] (default: None)
        bucket_filter: str
            bucket option - include files in the bucket with file names matching the pattern (default: None)
        deep_source_url: str
            deeper s3 path - used in case the dataset is json,csv,parquet in s3 and the source_url of dataset is with * suffix to allow deeper read granularity
            i.e.: source_url defined as s3://my_dataset_original_source_url/* , allows to query data from deeper level in case the scheme is difference by defining s3://my_dataset_original_source_url/suffix_key
        force_scheme_change: boolean
            In case scheme was change in the data meant to read/query use this to indicate spark to re-create the temporary view
            Use this only if case you want to read parquet files that were written with dataset=True and mode="overwrite_partitions"
            and where the overwrite scheme was changed
        recursive_lookup_no_partitions: boolean
            We recommend defining sub-folders as partitions instead of using this
            Note: this requires an EMR cluster > 6.3.0 with spark 3
            If True you'll be able to read data from subfolders, even though no partitions were defined
            default is False - meaning you have to define sub-folders as partitions (e.g "customer=customer1")
        use_spark: boolean
            In case your dataset is small or is being accessed very frequent, set it as False to utilize data wrangling without using Spark and EMR
            default is True - utilize spark cluster
        grace_seconds: int
            A grace period (default=30 sec) in case the same user sending a request during the streaming response of another request - this allows to avoid concurrency issues
        retries: int
            In case of a concurrency failure retry x retries times (default 1 = no retry) while randomly sleep for 30sec to max_retries_sleep_seconds
        max_retries_sleep_seconds: int
            In case retries > 1 sleep randomly between 30seconds to this parameter (default=60 seconds)
        """
        headers = {'X-Access-Key': self.access_key}
        params = {}
        if refresh:
            params['refresh'] = '1'
        if async_m:
            timeout = time.time() + async_m * 60
            params['async'] = '1'
        if es_index_type:
            params['es_index_type'] = es_index_type
        if es_node:
            params['es_node'] = es_node
        if ops_include_fields:
            params['ops_include_fields'] = ops_include_fields
        if bucket_suffixes:
            params['bucket_suffixes'] = bucket_suffixes
        if bucket_filter:
            params['bucket_filter'] = bucket_filter
        if deep_source_url:
            params['deep_source_url'] = deep_source_url
        if force_scheme_change:
            params['force_scheme_change'] = force_scheme_change
        if recursive_lookup_no_partitions:
            params['recursive_lookup_no_partitions'] = recursive_lookup_no_partitions
        if grace_seconds:
            params['grace_seconds'] = grace_seconds
        params['use_spark'] = use_spark

        # retries = 1
        while True:
            if async_m and timeout < time.time():
                raise Error('Timeout waiting for query.')
            try:
                logging.info('Sending query...')
                r = self.session.post(\
                        '{}/api/query'.format(self.base_url), params=params, data=query,
                        headers=headers, stream=True, allow_redirects=False, timeout=request_timeout)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('Query is processing, waiting a bit...')
                        time.sleep(5)
                        continue
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                        format(r.status_code, r.text))

                logging.info('Got query result, writing to file.')
                with open(output_file, 'wb') as fh:
                    copyfileobj(r.raw, fh)
                logging.info('Done writing to file.')
                break
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout,http_incompleteRead,urllib3_incompleteRead) as e:
                logging.exception('Got ConnectionError/IncompleteRead/ReadTimeout exception.')
                retries -= 1
                if retries <= 0:
                    raise Error(e)
                rand = randint(30, max_retries_sleep_seconds)
                logging.info(f'Retrying request. in {rand} seconds, according to max_retries_sleep_seconds')
                time.sleep(rand)
                continue

    def query_to_df(self,
                    query,
                    refresh=False,
                    async_m=None,
                    request_timeout=None,
                    es_index_type=None,
                    es_node=None,
                    ops_include_fields=None,
                    bucket_suffixes=None,
                    bucket_filter=None,
                    deep_source_url=None,
                    force_scheme_change=False,
                    recursive_lookup_no_partitions=False,
                    use_spark=True,
                    grace_seconds=30,
                    retries=1,
                    max_retries_sleep_seconds=60,
                    **kwargs):
        """
        Executes remote SQL query, and returns Pandas dataframe.
        Use with care as all the content is materialized.

        Parameters
        ----------
        query : str
            SQL query supported by Apache Spark
        refresh : boolean
            Whether to use force running query even cached results already exist (default: False)
        async_m : int
            How many minutes should the client poll the server.
        request_timeout : int/tuple
            requests timeout parameter for a single request.
            https://requests.readthedocs.io/en/master/user/advanced/#timeouts
        es_index_type: str
            elasticSearch/openSearch option - dynamically add/change the dataset es.resource (index/type) for the allowed cluster [e.g.: index1/type1,index2/type2] ,to search for all types in index ignore the type name (default: None)
        es_node: str
            elasticSearch/openSearch option - dynamically change host/cluster/node name - use this in case you've defined a regex based es.nodes in the source url of the dataset
        ops_include_fields: str
            openSearch option - dynamically include only the specified fields (comma separated string) , will reduce run time. e.g.: field1,field2,field3
        bucket_suffixes: str
            bucket option - bucket path suffix added to your dataset path name, [e.g.: MyPathSuffix1,MyPathSuffix2] (default: None)
        bucket_filter: str
            bucket option - include files in the bucket with file names matching the pattern (default: None)
        deep_source_url: str
            deeper s3 path - used in case the dataset is json,csv,parquet in s3 and the source_url of dataset is with * suffix to allow deeper read granularity
            i.e.: source_url defined as s3://my_dataset_original_source_url/* , allows to query data from deeper level in case the scheme is difference by defining s3://my_dataset_original_source_url/suffix_key
        force_scheme_change: boolean
            In case scheme was change in the data meant to read/query use this to indicate spark to re-create the temporary view
            Use this only if case you want to read parquet files that were written with dataset=True and mode="overwrite_partitions"
            and where the overwrite scheme was changed
        recursive_lookup_no_partitions: boolean
            We recommend defining sub-folders as partitions instead of using this
            Note: this requires an EMR cluster > 6.3.0 with spark 3
            If True you'll be able to read data from subfolders, even though no partitions were defined
            default is False - meaning you have to define sub-folders as partitions (e.g "customer=customer1")
        use_spark: boolean
            In case your dataset is small or is being accessed very frequent, set it as False to utilize data wrangling without using Spark and EMR
            default is True - utilize spark cluster
        enable_replay (BETA - NOT Working yet): boolean
            If True, enable you to replay the specific data that was queried in the specific query (restore data for retrospective needs)
            Data for replay will be expired after 14 days (default configuration)
        grace_seconds: int
            A grace period (default=30 sec) in case the same user sending a request during the streaming response of another request - this allows to avoid concurrency issues
        retries: int
            In case of a concurrency failure retry x retries times (default 1 = no retry) while randomly sleep for 30sec to max_retries_sleep_seconds
        max_retries_sleep_seconds: int
            In case retries > 1 sleep randomly between 30seconds to this parameter (default=60 seconds)
        **kwargs : params
            Arbitrary parameters to pass to `pandas.read_json()` method

        Returns
        -------
        Pandas dataframe.
        """
        import pandas as pd
        with tempfile.NamedTemporaryFile(suffix='.gz') as t:
            output_file = t.name
            self.query(query, output_file, refresh, async_m, request_timeout, es_index_type, es_node, ops_include_fields, bucket_suffixes, bucket_filter, deep_source_url, force_scheme_change, recursive_lookup_no_partitions, use_spark, grace_seconds, retries, max_retries_sleep_seconds)
            with open(output_file, 'rb') as fh:
                return pd.read_json(fh, compression='gzip', lines=True, **kwargs)


    def execute_pyspark_toFile(self,
                         code,
                         output_file,
                         refresh=True,
                         retries = 1,
                         async_m=None,
                         request_timeout=None,
                         grace_seconds=30,
                         max_retries_sleep_seconds=60,
                         **kwargs):
        """
        Executes remote pyspark code, and saves results to the specified file - use only if the code specify writes to a target file.

        Parameters
        ----------
        code : str
            Code supported by Apache Spark (pyspark code)
        output_file : str
            Full path to the file where results will be saved (results are represented by JSON records separated by the newline)
        refresh : boolean
            Whether to use force running query even cached results already exist (default: True)
        async_m : int
            How many minutes should the client poll the server.
        request_timeout : int/tuple
            requests timeout parameter for a single request.
            https://requests.readthedocs.io/en/master/user/advanced/#timeouts
        grace_seconds: int
            A grace period (default=30 sec) in case the same user sending a request during the streaming response of another request - this allows to avoid concurrency issues
        retries: int
            In case of a concurrency failure retry x retries times (default 1 = no retry) while randomly sleep for 30sec to max_retries_sleep_seconds
        max_retries_sleep_seconds: int
            In case retries > 1 sleep randomly between 30seconds to this parameter (default=60 seconds)
        """
        headers = {'X-Access-Key': self.access_key}
        params = {}
        if refresh:
            params['refresh'] = '1'
        if async_m:
            timeout = time.time() + async_m * 60
            params['async'] = '1'
        if grace_seconds:
            params['grace_seconds'] = grace_seconds

        while True:
            if async_m and timeout < time.time():
                raise Error('Timeout waiting for code.')
            try:
                logging.info('Sending spark code...')
                r = self.session.post( \
                    '{}/api/pyspark_code'.format(self.base_url), params=params, data=code,
                    headers=headers, stream=True, allow_redirects=False, timeout=request_timeout)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('Pyspark code is processing, waiting a bit...')
                        time.sleep(5)
                        continue
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Got pyspark code result, writing to file.')
                with open(output_file, 'wb') as fh:
                    copyfileobj(r.raw, fh)
                logging.info('Done writing to file.')
                break
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout, http_incompleteRead, urllib3_incompleteRead) as e:
                logging.exception('Got ConnectionError/IncompleteRead/ReadTimeout exception.')
                retries -= 1
                if retries <= 0:
                    raise Error(e)
                rand = randint(30, max_retries_sleep_seconds)
                logging.info(f'Retrying request. in {rand} seconds, according to max_retries_sleep_seconds')
                time.sleep(rand)
                continue

    def execute_pyspark_toJson(self,
                         code,
                         retries = 1,
                         async_m=None,
                         request_timeout=None,
                         grace_seconds=30,
                         max_retries_sleep_seconds=60,
                         **kwargs):

        """
        Executes remote pyspark code, and output the result as Json.

        Parameters
        ----------
        code : str
            Code supported by Apache Spark (pyspark code)
        async_m : int
            How many minutes should the client poll the server.
        request_timeout : int/tuple
            requests timeout parameter for a single request.
            https://requests.readthedocs.io/en/master/user/advanced/#timeouts
        grace_seconds: int
            A grace period (default=30 sec) in case the same user sending a request during the streaming response of another request - this allows to avoid concurrency issues
        retries: int
            In case of a concurrency failure retry x retries times (default 1 = no retry) while randomly sleep for 30sec to max_retries_sleep_seconds
        max_retries_sleep_seconds: int
            In case retries > 1 sleep randomly between 30seconds to this parameter (default=60 seconds)
        """

        headers = {'X-Access-Key': self.access_key}
        params = {}
        refresh = True
        if refresh:
            params['refresh'] = '1'
        if async_m:
            timeout = time.time() + async_m * 60
            params['async'] = '1'
        if grace_seconds:
            params['grace_seconds'] = grace_seconds

        while True:
            if async_m and timeout < time.time():
                raise Error('Timeout waiting for code.')
            try:
                logging.info('Sending pyspark code...')
                r = self.session.post( \
                    '{}/api/pyspark_code_toJson'.format(self.base_url), params=params, data=code,
                    headers=headers, stream=True, allow_redirects=False, timeout=request_timeout)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('Pyspark code is processing, waiting a bit...')
                        time.sleep(5)
                        continue
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Got pyspark code result, dump json response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    return json.dumps(rJson.get('text/plain'))
                else:
                    logging.exception('Could not find proper output, please check your code')
                # return r.text
                # logging.info('Done writing to file.')
                break
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout, http_incompleteRead, urllib3_incompleteRead) as e:
                logging.exception('Got ConnectionError/IncompleteRead/ReadTimeout exception.')
                retries -= 1
                if retries <= 0:
                    raise Error(e)
                rand = randint(30, max_retries_sleep_seconds)
                logging.info(f'Retrying request. in {rand} seconds, according to max_retries_sleep_seconds')
                time.sleep(rand)
                continue



    def write_from_query_to_db(self,
              query,
              output_dataset_name=None,
              async_m=None,
              request_timeout=None,
              es_index_type=None,
              es_node=None,
              bucket_suffixes=None,
              bucket_filter=None,
              deep_source_url=None,
              force_scheme_change=False,
              recursive_lookup_no_partitions=False,
              grace_seconds=30,
              retries=1,
              max_retries_sleep_seconds=60):
        """
        Executes remote SQL query, and saves results to the specified dataset (jdbc db - not s3).

        Parameters
        ----------
        query (required) : str
            SQL query supported by Apache Spark
        output_dataset_name (required) : str
            the output dataset name of the DB (not s3) to write results to
        async_m : int
            How many minutes should the client poll the server.
        request_timeout : int/tuple
            requests timeout parameter for a single request.
            https://requests.readthedocs.io/en/master/user/advanced/#timeouts
        es_index_type: str
            elasticSearch/openSearch option - dynamically add/change the dataset es.resource (index/type) for the allowed cluster [e.g.: index1/type1,index2/type2] ,to search for all types in index ignore the type name (default: None)
        es_node: str
            elasticSearch/openSearch option - dynamically change host/cluster/node name - use this in case you've defined a regex based es.nodes in the source url of the dataset
        bucket_suffixes: str
            bucket option - bucket path suffix added to your dataset path name, [e.g.: MyPathSuffix1,MyPathSuffix2] (default: None)
        bucket_filter: str
            bucket option - include files in the bucket with file names matching the pattern (default: None)
        deep_source_url: str
            deeper s3 path - used in case the dataset is json,csv,parquet in s3 and the source_url of dataset is with * suffix to allow deeper read granularity
            i.e.: source_url defined as s3://my_dataset_original_source_url/* , allows to query data from deeper level in case the scheme is difference by defining s3://my_dataset_original_source_url/suffix_key
        force_scheme_change: boolean
            In case scheme was change in the data meant to read/query use this to indicate spark to re-create the temporary view
            Use this only if case you want to read parquet files that were written with dataset=True and mode="overwrite_partitions"
            and where the overwrite scheme was changed
        recursive_lookup_no_partitions: boolean
            We recommend defining sub-folders as partitions instead of using this
            Note: this requires an EMR cluster > 6.3.0 with spark 3
            If True you'll be able to read data from subfolders, even though no partitions were defined
            default is False - meaning you have to define sub-folders as partitions (e.g "customer=customer1")
        grace_seconds: int
            A grace period (default=30 sec) in case the same user sending a request during the streaming response of another request - this allows to avoid concurrency issues
        retries: int
            In case of a concurrency failure retry x retries times (default 1 = no retry) while randomly sleep for 30sec to max_retries_sleep_seconds
        max_retries_sleep_seconds: int
            In case retries > 1 sleep randomly between 30seconds to this parameter (default=60 seconds)
        """
        headers = {'X-Access-Key': self.access_key}
        params = {}
        params['refresh'] = '1'

        if not output_dataset_name:
            raise Error('output_dataset_name must be defined')

        params['output_dataset_name'] = output_dataset_name
        if async_m:
            timeout = time.time() + async_m * 60
            params['async'] = '1'
        if es_index_type:
            params['es_index_type'] = es_index_type
        if es_node:
            params['es_node'] = es_node
        if bucket_suffixes:
            params['bucket_suffixes'] = bucket_suffixes
        if bucket_filter:
            params['bucket_filter'] = bucket_filter
        if deep_source_url:
            params['deep_source_url'] = deep_source_url
        if force_scheme_change:
            params['force_scheme_change'] = force_scheme_change
        if recursive_lookup_no_partitions:
            params['recursive_lookup_no_partitions'] = recursive_lookup_no_partitions
        if grace_seconds:
            params['grace_seconds'] = grace_seconds

        # retries = 1
        while True:
            if async_m and timeout < time.time():
                raise Error('Timeout waiting for query.')
            try:

                # backword compatability
                res = self.session.get('{}/version'.format(self.base_url))
                is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.06'
                if not is_new_enough:
                    logging.exception(
                        'This API requires server version >= 1.28.06, please update your DataPlate server')
                    return

                logging.info('Sending request...')
                r = self.session.post(\
                        '{}/api/write_from_query_to_db'.format(self.base_url), params=params, data=query,
                        headers=headers, stream=True, allow_redirects=False, timeout=request_timeout)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('Query is processing, waiting a bit...')
                        time.sleep(5)
                        continue
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                        format(r.status_code, r.text))

                logging.info('Got result')
                if r.text:
                    logging.info(r.text)
                    return
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # logging.info('Done writing to db.')
                break
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout,http_incompleteRead,urllib3_incompleteRead) as e:
                logging.exception('Got ConnectionError/IncompleteRead/ReadTimeout exception.')
                retries -= 1
                if retries <= 0:
                    raise Error(e)
                rand = randint(30, max_retries_sleep_seconds)
                logging.info(f'Retrying request. in {rand} seconds, according to max_retries_sleep_seconds')
                time.sleep(rand)
                continue

    ####
    # Start of AWS S3 Functions
    ####

    def write_to_s3_csv(self, *args, **kwargs):
        try:
            # json_object = json.dumps(kwargs)
            # if kwargs:
            #     print(f'Kwargs: {kwargs}')
            # if args:
            #     print(f'Kwargs: {args}')
            sig = signature(wr.s3.to_csv)
            sba = sig.bind(*args, **kwargs)

            if 'df' in kwargs:
                # df = pd.read_json(args['df'])
                kwargs['df'] = kwargs['df'].to_json()
                json_kwargs_object = json.dumps(kwargs)
                if len(kwargs['df']) <= 5:
                    logging.error('Empty dataframe !')
                    return
            elif len(args) >= 1:
                try:
                    kwargs['df'] = args[0].to_json()
                    json_kwargs_object = json.dumps(kwargs)
                except Exception as e:
                    logging.error('Empty dataframe !')
                    return
            else:
                logging.error('Empty dataframe !')
                # return wr.s3.to_csv(*sba.args, **sba.kwargs)


            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
            # params = json.dumps(args)#{}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/toS3_csv'.format(self.base_url), data=json_kwargs_object,
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('writing data to AWS...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing write response')
                # logging.info(str(r.text))
                if r.text:
                    logging.info(f'Done writing. {r.text}')
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)
            except BaseException as e:
                logging.exception('aws_to_s3_csv , ' + str(e))
                raise Error(e)

        except Exception as e:
            logging.exception('aws_to_s3_csv , ' + str(e))
            raise Error(e)

    # write_to_s3_csv.__doc__ = wr.s3.to_csv.__doc__.replace('import awswrangler as wr','from dataplate.client import DataPlate')
    write_to_s3_csv.__doc__ = wr.s3.to_csv.__doc__.replace('import awswrangler as wr','from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
    write_to_s3_csv.__doc__ = write_to_s3_csv.__doc__.replace('wr.s3.to_csv','dataplate.write_to_s3_csv')

    def write_to_s3_json(self, *args, **kwargs):
        try:
            # json_object = json.dumps(kwargs)
            # if kwargs:
            #     print(f'Kwargs: {kwargs}')
            # if args:
            #     print(f'Kwargs: {args}')
            sig = signature(wr.s3.to_json)
            sba = sig.bind(*args, **kwargs)

            if 'df' in kwargs:
                # df = pd.read_json(args['df'])
                kwargs['df'] = kwargs['df'].to_json()
                json_kwargs_object = json.dumps(kwargs)
                if len(kwargs['df']) <= 5:
                    logging.error('Empty dataframe !')
                    return
            elif len(args) >= 1:
                try:
                    kwargs['df'] = args[0].to_json()
                    json_kwargs_object = json.dumps(kwargs)
                except Exception as e:
                    logging.error('Empty dataframe !')
                    return
            else:
                logging.error('Empty dataframe !')
                # return wr.s3.to_json(*sba.args, **sba.kwargs)


            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
            # params = json.dumps(args)#{}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/toS3_json'.format(self.base_url), data=json_kwargs_object,
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('writing data to AWS...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing write response')
                # logging.info(str(r.text))
                if r.text:
                    #rJson = json.loads(r.text)
                    logging.info(f'Done writing. {r.text}')
                    # return r.text#json.dumps(response_text)
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)
            except BaseException as e:
                logging.exception('aws_to_s3_json , ' + str(e))
                raise Error(e)

        except Exception as e:
            logging.exception('aws_to_s3_json , ' + str(e))
            raise Error(e)

    # write_to_s3_json.__doc__ = wr.s3.to_json.__doc__.replace('awswrangler','dataplate')
    write_to_s3_json.__doc__ = wr.s3.to_json.__doc__.replace('import awswrangler as wr','from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
    write_to_s3_json.__doc__ = write_to_s3_json.__doc__.replace('wr.s3.to_json','dataplate.write_to_s3_json')


    def write_to_s3_parquet(self, *args, **kwargs):
        try:
            # json_object = json.dumps(kwargs)
            # if kwargs:
            #     print(f'Kwargs: {kwargs}')
            # if args:
            #     print(f'Kwargs: {args}')
            sig = signature(wr.s3.to_parquet)
            sba = sig.bind(*args, **kwargs)

            if 'df' in kwargs:
                # df = pd.read_json(args['df'])
                kwargs['df'] = kwargs['df'].to_json()
                json_kwargs_object = json.dumps(kwargs)
                if len(kwargs['df']) <= 5:
                    logging.error('Empty dataframe !')
                    return
            elif len(args) >= 1:
                try:
                    kwargs['df'] = args[0].to_json()
                    json_kwargs_object = json.dumps(kwargs)
                except Exception as e:
                    logging.error('Empty dataframe !')
                    return
            else:
                logging.error('Empty dataframe !')
                # return wr.s3.to_parquet(*sba.args, **sba.kwargs)


            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
            # params = json.dumps(kwargs)#{}

            try:
                logging.info('Uploading data...')
                #params=params,
                r = self.session.post( \
                    '{}/api/aws/toS3_parquet'.format(self.base_url), data=json_kwargs_object,
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('writing data to AWS...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing write response')
                # logging.info(str(r.text))
                if r.text:
                    logging.info(f'Done writing. {r.text}')
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)
            except BaseException as e:
                logging.exception('aws_to_s3_parquet , ' + str(e))
                raise Error(e)

        except Exception as e:
            logging.exception('aws_to_s3_parquet , ' + str(e))
            raise Error(e)

    write_to_s3_parquet.__doc__ = wr.s3.to_parquet.__doc__.replace('import awswrangler as wr','from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
    write_to_s3_parquet.__doc__ = write_to_s3_parquet.__doc__.replace('wr.s3.to_parquet', 'dataplate.write_to_s3_parquet')


    def delete_s3_objects(self, *args, **kwargs):
        try:
            sig = signature(wr.s3.delete_objects)
            sba = sig.bind(*args, **kwargs)

            json_kwargs_object = json.dumps(kwargs)
            json_args_object = json.dumps(args)

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
            # params = json.dumps(kwargs)#{}

            try:
                logging.info('Sending request....')
                r = self.session.post( \
                    '{}/api/aws/S3_delete_objects'.format(self.base_url), data=json_kwargs_object,
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('delete objects from AWS...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing delete response')
                if r.text:
                    logging.info(f'Done deleting. {r.text}')
                else:
                    logging.exception('Could not find proper output, please check your parameters')

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('aws_delete_s3_objects , ' + str(e))
            raise Error(e)

    delete_s3_objects.__doc__ = wr.s3.delete_objects.__doc__.replace('import awswrangler as wr','from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
    delete_s3_objects.__doc__ = delete_s3_objects.__doc__.replace('wr.s3.delete_objects', 'dataplate.delete_s3_objects')


    def list_s3_objects(self, *args, **kwargs):
        try:
            sig = signature(wr.s3.list_objects)
            sba = sig.bind(*args, **kwargs)

            json_kwargs_object = json.dumps(kwargs, default=str)
            json_args_object = json.dumps(args)

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
            # params = json.dumps(kwargs)#{}

            try:
                logging.info('Sending request...')
                r = self.session.post( \
                    '{}/api/aws/S3_list_objects'.format(self.base_url), data=json_kwargs_object,
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('list objects from AWS...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing list response')
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info(f'Done listing.')
                    return rJson
                else:
                    logging.exception('Could not find proper output, please check your parameters')

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('aws_list_s3_objects , ' + str(e))
            raise Error(e)

    list_s3_objects.__doc__ = wr.s3.list_objects.__doc__.replace('import awswrangler as wr','from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
    list_s3_objects.__doc__ = list_s3_objects.__doc__.replace('wr.s3.list_objects', 'dataplate.list_s3_objects')


    def list_s3_directories(self, *args, **kwargs):
        try:
            sig = signature(wr.s3.list_directories)
            sba = sig.bind(*args, **kwargs)

            json_kwargs_object = json.dumps(kwargs)
            json_args_object = json.dumps(args)

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
            # params = json.dumps(kwargs)#{}

            try:
                logging.info('Sending request...')
                r = self.session.post( \
                    '{}/api/aws/S3_list_directories'.format(self.base_url), data=json_kwargs_object,
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('list directories from AWS...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing list response')
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info(f'Done listing.')
                    return rJson
                else:
                    logging.exception('Could not find proper output, please check your parameters')

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('aws_list_s3_directories , ' + str(e))
            raise Error(e)

    list_s3_directories.__doc__ = wr.s3.list_directories.__doc__.replace('import awswrangler as wr','from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
    list_s3_directories.__doc__ = list_s3_directories.__doc__.replace('wr.s3.list_directories', 'dataplate.list_s3_directories')

    ####
    # End of AWS S3 Functions
    ####

    def run_notebook(self, notebook_file_path, instance_type = "ml.m5.large", parameters = "{}", image = None, max_time_limit_minutes = 180, securityGroupIds = [], subnets= [], role = None, tags = None, project = None, sub_project= None):
        """ Run a notebook in SageMaker Processing producing a new output notebook.
        Args:
            notebook (str): The notebook file path.
            input_path (str): The S3 object containing the notebook. If this is None, the `notebook` argument is
                              taken as a local file to upload (default: None).
            parameters (dict): The dictionary of parameters to pass to the notebook (default: {}).
            image (str): The name of the image (e.g. my-tensorflow) , default: notebook-runner
            instance_type (str): The SageMaker instance to use for executing the job (default: ml.m5.large).
            max_time_limit_minutes : maximum minutes to run before force stop
            securityGroupIds : a list of securityGroup Ids of aws for the processing job to communicate with, in case communication with other resources, e.g. internal dataplate service, is needed
            subnets : a list of subnets of aws for the processing job to communicate with
            role : a role ARN to run the notebook, the default is the Dataplate service role (cross rols in case of Sass)
            tags : tags to add to the processingJob - this is mostly for pricing management. format as array of key/value jsons:  [{"Key": "project","Value": "my_project"},{"Key": "product","Value": "Research"}]
            project : project name to add the processingJob to and enable easy search. Must define sub_project as well. Must satisfy regular expression: ^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}
            sub_project : sub project name to be added to specific project name and enable easy search. Must define project as well, . Must satisfy regular expression: ^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}
        Returns:
            The name of the processing job created to run the notebook.
        """
        try:
            if not notebook_file_path or not os.path.isfile(notebook_file_path) or not notebook_file_path.endswith('.ipynb'):
                raise FileNotFoundError(f'notebook file is not legal/valid : {notebook_file_path if notebook_file_path else "None"}')

            f = open(notebook_file_path, 'r')
            if f:
                # Reading from file
                notebook_json_data = json.loads(f.read())
                # Closing file
                f.close()

            if not notebook_json_data or len(json.dumps(notebook_json_data)) < 10 or not 'cells' in notebook_json_data:
                raise Error(f'notebook file is not legal : {notebook_file_path if notebook_file_path else "None"}')

            notebook_name = os.path.basename(notebook_file_path)
            params = {}
            if instance_type:
                params['instance_type'] = instance_type
            if parameters:
                params['parameters'] = parameters
            if max_time_limit_minutes:
                params['timelimit_minutes'] = max_time_limit_minutes
            if image:
                params['image'] = image
            params['SecurityGroupIds'] = json.dumps(securityGroupIds)#','.join(['"%s"' % w for w in securityGroupIds])
            params['Subnets'] = json.dumps(subnets)#','.join(['"%s"' % w for w in subnets])
            params['notebook_name'] = notebook_name if notebook_name else ""
            if role:
                params['role'] = role
            if tags:
                params['tags'] = json.dumps(tags)
            if project:
                params['project'] = project
            if sub_project:
                params['sub_project'] = sub_project

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/runNotebook'.format(self.base_url), params=params, data=json.dumps(notebook_json_data),
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('running notebook, processing...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('run notebook finished successfully.')
                    return r.text.replace('"','')#json.dumps(rJson)
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('run_notebook , ' + str(e))
            raise Error(e)


    def list_runs_notebook(self, n=10, notebook = None, rule = None, date_after=None, date_before=None, project=None, sub_project= None):
        """Returns a pandas data frame of the runs, with the most recent at the top.
        Args:
        n (int): The number of runs to return or all runs if 0 (default: 10)
        notebook (str): If not None, return only runs of this notebook (default: None)
        rule (str): If not None, return only runs invoked by this rule (default: None)
        date_after (datetime): A filter that returns only components created after the specified time
        date_before (datetime): A filter that returns only components created before the specified time
        project (str): A filter that return only components that were defined with this project name
        sub_project (str): A filter that return only components that were defined with this sub_project name
        """

        try:

            params = {}
            if n:
                params['n'] = n
            if notebook:
                params['notebook'] = notebook
            if rule:
                params['rule'] = rule
            if date_after:
                params['date_after'] = date_after
            if date_before:
                params['date_before'] = date_before
            if project:
                params['project'] = project
            if sub_project:
                params['sub_project'] = sub_project

            json_params = json.dumps(params, default=str)

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                #backword compatability
                res = self.session.get('{}/version'.format(self.base_url))
                is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] > '1.24.01'
                if is_new_enough:
                    r = self.session.post( \
                        '{}/api/aws/listRunsNotebook'.format(self.base_url), data=json_params,
                        headers=headers, stream=True, allow_redirects=False)
                else:
                    r = self.session.post( \
                        '{}/api/aws/listRunsNotebook'.format(self.base_url), params=params, data="",
                        headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing notebook runs...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('list notebook runs finished successfully.')
                    try:
                        df = pd.read_json(rJson)
                        df['Created'] = pd.to_datetime(df['Created'], unit='ms',utc=True)
                        df['Start'] = pd.to_datetime(df['Start'], unit='ms', utc=True)
                        df['End'] = pd.to_datetime(df['End'], unit='ms', utc=True)
                        df['Elapsed'] = pd.to_timedelta(df['Elapsed'], unit='ms')
                        return df
                    except Exception as e:
                        logging.info('No notebook runs were found.')
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('list_runs_notebook , ' + str(e))
            raise Error(e)



    def stop_run_notebook(self, job_name= None):
        """Stop the named processing job.
        Args:
        job_name (string): The name of the job to stop. use list_runs_notebook to get specific notebook Job name
        """

        try:

            params = {}
            if job_name:
                params['jobname'] = job_name
            else:
                raise Error('Not a valid job name, use list_runs_notebook function to get specific notebook Job name.')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/stopNotebook'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing notebook stops...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    logging.info(r.text)
                    return
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('stop_run_notebook , ' + str(e))
            raise Error(e)


    def download_notebook_result(self, result_s3_file= None, output="."):
        """Download the output notebook from a previously completed job.

        Args:
          result_s3_file (str): The name of the SageMaker Processing Job Result that executed the notebook. (Required). use list_runs_notebook to get specific Result of Job
          output (str): The directory to copy the output file to. (Default: the current working directory)

        Returns:
          The filename of the downloaded notebook.
        """

        try:
            params = {}
            if result_s3_file:
                params['result_file'] = result_s3_file
            else:
                raise Error('Not a valid job name, use list_runs_notebook function to get specific notebook Job name.')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/downloadNotebook'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing notebook stops...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    # rJson = json.loads(r.text)
                    logging.info('Got notebook result successfully.')
                    # return json.dumps(rJson)
                    if not os.path.exists(output):
                        try:
                            os.makedirs(output)
                        except OSError as e:
                            raise Error(f'Could not crate output directory {output}')


                    o = urlparse(result_s3_file, allow_fragments=False)
                    # ParseResult(scheme='s3', netloc='bucket_name', path='/folder1/folder2/file1.json', params='', query='',
                    #             fragment='')
                    base_notebook_name = ""
                    split_path = o.path.split('/')
                    if split_path and len(split_path) > 0:
                        if len(split_path[-1]) > 0 and split_path[-1].find('.') >= 0:
                            base_notebook_name = split_path[-1]

                    filename_out = '/'.join([str(output.rstrip("/")), str(base_notebook_name)])
                    # with open(filename_out.rstrip("/"), 'wb') as fh:
                    #     copyfileobj(json.loads(r.text), fh)
                    f = open(filename_out.rstrip("/"), 'w', encoding = 'utf-8')
                    if f:
                        # writing file
                        json.dump(json.loads(r.text), f, ensure_ascii=False)#, indent=4)
                        # Closing file
                        f.close()

                    logging.info('Done writing to file.')
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('download_notebook_result , ' + str(e))
            raise Error(e)




    def list_datasets(self, mine = True):
        """Returns a list of datasets defined in the system
        Args:
        mine (boolean): return only datasets that I'm allowed to query (default: True)
        """

        try:

            params = {}
            if mine:
                params['mine'] = mine

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/list_datasets'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('still working...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('list datasets finished')
                    try:
                        df = pd.read_json(json.dumps(rJson))
                        return df
                    except Exception as e:
                        logging.info('No datasets were found.')
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('list_datasets , ' + str(e))
            raise Error(e)



    def list_schedules_notebook(self, n=10, rule_prefix = None):
        """Return a pandas data frame of the schedule rules.

        Args:
            n (int): The number of rules to return or all rules if 0 (default: 10)
            rule_prefix (str): If not None, return only rules whose names begin with the prefix (default: None)
        """

        try:

            params = {}
            if n:
                params['n'] = n
            if rule_prefix:
                params['rule_prefix'] = rule_prefix

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/listSchedulesNotebook'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing notebook schedules...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('list notebook schedules finished successfully.')
                    try:
                        df = pd.read_json(rJson)
                        return df
                    except Exception as e:
                        logging.info('No notebook schedules found.')
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('list_schedules_notebook , ' + str(e))
            raise Error(e)



    def describe_notebook_run(self, job_name= None, _showprocesslogging=True):
        """Stop the named processing job.
        Args:
        job_name (string): The name of the job to stop. use list_runs_notebook to get specific notebook Job name
        Returns:
          A dictionary with keys for each element of the job description. For example::

          {'Notebook': 'test.ipynb',
           'Rule': '',
           'Parameters': '{"input": "s3://notebook-testing/const.txt"}',
           'Job': 'papermill-test-2020-10-21-20-00-11',
           'Status': 'Completed',
           'Failure': None,
           'Created': datetime.datetime(2020, 10, 21, 13, 0, 12, 817000, tzinfo=tzlocal()),
           'Start': datetime.datetime(2020, 10, 21, 13, 4, 1, 58000, tzinfo=tzlocal()),
           'End': datetime.datetime(2020, 10, 21, 13, 4, 55, 710000, tzinfo=tzlocal()),
           'Elapsed': datetime.timedelta(seconds=54, microseconds=652000),
           'Result': 's3://dataplate/output/test-2020-10-21-20-00-11.ipynb',
           'Input': 's3://dataplate/input/notebook-2020-10-21-20-00-08.ipynb',
           'Image': 'notebook-runner',
           'Instance': 'ml.m5.large',
           'Role': 'BasicExecuteNotebookRole-us-west-2'}
        """

        try:

            params = {}
            if job_name:
                params['jobname'] = job_name
            else:
                raise Error('Not a valid job name, use list_runs_notebook function to get specific notebook Job name.')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                if _showprocesslogging:
                    logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/describeNotebookRun'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        if _showprocesslogging:
                            logging.info('analysing notebook details...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                if _showprocesslogging:
                    logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    try:
                        rJson = json.loads(r.text)
                        # res = ast.literal_eval(r.text)
                        if _showprocesslogging:
                            logging.info('describe notebook run finished successfully.')
                        return rJson
                    except Exception as e:
                        logging.info('Invalid notebook details found.')
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('describe_notebook_run , ' + str(e))
            raise Error(e)


    def wait_for_complete(self, job_name, progress=True, sleep_time=10):
        """Wait for a notebook execution job to complete.

        Args:
          job_name (str):
            The name of the SageMaker Processing Job executing the notebook. (Required)
          progress (boolean):
            If True, print a period after every poll attempt. (Default: True)
          sleep_time (int):
            The number of seconds between polls. (Default: 10)

        Returns:
          A tuple with the job status and the failure message if any.
        """

        done = False
        while not done:
            if progress:
                print(".", end="")
            desc = self.describe_notebook_run(job_name=job_name,_showprocesslogging=False)
            status = desc["Status"]
            if status != "InProgress":
                done = True
            else:
                time.sleep(sleep_time)
        if progress:
            print()
        return status, desc.get("FailureReason")


    def stop_schedule_notebook(self, rule_name= None):
        """Delete an existing notebook schedule rule.
        Args:
            rule_name (str): The name of the schedule rule (required).
        """

        try:
            params = {}
            if rule_name:
                params['rule_name'] = rule_name
            else:
                raise Error('Not a valid rule name, use list_schedules_notebook function to get specific notebook schedule rule name.')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/stopSchedule'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing notebook schedule stops...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    logging.info(r.text)
                    return
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('stop_schedule_notebook , ' + str(e))
            raise Error(e)



    def disable_schedule_notebook(self, rule_name= None):
        """Disable an existing notebook schedule rule.
        Args:
            rule_name (str): The name of the schedule rule (required).
        """

        try:
            params = {}
            if rule_name:
                params['rule_name'] = rule_name
            else:
                raise Error('Not a valid rule name, use list_schedules_notebook function to get specific notebook schedule rule name.')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/disableSchedule'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing disable notebook schedule...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    logging.info(r.text)
                    return
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('disable_schedule_notebook , ' + str(e))
            raise Error(e)



    def enable_schedule_notebook(self, rule_name= None):
        """Enable an existing notebook schedule rule.
        Args:
            rule_name (str): The name of the schedule rule (required).
        """

        try:
            params = {}
            if rule_name:
                params['rule_name'] = rule_name
            else:
                raise Error('Not a valid rule name, use list_schedules_notebook function to get specific notebook schedule rule name.')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/enableSchedule'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing enable notebook schedule...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    logging.info(r.text)
                    return
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('enable_schedule_notebook , ' + str(e))
            raise Error(e)



    def schedule_notebook(self, notebook_file_path, rule_name = None, schedule = None, event_pattern = None, instance_type = "ml.m5.large", parameters = "{}", image = None, max_time_limit_minutes = 180, securityGroupIds = [], subnets= [], role = None, tags = None, project = None, sub_project= None):
        """ Create a schedule for invoking a notebook in a specific cron/rate based intervals

            Creates a scheduled rule to invoke the notebook (calling run_notebook) on the provided schedule or in response
            to the provided event \

            :meth:
            To find jobs run by the schedule, see :meth:`list_runs_notebook` using the `rule` argument to filter to 
            a specific rule. To download the results, see :meth:`download_notebook_result` 

            dataplate.schedule_notebook(notebook="powers.ipynb", rule_name="Powers", schedule="rate(1 hour)")

            Args:
                notebook (str): The notebook file path.
                rule_name (str): The name of the rule for CloudWatch Events (required).
                schedule (str): A schedule string which defines when the job should be run. For details, 
                                see https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html 
                                (default: None)
                event_pattern (str): A pattern for events that will trigger notebook execution. For details,
                             see https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html.
                             (default: None. Note: one of `schedule` or `event_pattern` must be specified).
                input_path (str): The S3 object containing the notebook. If this is None, the `notebook` argument is
                                  taken as a local file to upload (default: None).
                parameters (dict): The dictionary of parameters to pass to the notebook (default: {}).
                image (str): The name of the image (e.g. my-tensorflow) , default: notebook-runner
                instance_type (str): The SageMaker instance to use for executing the job (default: ml.m5.large).
                max_time_limit_minutes : maximum minutes to run before force stop
                securityGroupIds : a list of securityGroup Ids of aws for the processing job to communicate with, in case communication with other resources, e.g. internal dataplate service, is needed
                subnets : a list of subnets of aws for the processing job to communicate with
                role : a role ARN to run the notebook, the default is the Dataplate service role (cross rols in case of Sass)
                tags : tags to add to the processingJob - this is mostly for pricing management. format as array of key/value jsons:  [{"Key": "project","Value": "my_project"},{"Key": "product","Value": "Research"}]
                project : project name to add the processingJob to and enable easy search. Must define sub_project as well. Must satisfy regular expression: ^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}
                sub_project : sub project name to be added to specific project name and enable easy search. Must define project as well, . Must satisfy regular expression: ^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}
            """
        try:
            if not notebook_file_path or not os.path.isfile(notebook_file_path) or not notebook_file_path.endswith('.ipynb'):
                raise FileNotFoundError(f'notebook file is not legal/valid : {notebook_file_path if notebook_file_path else "None"}')

            f = open(notebook_file_path, 'r')
            if f:
                # Reading from file
                notebook_json_data = json.loads(f.read())
                # Closing file
                f.close()

            if not notebook_json_data or len(json.dumps(notebook_json_data)) < 10 or not 'cells' in notebook_json_data:
                raise Error(f'notebook file is not legal : {notebook_file_path if notebook_file_path else "None"}')

            notebook_name = os.path.basename(notebook_file_path)
            params = {}
            if instance_type:
                params['instance_type'] = instance_type
            if parameters:
                params['parameters'] = parameters
            if max_time_limit_minutes:
                params['timelimit_minutes'] = max_time_limit_minutes
            if image:
                params['image'] = image
            params['SecurityGroupIds'] = json.dumps(securityGroupIds)
            params['Subnets'] = json.dumps(subnets)
            params['notebook_name'] = notebook_name if notebook_name else ""
            if not rule_name:
                raise Error(f'rule_name is required')
            if not schedule and not event_pattern:
                raise Error(f'schedule or event_pattern is required, for cron scheduling see https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html#eb-cron-expressions')
            elif schedule and len(schedule) < 4:
                raise Error(
                    f'schedule not defined properly, see https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html#eb-cron-expressions')
            elif event_pattern and len(event_pattern) < 4:
                raise Error(
                    f'event_pattern not defined properly, see https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html')
            params['rule_name'] = rule_name
            if schedule:
                params['schedule'] = schedule
            if event_pattern:
                params['event_pattern'] = event_pattern
            if role:
                params['role'] = role
            if tags:
                params['tags'] = json.dumps(tags)
            if project:
                params['project'] = project
            if sub_project:
                params['sub_project'] = sub_project

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/scheduleNotebook'.format(self.base_url), params=params, data=json.dumps(notebook_json_data),
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('scheduling notebook, processing...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('schedule notebook finished successfully.')
                    return json.dumps(rJson)
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('schedule_notebook , ' + str(e))
            raise Error(e)


    def run_notebook_after_schedule(self, notebook_file_path, rule_name = None, trigger_rule_name = None, trigger_rule_status = "Completed" ,instance_type = "ml.m5.large", parameters = "{}", image = None, max_time_limit_minutes = 180, securityGroupIds = [], subnets= [], role = None, tags = None, project = None, sub_project= None):
        """invoke a notebook run after another scheduled notebook Completed/InProgress/Failed.

            Creates a rule to invoke the notebook once a scheduled notebook rule status changed to Completed/InProgress/Failed

            :meth:
            To find jobs run by the schedule, see :meth:`list_runs_notebook` using the `rule` argument to filter to
            a specific rule. To download the results, see :meth:`download_notebook_result`

            dataplate.run_notebook_after_schedule(notebook="powers.ipynb", rule_name="Powers-follow", trigger_rule_name="Powers")

            Args:
                notebook (str): The notebook file path.
                rule_name (str): The name of the rule for CloudWatch Events (required).
                trigger_rule_name (str): A scheduled rule name of another scheduled notebook that will trigger this notebook once Completed/InProgress/Failed
                trigger_rule_status (str): The state of the trigger_rule_name scheduled notebook that this notebook will listen for invokation (default='Completed')
                                           options: 'Completed','InProgress','Failed'
                input_path (str): The S3 object containing the notebook. If this is None, the `notebook` argument is
                                  taken as a local file to upload (default: None).
                parameters (dict): The dictionary of parameters to pass to the notebook (default: {}).
                image (str): The name of the image (e.g. my-tensorflow) , default: notebook-runner
                instance_type (str): The SageMaker instance to use for executing the job (default: ml.m5.large).
                max_time_limit_minutes : maximum minutes to run before force stop
                securityGroupIds : a list of securityGroup Ids of aws for the processing job to communicate with, in case communication with other resources, e.g. internal dataplate service, is needed
                subnets : a list of subnets of aws for the processing job to communicate with
                role : a role ARN to run the notebook, the default is the Dataplate service role (cross rols in case of Sass)
                tags : tags to add to the processingJob - this is mostly for pricing management. format as array of key/value jsons:  [{"Key": "project","Value": "my_project"},{"Key": "product","Value": "Research"}]
                project : project name to add the processingJob to and enable easy search. Must define sub_project as well. Must satisfy regular expression: ^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}
                sub_project : sub project name to be added to specific project name and enable easy search. Must define project as well, . Must satisfy regular expression: ^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}
            """
        try:
            if not notebook_file_path or not os.path.isfile(notebook_file_path) or not notebook_file_path.endswith('.ipynb'):
                raise FileNotFoundError(f'notebook file is not legal/valid : {notebook_file_path if notebook_file_path else "None"}')

            f = open(notebook_file_path, 'r')
            if f:
                # Reading from file
                notebook_json_data = json.loads(f.read())
                # Closing file
                f.close()

            if not notebook_json_data or len(json.dumps(notebook_json_data)) < 10 or not 'cells' in notebook_json_data:
                raise Error(f'notebook file is not legal : {notebook_file_path if notebook_file_path else "None"}')

            notebook_name = os.path.basename(notebook_file_path)
            params = {}
            if instance_type:
                params['instance_type'] = instance_type
            if parameters:
                params['parameters'] = parameters
            if max_time_limit_minutes:
                params['timelimit_minutes'] = max_time_limit_minutes
            if image:
                params['image'] = image
            params['SecurityGroupIds'] = json.dumps(securityGroupIds)
            params['Subnets'] = json.dumps(subnets)
            params['notebook_name'] = notebook_name if notebook_name else ""
            if not rule_name:
                raise Error(f'rule_name is required')
            if not trigger_rule_name:
                raise Error(f'trigger_rule_name is required, for following a specific scheduled rule that will trigger this notebook')
            if trigger_rule_status:
                if trigger_rule_status != 'Completed' and trigger_rule_status != 'InProgress' and trigger_rule_status != 'Failed':
                    raise Error(
                        f"trigger_rule_status is invalid, options: 'Completed','InProgress','Failed'")
            params['rule_name'] = rule_name
            params['trigger_rule_name'] = trigger_rule_name
            params['trigger_rule_status'] = trigger_rule_status
            if role:
                params['role'] = role
            if tags:
                params['tags'] = json.dumps(tags)
            if project:
                params['project'] = project
            if sub_project:
                params['sub_project'] = sub_project

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/runNotebookAfterSchedule'.format(self.base_url), params=params, data=json.dumps(notebook_json_data),
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('creating rule to invoke notebook after scheduled notebook, processing...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('rule to invoke notebook finished successfully.')
                    return json.dumps(rJson)
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('invoke_notebook_after_schedule , ' + str(e))
            raise Error(e)



    def run_notebook_after_notebook(self, notebook_file_path, rule_name = None, trigger_notebook_name = None, trigger_notebook_status = "Completed" ,instance_type = "ml.m5.large", parameters = "{}", image = None, max_time_limit_minutes = 180, securityGroupIds = [], subnets= [], role = None, tags = None, project = None, sub_project= None):
        """invoke a notebook run after another scheduled notebook Completed/InProgress/Failed.

            Creates a rule to invoke the notebook once a scheduled notebook rule status changed to Completed/InProgress/Failed

            :meth:
            To find jobs run by the schedule, see :meth:`list_runs_notebook` using the `rule` argument to filter to
            a specific rule. To download the results, see :meth:`download_notebook_result`

            dataplate.run_notebook_after_schedule(notebook="powers.ipynb", rule_name="myNotebook-power-follow", trigger_notebook_name="myNotebook.ipynb")

            Args:
                notebook (str): The notebook file path.
                rule_name (str): The name of the rule for CloudWatch Events (required).
                trigger_notebook_name (str): A notebook name of another notebook that will trigger this notebook once Completed/InProgress/Failed
                trigger_notebook_status (str): The state of the trigger_notebook_name notebook that this notebook will listen for invokation (default='Completed')
                                           options: 'Completed','InProgress','Failed'
                input_path (str): The S3 object containing the notebook. If this is None, the `notebook` argument is
                                  taken as a local file to upload (default: None).
                parameters (dict): The dictionary of parameters to pass to the notebook (default: {}).
                image (str): The name of the image (e.g. my-tensorflow) , default: notebook-runner
                instance_type (str): The SageMaker instance to use for executing the job (default: ml.m5.large).
                max_time_limit_minutes : maximum minutes to run before force stop
                securityGroupIds : a list of securityGroup Ids of aws for the processing job to communicate with, in case communication with other resources, e.g. internal dataplate service, is needed
                subnets : a list of subnets of aws for the processing job to communicate with
                role : a role ARN to run the notebook, the default is the Dataplate service role (cross rols in case of Sass)
                tags : tags to add to the processingJob - this is mostly for pricing management. format as array of key/value jsons:  [{"Key": "project","Value": "my_project"},{"Key": "product","Value": "Research"}]
                project : project name to add the processingJob to and enable easy search. Must define sub_project as well. Must satisfy regular expression: ^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}
                sub_project : sub project name to be added to specific project name and enable easy search. Must define project as well, . Must satisfy regular expression: ^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}
            """
        try:
            if not notebook_file_path or not os.path.isfile(notebook_file_path) or not notebook_file_path.endswith('.ipynb'):
                raise FileNotFoundError(f'notebook file is not legal/valid : {notebook_file_path if notebook_file_path else "None"}')

            f = open(notebook_file_path, 'r')
            if f:
                # Reading from file
                notebook_json_data = json.loads(f.read())
                # Closing file
                f.close()

            if not notebook_json_data or len(json.dumps(notebook_json_data)) < 10 or not 'cells' in notebook_json_data:
                raise Error(f'notebook file is not legal : {notebook_file_path if notebook_file_path else "None"}')

            notebook_name = os.path.basename(notebook_file_path)
            params = {}
            if instance_type:
                params['instance_type'] = instance_type
            if parameters:
                params['parameters'] = parameters
            if max_time_limit_minutes:
                params['timelimit_minutes'] = max_time_limit_minutes
            if image:
                params['image'] = image
            params['SecurityGroupIds'] = json.dumps(securityGroupIds)
            params['Subnets'] = json.dumps(subnets)
            params['notebook_name'] = notebook_name if notebook_name else ""
            if not rule_name:
                raise Error(f'rule_name is required')
            if not trigger_notebook_name:
                raise Error(f'trigger_notebook_name is required, for following a specific notebook rule that will trigger this notebook')
            if trigger_notebook_status:
                if trigger_notebook_status != 'Completed' and trigger_notebook_status != 'InProgress' and trigger_notebook_status != 'Failed':
                    raise Error(
                        f"trigger_rule_status is invalid, options: 'Completed','InProgress','Failed'")
            params['rule_name'] = rule_name
            params['trigger_notebook_name'] = trigger_notebook_name
            params['trigger_notebook_status'] = trigger_notebook_status
            if role:
                params['role'] = role
            if tags:
                params['tags'] = json.dumps(tags)
            if project:
                params['project'] = project
            if sub_project:
                params['sub_project'] = sub_project

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/runNotebookAfterNotebook'.format(self.base_url), params=params, data=json.dumps(notebook_json_data),
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('creating rule to invoke notebook after scheduled notebook, processing...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('rule to invoke notebook finished successfully.')
                    return json.dumps(rJson)
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('invoke_notebook_after_notebook , ' + str(e))
            raise Error(e)


    def scan_notebook(self, notebook_file_path, parameters = "{}", apply_style=True, archive=True):
        """Scan a notebook Job result for security issue.
        Args:
            notebook (str): The notebook file path.
            input_path (str): The S3 object containing the notebook. If this is None, the `notebook` argument is
                              taken as a local file to upload (default: None).
            parameters (dict): The dictionary of parameters to pass to the scanner (default: {}).
            apply_style (bool): should the result DataFrame be formatted with style
            archive (bool): archive the report to later view in DataPlate server Reporting menu (default=True)
        Returns:
            Json list of compromised (exceptions, suspicious, dangerous actions)
        """
        try:
            if not notebook_file_path or not os.path.isfile(notebook_file_path) or not notebook_file_path.endswith('.ipynb'):
                raise FileNotFoundError(f'notebook file is not legal/valid : {notebook_file_path if notebook_file_path else "None"}')

            f = open(notebook_file_path, 'r')
            if f:
                # Reading from file
                notebook_json_data = json.loads(f.read())
                # Closing file
                f.close()

            if not notebook_json_data or len(json.dumps(notebook_json_data)) < 10 or not 'cells' in notebook_json_data:
                raise Error(f'notebook file is not legal : {notebook_file_path if notebook_file_path else "None"}')

            notebook_name = os.path.basename(notebook_file_path)
            params = {}
            if parameters:
                params['parameters'] = parameters

            params['notebook_name'] = notebook_name if notebook_name else ""
            params['archive'] = archive

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/sec/scanNotebook'.format(self.base_url), params=params, data=json.dumps(notebook_json_data),
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('scanning notebook, processing...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('scan notebook finished successfully.')
                    parsed_json = ast.literal_eval(rJson)
                    df_compromise = pd.read_json(json.dumps(parsed_json))

                    def colour_severity(series):
                        red = 'background-color: lightcoral;'  # red
                        orange = 'background-color: orange;'
                        yellow = 'background-color: lightyellow;'
                        default = ''

                        # note multiple else ..if conditions
                        return [
                            red if e == 'critical' else orange if e == 'warning' else yellow if e == 'notice' else default
                            for e in series]

                    if apply_style and not df_compromise.empty:
                        if 'compromise_severity' in df_compromise.columns:
                            df_compromise = df_compromise.style.set_properties(
                                **{'border': '1px black solid !important'}).set_table_attributes(
                                'style="border-collapse:collapse"'
                            ).set_table_styles([{'selector': 'tr:hover',
                                                 'props': 'background-color: lightblue; font-size: 1em;'}, {
                                                    'selector': '.col_heading',
                                                    'props': 'background-color: lightblue; color: black; border-collapse: collapse; border: 1px black solid !important;'
                                                }]).apply(colour_severity, axis=0, subset=['compromise_severity'])
                    # df_compromise = df_compromise.style.apply(colour_severity, axis=0, subset=['compromise_severity'])
                    return df_compromise#r.text.replace('"','')#json.dumps(rJson)
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('scan_notebook , ' + str(e))
            raise Error(e)


    def analyzeNotebookResult(self, job_name= None):
        """Analyze the named job.
        Args:
        job_name (string): The name of the job to stop. use list_runs_notebook to get specific notebook Job name
        """
        try:
            params = {}
            if job_name:
                params['jobname'] = job_name
            else:
                raise Error('Not a valid job name, use list_runs_notebook function to get specific notebook Job name.')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/sec/analyzeNotebookResult'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing notebook stops...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    # logging.info(r.text)
                    # rJson = json.loads(r.text)
                    logging.info('analyze notebook finished successfully.')
                    # parsed_json = ast.literal_eval(rJson)
                    df_compromise = pd.read_json(r.text)
                    return df_compromise
                    # return
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('stop_run_notebook , ' + str(e))
            raise Error(e)


    def recreate_inference_endpoint(self, endpoint_name, container_full_name, instance_type="ml.m5.large", initial_instance_count=1,
                                    initial_variant_weight=1, mode="SingleModel", model_url=None, securityGroupIds=[], subnets=[], role=None):
        """ Create/Update an inference EndPoint in SageMaker - including recreate model, configuration resigtry and endpoint
        Args:
            endpoint_name (str): The name for the endpoint,model and endpoint config
            container_full_name (str): full container name e.g. YOUR_AWS_ACCOUNTID.dkr.ecr.us-east-1.amazonaws.com/my_container:latest
            instance_type (str): The SageMaker instance to use (default: ml.m5.large).
            initial_instance_count : Initial amount of instances to start from (with or without auto scaling)
            initial_variant_weight : Determines initial traffic distribution among all of the models e.g 0.5 is 50% (default = 1.0)
            mode : SingleModel | MultiModel (default is SingleModel)
            model_url : In case of MultiModel ,the maximum s3 path that all models are located in
            securityGroupIds : a list of securityGroup Ids of aws for the processing job to communicate with, in case communication with other resources, e.g. internal dataplate service, is needed
            subnets : a list of subnets of aws for the processing job to communicate with
            role : a role ARN to run the notebook, the default is the Dataplate service role (cross rols in case of Sass)
        Returns:
            The arn of the inference EndPoint created
        """
        try:
            if not endpoint_name or len(endpoint_name) == 0:
                raise FileNotFoundError(
                    f'model_name is not legal/valid : {endpoint_name if endpoint_name else "None"}')


            if not container_full_name or len(container_full_name) < 47 :
                raise Error(f'please check your container_full_name : {container_full_name if container_full_name else "None"}')

            params = {}
            if instance_type:
                params['instance_type'] = instance_type
            if initial_instance_count:
                params['initial_instance_count'] = initial_instance_count
            if initial_variant_weight:
                params['initial_variant_weight'] = initial_variant_weight
            params['SecurityGroupIds'] = json.dumps(
                securityGroupIds)  # ','.join(['"%s"' % w for w in securityGroupIds])
            params['Subnets'] = json.dumps(subnets)  # ','.join(['"%s"' % w for w in subnets])
            params['endpoint_name'] = endpoint_name
            params['container_full_name'] = container_full_name
            params['mode'] = mode
            if model_url:
                params['model_url'] = model_url
            if role:
                params['role'] = role

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('Deleting previous endpoint...')
                r = self.session.post( \
                    '{}/api/aws/deleteEndpoint'.format(self.base_url), params=params,
                    data=json.dumps({}),
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('re-creating inference endpoint, processing...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    logging.info('delete inference endpoint finished successfully')
                    logging.info(r.text)  # json.dumps(rJson)
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)
            except Exception as e:
                logging.exception('Could not find relevant endpoint - continue to create')

            try:
                logging.info('Creating endpoint...')
                r = self.session.post( \
                    '{}/api/aws/recreateEndpoint'.format(self.base_url), params=params,
                    data=json.dumps({}),
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('re-creating inference endpoint, processing...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    logging.info('re-creating inference endpoint finished successfully - it may take few minute for it to be available.')
                    return r.text  # json.dumps(rJson)
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('recreate_inference_endpoint , ' + str(e))
            raise Error(e)



    def delete_inference_endpoint(self, endpoint_name):
        """ Delete an inference EndPoint in SageMaker - includes deleting also configuration resigtry , model and endpoint
        Args:
            endpoint_name (str): The name for the endpoint,model and endpoint config (should be the same name for all)
        """
        try:
            if not endpoint_name or len(endpoint_name) == 0:
                raise FileNotFoundError(
                    f'model_name is not legal/valid : {endpoint_name if endpoint_name else "None"}')


            params = {}
            params['endpoint_name'] = endpoint_name

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            logging.info('Deleting endpoint...')
            r = self.session.post( \
                '{}/api/aws/deleteEndpoint'.format(self.base_url), params=params,
                data=json.dumps({}),
                headers=headers, stream=True, allow_redirects=False)

            if r.status_code != 200:
                if r.status_code == 302:
                    raise Error(
                        'Bad Access Key! Get your access key at: {}'.format(
                            self.base_url))
                if r.status_code == 206:
                    logging.info('re-creating inference endpoint, processing...')
                    time.sleep(5)
                raise Error(
                    'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                        format(r.status_code, r.text))

            logging.info('Parsing response')
            # logging.info(str(r.text))
            if r.text:
                logging.info('delete inference endpoint finished successfully')
                logging.info(r.text)  # json.dumps(rJson)
            else:
                logging.exception('Could not find proper output, please check your parameters')
            # return r.text

        except (requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout) as e:
            logging.exception('Got ConnectionError/ReadTimeout exception.')
            raise Error(e)
        except Exception as e:
            logging.exception('Could not find relevant endpoint')


    def save_statistic(self, variable_name, variable_value):
        """ Save a statistics to follow later - can big a matplotlib-figure/dataframe/string/dict/json/int/float
            You can later call the report_statistic API to get a list of all statistics of last X runs
        Args:
            variable_name (str): The name for the statistics
            variable_value : can be any value or type matplotlib-figure/dataframe/string/dict/json/int/float
        """
        try:
            import scrapbook as sb
            from IPython.display import clear_output
            clear_output()
            if not variable_name:
                logging.exception('Could not save statistic: make sure variable_name and variable_value are defined')
            if str(type(variable_value)) == "<class 'matplotlib.figure.Figure'>":
                logging.info(f'found Figure type')
                sb.glue(variable_name, variable_value, 'display')
            elif str(type(variable_value)) == "<class 'pandas.core.frame.DataFrame'>":
                logging.info(f'found DataFrame type')
                sb.glue(variable_name, variable_value, 'pandas')
            else:
                sb.glue(variable_name, variable_value)

            logging.info(f'statistics {variable_name} saved successfully')
        except Exception as e:
            logging.exception('Could not save statistic: make sure the variable_value is either: dataframe/string/dict/json/int/float/matplotlib-figure')


    def report_statistic(self, notebook_name, number_runs=5, include_data=False, embed_report=True, archive=True):
        """ Report a statistics that was saved using the save_statistic API
            Get a list of all statistics of last X runs
        Args:
            notebook_name (str): The name for the notebook to get the last statistics report for
            number_runs (int): number of last X runs to show statistics report for (default=5)
            include_data (bool): should include dataFrames or other data. By default includes only figures (default=False)
            embed_report (bool): display report as iFrame inside the notebook (default=True)
            archive (bool): archive the report to later view in DataPlate server Reporting menu (default=True)
        """
        # deleteHtmlResult (bool): delete the html output local report (default=False)
        try:
            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            if not notebook_name or len(notebook_name) == 0:
                raise FileNotFoundError(
                    f'notebook_name is not legal/valid : {notebook_name if notebook_name else "None"}')

            params = {}
            params['notebook_name'] = notebook_name
            params['number_runs'] = number_runs
            params['include_data'] = include_data
            params['archive'] = archive

            logging.info('sending report request...')
            r = self.session.post( \
                '{}/api/aws/reportNotebookStatistics'.format(self.base_url), params=params, data=json.dumps('{}'),
                headers=headers, stream=True, allow_redirects=False)

            if r.status_code != 200:
                if r.status_code == 302:
                    raise Error(
                        'Bad Access Key! Get your access key at: {}'.format(
                            self.base_url))
                if r.status_code == 206:
                    logging.info('scanning notebook, processing...')
                    time.sleep(5)
                raise Error(
                    'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                        format(r.status_code, r.text))

            logging.info('Parsing response')
            # logging.info(str(r.text))
            if r.text:
                output_read_path = r.text
                if output_read_path:
                    str_report_name = "html_report_" + str(datetime.now())[:19].strip() + ".html"
                    with open(str_report_name, "w") as f:
                        f.write(output_read_path)

                    logging.info('report statistics retrieved successfully.')
                    output = f'%%html\n<iframe src="{str_report_name}" width="100%" height="1200"></iframe>'
                    if embed_report:
                        import IPython
                        IPython.get_ipython().run_cell(output)
                    # if deleteHtmlResult:
                    #     os.remove(str_report_name)
                    return str_report_name
                else:
                    logging.exception('Could not get statistics report properly - please check your s3 connection')
            else:
                logging.exception('Could not find proper output, please check your parameters')
            # return r.text

        except (requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout) as e:
            logging.exception('Got ConnectionError/ReadTimeout exception.')
            raise Error(e)

        except Exception as e:
            logging.exception('scan_notebook , ' + str(e))
            raise Error(e)


    def list_projects(self, n=10, name_contains=None):
        """Return a pandas data frame of the projects.

        Args:
            n (int): The number of projects to return or all projects if 0 (default: 10)
            name_contains (str): Search for projects that contain this string
        """

        try:

            params = {}
            if n:
                params['n'] = n
            if name_contains:
                params['name_contains'] = name_contains

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                res = self.session.get('{}/version'.format(self.base_url))
                is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.27.00'
                if not is_new_enough:
                    logging.exception(
                        'This API requires server version >= 1.27.00, please update your DataPlate server')
                    return

                r = self.session.post( \
                    '{}/api/aws/listProjects'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing projects...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('list projects finished successfully.')
                    try:
                        df = pd.read_json(rJson)
                        return df
                    except Exception as e:
                        logging.info('No projects found.')
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('list_projects , ' + str(e))
            raise Error(e)


    def list_sub_projects(self, project_name = None, n=10):
        """Return a pandas data frame of the projects.

        Args:
            n (int): The number of sub-projects to return or all sub-projects if 0 (default: 10)
            project_name (string): The project name to search sub-projects for (must be defined)
        """

        try:

            params = {}
            if n:
                params['n'] = n
            if project_name:
                params['project_name'] = project_name
            else:
                raise Error(
                    'Project name must be defined')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                # backword compatability
                res = self.session.get('{}/version'.format(self.base_url))
                is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.27.00'
                if not is_new_enough:
                    logging.exception(
                        'This API requires server version >= 1.27.00, please update your DataPlate server')
                    return

                r = self.session.post( \
                    '{}/api/aws/listSubProjects'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing sub projects...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('list sub-projects finished successfully.')
                    try:
                        df = pd.read_json(rJson)
                        return df
                    except Exception as e:
                        logging.info('No sub-projects found.')
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('list_sub_projects , ' + str(e))
            raise Error(e)



    def list_containers(self, n=0, repositories_prefix='notebook'):
        """Return a pandas data frame of the containers used to run notebooks.
           more info: https://api.dataplate.io/reference/api-reference/build-your-own-notebook-container
        Args:
            n (int): The number of containers to return or all containers if 0 (default: 0)
            repositories_prefix (string) - Optional: The containers repositories prefix (in AWS ECR) to search containers (default: 'notebook')
        """

        try:
            params = {}
            if n:
                params['n'] = n
            if repositories_prefix:
                params['repositories_prefix'] = repositories_prefix
            else:
                raise Error(
                    'Project name must be defined')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')

                # backword compatability
                res = self.session.get('{}/version'.format(self.base_url))
                is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.27.03'
                if not is_new_enough:
                    logging.exception('This API requires server version >= 1.27.03, please update your DataPlate server')
                    return

                r = self.session.post( \
                    '{}/api/aws/listNotebookRepositories'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing containers...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('list containers finished successfully.')
                    try:
                        df = pd.read_json(rJson)
                        return df
                    except Exception as e:
                        logging.info('No containers found.')
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('list_containers , ' + str(e))
            raise Error(e)

    def run_batch_step(self,
                       cluster_id=None,
                       file=None,
                       class_name=None,
                       args=None,
                       jars=None,
                       py_files = None,
                       files=None,
                       driver_memory = None,
                       driver_cores = None,
                       executor_memory = None,
                       executor_cores = None,
                       num_executors = None,
                       archives = None,
                       queue = None,
                       name = None,
                       spark_conf = None,
                       retries = 1,
                       async_m=None,
                       request_timeout=None,
                       grace_seconds=30,
                       max_retries_sleep_seconds=60,
                       **kwargs):

        """
        Executes batch jar/spark/pyspark step on current default dataplate EMR, and output the log as text.

        Parameters
        ----------
        cluster_id: if specified use this cluster (must have Livy application installed on the cluster) ,else use the DataPlate default emr defined in system configuration
        file: File containing the application to execute. (path - required)
        class_name: Application Java/Spark main class.
        args: Command line arguments for the application (list of strings)
        jars: URLs of jars to be used in this session. (list of strings)
        py_files: URLs of Python files to be used in this session. (list of strings)
        files: URLs of files to be used in this session. (list of strings)
        driver_memory: Amount of memory to use for the driver process
            (e.g. '512m').
        driver_cores: Number of cores to use for the driver process.
        executor_memory: Amount of memory to use per executor process
            (e.g. '512m').
        executor_cores: Number of cores to use for each executor.
        num_executors: Number of executors to launch for this session.
        archives: URLs of archives to be used in this session.
        queue: The name of the YARN queue to which submitted.
        name: The name of this session.
        spark_conf: Spark configuration properties.
        """

        headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
        params = {}
        refresh = True
        if refresh:
            params['refresh'] = '1'
        if async_m:
            timeout = time.time() + async_m * 60
            params['async'] = '1'
        if grace_seconds:
            params['grace_seconds'] = grace_seconds

        if cluster_id is not None:
            params['cluster_id'] = cluster_id
        if file is not None:
            params["file"] = file
        if class_name is not None:
            params["class_name"] = class_name
        if args is not None:
            params['args'] = json.dumps(args)
        if jars is not None:
            params["jars"] = json.dumps(jars)
        if py_files is not None:
            params["pyFiles"] = json.dumps(py_files)
        if files is not None:
            params["files"] = json.dumps(files)
        if driver_memory is not None:
            params["driverMemory"] = driver_memory
        if driver_cores is not None:
            params["driverCores"] = driver_cores
        if executor_memory is not None:
            params["executorMemory"] = executor_memory
        if executor_cores is not None:
            params["executorCores"] = executor_cores
        if num_executors is not None:
            params["numExecutors"] = num_executors
        if archives is not None:
            params["archives"] = archives
        if queue is not None:
            params["queue"] = queue
        if name is not None:
            params["name"] = name
        if spark_conf is not None:
            params["spark_conf"] = spark_conf

        while True:
            if async_m and timeout < time.time():
                raise Error('Timeout waiting for batch step.')
            try:
                logging.info('Sending batch step data...')
                logging.info('waiting for job completion')
                r = self.session.post( \
                    '{}/api/run_batch_step'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False, timeout=request_timeout)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('Batch step is processing, waiting a bit...')
                        time.sleep(5)
                        continue
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))


                # logging.info(str(r.text))
                if r.text:
                    logging.info('batch step finished')
                    logging.info('Got batch step log, dump text response/errors')
                    # logging.info(r.text)
                    # rJson = json.loads(r.text)
                    # logging.info(f'Done listing.')
                    return r.text
                else:
                    logging.exception('Could not find proper output, please check your code')
                # return r.text
                # logging.info('Done writing to file.')
                break
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout, http_incompleteRead, urllib3_incompleteRead) as e:
                logging.exception('Got ConnectionError/IncompleteRead/ReadTimeout exception.')
                retries -= 1
                if retries <= 0:
                    raise Error(e)
                rand = randint(30, max_retries_sleep_seconds)
                logging.info(f'Retrying request. in {rand} seconds, according to max_retries_sleep_seconds')
                time.sleep(rand)
                continue


    class _EMR():

        def __init__(self, dataplate):
            self._dataplate = dataplate

        def create_cluster(self, *args, **kwargs):
            try:
                sig = signature(wr.emr.create_cluster)
                sba = sig.bind(*args, **kwargs)

                json_kwargs_object = json.dumps(kwargs, default=str)
                json_args_object = json.dumps(args)

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}
                # params = json.dumps(kwargs)#{}

                try:

                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.00'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.00, please update your DataPlate server')
                        return

                    logging.info('Sending request...')
                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_create_cluster'.format(self._dataplate.base_url), data=json_kwargs_object,
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('create emr cluster in AWS...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    if r.text:
                        rJson = json.loads(r.text)
                        logging.info(f'Done listing.')
                        return rJson
                    else:
                        logging.exception('Could not find proper output, please check your parameters')

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('emr_create_cluster , ' + str(e))
                raise Error(e)

        create_cluster.__doc__ = wr.emr.create_cluster.__doc__.replace('import awswrangler as wr',
                                                                     'from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
        create_cluster.__doc__ = create_cluster.__doc__.replace('wr.emr.create_cluster', 'dataplate.emr.create_cluster')


        def submit_step(self, *args, **kwargs):
            try:
                sig = signature(wr.emr.submit_step)
                sba = sig.bind(*args, **kwargs)

                json_kwargs_object = json.dumps(kwargs, default=str)
                json_args_object = json.dumps(args)

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}
                # params = json.dumps(kwargs)#{}

                try:

                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.00'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.00, please update your DataPlate server')
                        return

                    logging.info('Sending request...')
                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_submit_step'.format(self._dataplate.base_url), data=json_kwargs_object,
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('Submit EMR step to cluster on AWS...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    if r.text:
                        rJson = json.loads(r.text)
                        logging.info(f'Done listing.')
                        return rJson
                    else:
                        logging.exception('Could not find proper output, please check your parameters')

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('emr_submit_step , ' + str(e))
                raise Error(e)

        submit_step.__doc__ = wr.emr.submit_step.__doc__.replace('import awswrangler as wr',
                                                                     'from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
        submit_step.__doc__ = submit_step.__doc__.replace('wr.emr.submit_step', 'dataplate.emr.submit_step')


        def terminate_cluster(self, *args, **kwargs):
            try:
                sig = signature(wr.emr.terminate_cluster)
                sba = sig.bind(*args, **kwargs)

                json_kwargs_object = json.dumps(kwargs, default=str)
                json_args_object = json.dumps(args)

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}
                # params = json.dumps(kwargs)#{}

                try:
                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.00'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.00, please update your DataPlate server')
                        return

                    logging.info('Sending request...')
                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_terminate_cluster'.format(self._dataplate.base_url), data=json_kwargs_object,
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('Terminate EMR cluster on AWS...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    if r.text:
                        rJson = json.loads(r.text)
                        logging.info(f'Done listing.')
                        return rJson
                    else:
                        logging.exception('Could not find proper output, please check your parameters')

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('emr_terminate_cluster , ' + str(e))
                raise Error(e)

        terminate_cluster.__doc__ = wr.emr.terminate_cluster.__doc__.replace('import awswrangler as wr',
                                                                     'from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
        terminate_cluster.__doc__ = terminate_cluster.__doc__.replace('wr.emr.terminate_cluster', 'dataplate.emr.terminate_cluster')



        def cluster_state(self, *args, **kwargs):
            try:
                sig = signature(wr.emr.get_cluster_state)
                sba = sig.bind(*args, **kwargs)

                json_kwargs_object = json.dumps(kwargs, default=str)
                json_args_object = json.dumps(args)

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}
                # params = json.dumps(kwargs)#{}

                try:
                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.00'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.00, please update your DataPlate server')
                        return

                    logging.info('Sending request...')
                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_cluster_state'.format(self._dataplate.base_url), data=json_kwargs_object,
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('Get EMR cluster state on AWS...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    if r.text:
                        rJson = json.loads(r.text)
                        logging.info(f'Done listing.')
                        return rJson
                    else:
                        logging.exception('Could not find proper output, please check your parameters')

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('emr_cluster_state , ' + str(e))
                raise Error(e)

        cluster_state.__doc__ = wr.emr.get_cluster_state.__doc__.replace('import awswrangler as wr',
                                                                     'from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
        cluster_state.__doc__ = cluster_state.__doc__.replace('wr.emr.get_cluster_state', 'dataplate.emr.cluster_state')



        def step_state(self, *args, **kwargs):
            try:
                sig = signature(wr.emr.get_step_state)
                sba = sig.bind(*args, **kwargs)

                json_kwargs_object = json.dumps(kwargs, default=str)
                json_args_object = json.dumps(args)

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}
                # params = json.dumps(kwargs)#{}

                try:
                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.00'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.00, please update your DataPlate server')
                        return

                    logging.info('Sending request...')
                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_step_state'.format(self._dataplate.base_url), data=json_kwargs_object,
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('Get EMR step state on AWS...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    if r.text:
                        rJson = json.loads(r.text)
                        logging.info(f'Done listing.')
                        return rJson
                    else:
                        logging.exception('Could not find proper output, please check your parameters')

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('emr_step_state , ' + str(e))
                raise Error(e)

        step_state.__doc__ = wr.emr.get_step_state.__doc__.replace('import awswrangler as wr',
                                                                     'from dataplate.client import DataPlate\n    >>> dataplate = DataPlate()')
        step_state.__doc__ = step_state.__doc__.replace('wr.emr.get_step_state', 'dataplate.emr.step_state')

        def list_clusters(self, n=0, cluster_states=['STARTING','BOOTSTRAPPING','RUNNING','WAITING','TERMINATING']):
            """Return a pandas data frame of the EMR clusters.
            Args:
                n (int): The number of clusters to return or all clusters if 0 (default: 0)
                cluster_states (list of strings) - Optional: The cluster states to filter by (default: ['STARTING','BOOTSTRAPPING','RUNNING','WAITING','TERMINATING'])
                                                   Options are: STARTING | BOOTSTRAPPING | RUNNING | WAITING | TERMINATING | TERMINATED | TERMINATED_WITH_ERRORS
            """
            try:
                params = {}
                if n:
                    params['n'] = n
                if cluster_states and isinstance(cluster_states,list):
                    params['cluster_states'] = json.dumps(cluster_states)
                else:
                    raise Error('cluster_states must be defined as list of strings')

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}

                try:
                    logging.info('sending request...')

                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.02'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.02, please update your DataPlate server')
                        return

                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_listClusters'.format(self._dataplate.base_url), params=params, data="",
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('analysing clusters...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    # logging.info(str(r.text))
                    if r.text:
                        rJson = json.loads(r.text)
                        logging.info('list clusters finished successfully.')
                        try:
                            df = pd.read_json(rJson)
                            return df
                        except Exception as e:
                            logging.info('No clusters found.')
                    else:
                        logging.exception('Could not find proper output, please check your parameters')
                    # return r.text

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('list_clusters , ' + str(e))
                raise Error(e)



        def list_steps(self, n=0, cluster_id=None, step_states=['PENDING', 'CANCEL_PENDING', 'RUNNING', 'COMPLETED', 'CANCELLED', 'FAILED', 'INTERRUPTED']):
            """Return a pandas data frame of the EMR cluster steps.
            Args:
                n (int): The number of steps to return or all steps if 0 (default: 0)
                cluster_id (string): cluster Id to check steps in (required)
                step_states (list of strings) - Optional: The step states to filter by (default: ['PENDING', 'CANCEL_PENDING', 'RUNNING', 'COMPLETED', 'CANCELLED', 'FAILED', 'INTERRUPTED'])
                                                   Options are: PENDING | CANCEL_PENDING | RUNNING | COMPLETED | CANCELLED | FAILED | INTERRUPTED
            """
            try:
                params = {}
                if n:
                    params['n'] = n
                if step_states and isinstance(step_states,list):
                    params['step_states'] = json.dumps(step_states)
                else:
                    raise Error('step_states must be defined as list of strings')

                if not cluster_id:
                    raise Error('cluster_id must be defined - use dataplate.emr.list_clusters() to get the list of active clusters and their IDs')

                params['cluster_id'] = cluster_id

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}

                try:
                    logging.info('sending request...')

                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.02'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.02, please update your DataPlate server')
                        return

                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_listSteps'.format(self._dataplate.base_url), params=params, data="",
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('analysing steps...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    # logging.info(str(r.text))
                    if r.text:
                        rJson = json.loads(r.text)
                        logging.info('list steps finished successfully.')
                        try:
                            df = pd.read_json(rJson)
                            return df
                        except Exception as e:
                            logging.info('No steps found.')
                    else:
                        logging.exception('Could not find proper output, please check your parameters')
                    # return r.text

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('list_steps , ' + str(e))
                raise Error(e)



        def list_instance_fleets(self, n=0, cluster_id=None, fleet_states=['PROVISIONING','BOOTSTRAPPING','RUNNING','RESIZING','SUSPENDED','TERMINATING']):
            """Return a pandas data frame of the EMR cluster instance fleets.
            Args:
                n (int): The number of fleets to return or all fleets if 0 (default: 0)
                cluster_id (string): cluster Id to check fleets in (required)
                fleet_states (list of strings) - Optional: The fleet states to filter by (default: ['PROVISIONING','BOOTSTRAPPING','RUNNING','RESIZING','SUSPENDED','TERMINATING'])
                                                   Options are: 'PROVISIONING','BOOTSTRAPPING','RUNNING','RESIZING','SUSPENDED','TERMINATING','TERMINATED'
            """
            try:
                params = {}
                if n:
                    params['n'] = n
                if fleet_states and isinstance(fleet_states,list):
                    params['fleet_states'] = json.dumps(fleet_states)
                else:
                    raise Error('fleet_states must be defined as list of strings')

                if not cluster_id:
                    raise Error('cluster_id must be defined - use dataplate.emr.list_clusters() to get the list of active clusters and their IDs')

                params['cluster_id'] = cluster_id

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}

                try:
                    logging.info('sending request...')

                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.02'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.02, please update your DataPlate server')
                        return

                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_listInstanceFleets'.format(self._dataplate.base_url), params=params, data="",
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('analysing fleets...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    # logging.info(str(r.text))
                    if r.text:
                        rJson = json.loads(r.text)
                        logging.info('list fleets finished successfully.')
                        try:
                            df = pd.read_json(rJson)
                            return df
                        except Exception as e:
                            logging.info('No steps found.')
                    else:
                        logging.exception('Could not find proper output, please check your parameters')
                    # return r.text

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('list_instance_fleets , ' + str(e))
                raise Error(e)



        def list_instance_groups(self, n=0, cluster_id=None, group_states=['PROVISIONING','BOOTSTRAPPING','RUNNING','RECONFIGURING','RESIZING','SUSPENDED','TERMINATING','ARRESTED','SHUTTING_DOWN']):
            """Return a pandas data frame of the EMR cluster instance groups.
            Args:
                n (int): The number of groups to return or all groups if 0 (default: 0)
                cluster_id (string): cluster Id to check groups in (required)
                group_states (list of strings) - Optional: The groups states to filter by (default: [''PROVISIONING','BOOTSTRAPPING','RUNNING','RECONFIGURING','RESIZING','SUSPENDED','TERMINATING','ARRESTED','SHUTTING_DOWN'])
                                                   Options are: 'PROVISIONING','BOOTSTRAPPING','RUNNING','RECONFIGURING','RESIZING','SUSPENDED','TERMINATING','TERMINATED','ARRESTED','SHUTTING_DOWN','ENDED'
            """
            try:
                params = {}
                if n:
                    params['n'] = n
                if group_states and isinstance(group_states,list):
                    params['group_states'] = json.dumps(group_states)
                else:
                    raise Error('group_states must be defined as list of strings')

                if not cluster_id:
                    raise Error('cluster_id must be defined - use dataplate.emr.list_clusters() to get the list of active clusters and their IDs')

                params['cluster_id'] = cluster_id

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}

                try:
                    logging.info('sending request...')

                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.02'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.02, please update your DataPlate server')
                        return

                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_listInstanceGroups'.format(self._dataplate.base_url), params=params, data="",
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('analysing groups...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    # logging.info(str(r.text))
                    if r.text:
                        rJson = json.loads(r.text)
                        logging.info('list groups finished successfully.')
                        try:
                            df = pd.read_json(rJson)
                            return df
                        except Exception as e:
                            logging.info('No steps found.')
                    else:
                        logging.exception('Could not find proper output, please check your parameters')
                    # return r.text

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('list_instance_groups , ' + str(e))
                raise Error(e)


        def modify_fleet_instance(self, cluster_id=None, instance_fleet_id=None, target_ondemand_capacity=1, target_spot_capacity=0):
            """Modifies the target On-Demand and target Spot capacities for the instance fleet with the specified InstanceFleetID within the cluster specified using cluster_id. The call either succeeds or fails atomically..
            Args:
                cluster_id (string): cluster Id to check groups in (required)
                instance_fleet_id (string): instance_fleet id (required)
                target_ondemand_capacity (int): new onDemand instances capacity for the fleet (default: 1)
                target_spot_capacity (int): new Spot instances capacity for the fleet (default: 0)
            """
            try:
                params = {}

                if not cluster_id:
                    raise Error('cluster_id must be defined - use dataplate.emr.list_clusters() to get the list of active clusters and their IDs')
                params['cluster_id'] = cluster_id

                if not instance_fleet_id:
                    raise Error('instance_fleet_id must be defined - use dataplate.emr.list_instance_fleets() to get the list of active instance fleets and their IDs')
                params['instance_fleet_id'] = instance_fleet_id

                if target_ondemand_capacity == 0 and target_spot_capacity == 0:
                    raise Error(
                        'at least one of instance_target_ondemand_capacity and target_spot_capacity must be larger than 0')
                params['target_ondemand_capacity'] = target_ondemand_capacity
                params['target_spot_capacity'] = target_spot_capacity

                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}

                try:
                    logging.info('sending request...')

                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.02'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.02, please update your DataPlate server')
                        return

                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_modifyFleetInstance'.format(self._dataplate.base_url), params=params, data="",
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('analysing status...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    # logging.info(str(r.text))
                    if r.text:
                        logging.info(r.text)
                    else:
                        logging.exception('Could not find proper output, please check your parameters')
                    # return r.text

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('modify_fleet_instance , ' + str(e))
                raise Error(e)



        def describe_cluster(self, cluster_id=None):
            """Describe EMR cluster using cluster_id.
            Args:
                cluster_id (string): cluster Id to get description for (required)
            """
            try:
                params = {}

                if not cluster_id:
                    raise Error('cluster_id must be defined - use dataplate.emr.list_clusters() to get the list of active clusters and their IDs')
                params['cluster_id'] = cluster_id


                headers = {'X-Access-Key': self._dataplate.access_key}

                try:
                    logging.info('sending request...')

                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.02'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.02, please update your DataPlate server')
                        return

                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_describeCluster'.format(self._dataplate.base_url), params=params, data="",
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('analysing status...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    # logging.info(str(r.text))
                    if r.text:
                        logging.info('describe cluster finished successfully.')
                        return r.text
                        # try:
                        #     rJson = json.loads(json.dumps(r.text))
                        #     # logging.info(str(r.text))
                        #     return rJson
                        # except Exception as e:
                        #     logging.exception('Failed to parse result')
                    else:
                        logging.exception('Could not find proper output, please check your parameters')
                    # return r.text

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('describe_cluster , ' + str(e))
                raise Error(e)


        def step_log(self, cluster_id=None, step_id=None, errors=False):
            """Output EMR step log using cluster_id and step_id.
            Args:
                cluster_id (string): cluster Id to get log for (required)
                step_id (string): step Id to get log for (required)
                errors (bool): get only error log or output log (default:False - get output log)
            return:
                dataframe of log-lines
            """
            try:
                params = {}

                if not cluster_id:
                    raise Error('cluster_id must be defined - use dataplate.emr.list_clusters() to get the list of active clusters and their IDs')
                params['cluster_id'] = cluster_id

                if not step_id:
                    raise Error('step_id must be defined - use dataplate.emr.list_steps() to get the list of active steps per cluster_id and their IDs')
                params['step_id'] = step_id

                params['errors'] = errors


                headers = {'X-Access-Key': self._dataplate.access_key, 'Content-Type': 'application/json'}

                try:
                    logging.info('sending request...')

                    # backword compatability
                    res = self._dataplate.session.get('{}/version'.format(self._dataplate.base_url))
                    is_new_enough = res.text[res.text.index('VersionNumber:') + len('VersionNumber:'):] >= '1.28.02'
                    if not is_new_enough:
                        logging.exception(
                            'This API requires server version >= 1.28.02, please update your DataPlate server')
                        return

                    r = self._dataplate.session.post( \
                        '{}/api/aws/EMR_outputStepLog'.format(self._dataplate.base_url), params=params, data="",
                        headers=headers, stream=True, allow_redirects=False)

                    if r.status_code != 200:
                        if r.status_code == 302:
                            raise Error(
                                'Bad Access Key! Get your access key at: {}'.format(
                                    self._dataplate.base_url))
                        if r.status_code == 206:
                            logging.info('analysing status...')
                            time.sleep(5)
                        raise Error(
                            'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                                format(r.status_code, r.text))

                    logging.info('Parsing response')
                    # logging.info(str(r.text))
                    if r.text:
                        logging.info('output log received successfully.')
                        return pd.DataFrame(r.text.split('\n'),columns=['log-line'])
                        # try:
                        #     rJson = json.loads(json.dumps(r.text))
                        #     # logging.info(str(r.text))
                        #     return rJson
                        # except Exception as e:
                        #     logging.exception('Failed to parse result')
                    else:
                        logging.exception('Could not find proper output, please check your parameters')
                    # return r.text

                except (requests.exceptions.ConnectionError,
                        requests.exceptions.ReadTimeout) as e:
                    logging.exception('Got ConnectionError/ReadTimeout exception.')
                    raise Error(e)

            except Exception as e:
                logging.exception('emr_step_log , ' + str(e))
                raise Error(e)