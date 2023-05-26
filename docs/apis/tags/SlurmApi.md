<a id="__pageTop"></a>
# slurmrestapi.apis.tags.slurm_api.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurm_v0038_cancel_job**](#slurm_v0038_cancel_job) | **delete** /slurm/v0.0.38/job/{job_id} | cancel or signal job
[**slurm_v0038_diag**](#slurm_v0038_diag) | **get** /slurm/v0.0.38/diag | get diagnostics
[**slurm_v0038_get_job**](#slurm_v0038_get_job) | **get** /slurm/v0.0.38/job/{job_id} | get job info
[**slurm_v0038_get_jobs**](#slurm_v0038_get_jobs) | **get** /slurm/v0.0.38/jobs | get list of jobs
[**slurm_v0038_get_node**](#slurm_v0038_get_node) | **get** /slurm/v0.0.38/node/{node_name} | get node info
[**slurm_v0038_get_nodes**](#slurm_v0038_get_nodes) | **get** /slurm/v0.0.38/nodes | get all node info
[**slurm_v0038_get_partition**](#slurm_v0038_get_partition) | **get** /slurm/v0.0.38/partition/{partition_name} | get partition info
[**slurm_v0038_get_partitions**](#slurm_v0038_get_partitions) | **get** /slurm/v0.0.38/partitions | get all partition info
[**slurm_v0038_get_reservation**](#slurm_v0038_get_reservation) | **get** /slurm/v0.0.38/reservation/{reservation_name} | get reservation info
[**slurm_v0038_get_reservations**](#slurm_v0038_get_reservations) | **get** /slurm/v0.0.38/reservations | get all reservation info
[**slurm_v0038_ping**](#slurm_v0038_ping) | **get** /slurm/v0.0.38/ping | ping test
[**slurm_v0038_slurmctld_get_licenses**](#slurm_v0038_slurmctld_get_licenses) | **get** /slurm/v0.0.38/licenses | get all Slurm tracked license info
[**slurm_v0038_submit_job**](#slurm_v0038_submit_job) | **post** /slurm/v0.0.38/job/submit | submit new job
[**slurm_v0038_update_job**](#slurm_v0038_update_job) | **post** /slurm/v0.0.38/job/{job_id} | update job
[**slurmdb_v0038_add_clusters**](#slurmdb_v0038_add_clusters) | **post** /slurmdb/v0.0.38/clusters | Add clusters
[**slurmdb_v0038_add_wckeys**](#slurmdb_v0038_add_wckeys) | **post** /slurmdb/v0.0.38/wckeys | Add wckeys
[**slurmdb_v0038_delete_account**](#slurmdb_v0038_delete_account) | **delete** /slurmdb/v0.0.38/account/{account_name} | Delete account
[**slurmdb_v0038_delete_association**](#slurmdb_v0038_delete_association) | **delete** /slurmdb/v0.0.38/association | Delete association
[**slurmdb_v0038_delete_associations**](#slurmdb_v0038_delete_associations) | **delete** /slurmdb/v0.0.38/associations | Delete associations
[**slurmdb_v0038_delete_cluster**](#slurmdb_v0038_delete_cluster) | **delete** /slurmdb/v0.0.38/cluster/{cluster_name} | Delete cluster
[**slurmdb_v0038_delete_qos**](#slurmdb_v0038_delete_qos) | **delete** /slurmdb/v0.0.38/qos/{qos_name} | Delete QOS
[**slurmdb_v0038_delete_user**](#slurmdb_v0038_delete_user) | **delete** /slurmdb/v0.0.38/user/{user_name} | Delete user
[**slurmdb_v0038_delete_wckey**](#slurmdb_v0038_delete_wckey) | **delete** /slurmdb/v0.0.38/wckey/{wckey} | Delete wckey
[**slurmdb_v0038_diag**](#slurmdb_v0038_diag) | **get** /slurmdb/v0.0.38/diag | Get slurmdb diagnostics
[**slurmdb_v0038_get_account**](#slurmdb_v0038_get_account) | **get** /slurmdb/v0.0.38/account/{account_name} | Get account info
[**slurmdb_v0038_get_accounts**](#slurmdb_v0038_get_accounts) | **get** /slurmdb/v0.0.38/accounts | Get account list
[**slurmdb_v0038_get_association**](#slurmdb_v0038_get_association) | **get** /slurmdb/v0.0.38/association | Get association info
[**slurmdb_v0038_get_associations**](#slurmdb_v0038_get_associations) | **get** /slurmdb/v0.0.38/associations | Get association list
[**slurmdb_v0038_get_cluster**](#slurmdb_v0038_get_cluster) | **get** /slurmdb/v0.0.38/cluster/{cluster_name} | Get cluster info
[**slurmdb_v0038_get_clusters**](#slurmdb_v0038_get_clusters) | **get** /slurmdb/v0.0.38/clusters | Get cluster list
[**slurmdb_v0038_get_config**](#slurmdb_v0038_get_config) | **get** /slurmdb/v0.0.38/config | Dump all configuration information
[**slurmdb_v0038_get_job**](#slurmdb_v0038_get_job) | **get** /slurmdb/v0.0.38/job/{job_id} | Get job info
[**slurmdb_v0038_get_jobs**](#slurmdb_v0038_get_jobs) | **get** /slurmdb/v0.0.38/jobs | Get job list
[**slurmdb_v0038_get_qos**](#slurmdb_v0038_get_qos) | **get** /slurmdb/v0.0.38/qos | Get QOS list
[**slurmdb_v0038_get_single_qos**](#slurmdb_v0038_get_single_qos) | **get** /slurmdb/v0.0.38/qos/{qos_name} | Get QOS info
[**slurmdb_v0038_get_tres**](#slurmdb_v0038_get_tres) | **get** /slurmdb/v0.0.38/tres | Get TRES info
[**slurmdb_v0038_get_user**](#slurmdb_v0038_get_user) | **get** /slurmdb/v0.0.38/user/{user_name} | Get user info
[**slurmdb_v0038_get_users**](#slurmdb_v0038_get_users) | **get** /slurmdb/v0.0.38/users | Get user list
[**slurmdb_v0038_get_wckey**](#slurmdb_v0038_get_wckey) | **get** /slurmdb/v0.0.38/wckey/{wckey} | Get wckey info
[**slurmdb_v0038_get_wckeys**](#slurmdb_v0038_get_wckeys) | **get** /slurmdb/v0.0.38/wckeys | Get wckey list
[**slurmdb_v0038_set_config**](#slurmdb_v0038_set_config) | **post** /slurmdb/v0.0.38/config | Load all configuration information
[**slurmdb_v0038_update_account**](#slurmdb_v0038_update_account) | **post** /slurmdb/v0.0.38/accounts | Update accounts
[**slurmdb_v0038_update_associations**](#slurmdb_v0038_update_associations) | **post** /slurmdb/v0.0.38/associations | Set associations info
[**slurmdb_v0038_update_qos**](#slurmdb_v0038_update_qos) | **post** /slurmdb/v0.0.38/qos | Set QOS info
[**slurmdb_v0038_update_tres**](#slurmdb_v0038_update_tres) | **post** /slurmdb/v0.0.38/tres | Set TRES info
[**slurmdb_v0038_update_users**](#slurmdb_v0038_update_users) | **post** /slurmdb/v0.0.38/users | Update user

# **slurm_v0038_cancel_job**
<a id="slurm_v0038_cancel_job"></a>
> slurm_v0038_cancel_job(job_id)

cancel or signal job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_signal import V0038Signal
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    query_params = {
    }
    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0038_cancel_job(
            path_params=path_params,
            query_params=query_params,
        )
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_cancel_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'job_id': "job_id_example",
    }
    query_params = {
        'signal': V0038Signal("HUP"),
    }
    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0038_cancel_job(
            path_params=path_params,
            query_params=query_params,
        )
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_cancel_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
signal | SignalSchema | | optional


# SignalSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Signal**](../../models/V0038Signal.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | JobIdSchema | | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_cancel_job.ApiResponseFor200) | job cancelled or sent signal
500 | [ApiResponseFor500](#slurm_v0038_cancel_job.ApiResponseFor500) | job not found

#### slurm_v0038_cancel_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slurm_v0038_cancel_job.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_diag**
<a id="slurm_v0038_diag"></a>
> V0038Diag slurm_v0038_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_errors import V0038Errors
from slurmrestapi.model.v0038_diag import V0038Diag
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get diagnostics
        api_response = api_instance.slurm_v0038_diag()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_diag: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_diag.ApiResponseFor200) | diagnostic results
default | [ApiResponseForDefault](#slurm_v0038_diag.ApiResponseForDefault) | unable to request ping test

#### slurm_v0038_diag.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Diag**](../../models/V0038Diag.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Diag**](../../models/V0038Diag.md) |  | 


#### slurm_v0038_diag.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_get_job**
<a id="slurm_v0038_get_job"></a>
> V0038JobsResponse slurm_v0038_get_job(job_id)

get job info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_jobs_response import V0038JobsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    try:
        # get job info
        api_response = api_instance.slurm_v0038_get_job(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | JobIdSchema | | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_get_job.ApiResponseFor200) | job(s) information
default | [ApiResponseForDefault](#slurm_v0038_get_job.ApiResponseForDefault) | job matching JobId not found

#### slurm_v0038_get_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobsResponse**](../../models/V0038JobsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobsResponse**](../../models/V0038JobsResponse.md) |  | 


#### slurm_v0038_get_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_get_jobs**
<a id="slurm_v0038_get_jobs"></a>
> V0038JobsResponse slurm_v0038_get_jobs()

get list of jobs

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_jobs_response import V0038JobsResponse
from slurmrestapi.model.v0038_errors import V0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'update_time': 1,
    }
    try:
        # get list of jobs
        api_response = api_instance.slurm_v0038_get_jobs(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_jobs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
update_time | UpdateTimeSchema | | optional


# UpdateTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_get_jobs.ApiResponseFor200) | job(s) information
default | [ApiResponseForDefault](#slurm_v0038_get_jobs.ApiResponseForDefault) | job not found

#### slurm_v0038_get_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobsResponse**](../../models/V0038JobsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobsResponse**](../../models/V0038JobsResponse.md) |  | 


#### slurm_v0038_get_jobs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_get_node**
<a id="slurm_v0038_get_node"></a>
> V0038NodesResponse slurm_v0038_get_node(node_name)

get node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_errors import V0038Errors
from slurmrestapi.model.v0038_nodes_response import V0038NodesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_name': "node_name_example",
    }
    try:
        # get node info
        api_response = api_instance.slurm_v0038_get_node(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_node: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
node_name | NodeNameSchema | | 

# NodeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_get_node.ApiResponseFor200) | node information
default | [ApiResponseForDefault](#slurm_v0038_get_node.ApiResponseForDefault) | node not found

#### slurm_v0038_get_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038NodesResponse**](../../models/V0038NodesResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038NodesResponse**](../../models/V0038NodesResponse.md) |  | 


#### slurm_v0038_get_node.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_get_nodes**
<a id="slurm_v0038_get_nodes"></a>
> V0038NodesResponse slurm_v0038_get_nodes()

get all node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_errors import V0038Errors
from slurmrestapi.model.v0038_nodes_response import V0038NodesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'update_time': 1,
    }
    try:
        # get all node info
        api_response = api_instance.slurm_v0038_get_nodes(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_nodes: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
update_time | UpdateTimeSchema | | optional


# UpdateTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_get_nodes.ApiResponseFor200) | node information
default | [ApiResponseForDefault](#slurm_v0038_get_nodes.ApiResponseForDefault) | no nodes in cluster

#### slurm_v0038_get_nodes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038NodesResponse**](../../models/V0038NodesResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038NodesResponse**](../../models/V0038NodesResponse.md) |  | 


#### slurm_v0038_get_nodes.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_get_partition**
<a id="slurm_v0038_get_partition"></a>
> V0038PartitionsResponse slurm_v0038_get_partition(partition_name)

get partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_errors import V0038Errors
from slurmrestapi.model.v0038_partitions_response import V0038PartitionsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'partition_name': "partition_name_example",
    }
    query_params = {
    }
    try:
        # get partition info
        api_response = api_instance.slurm_v0038_get_partition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_partition: %s\n" % e)

    # example passing only optional values
    path_params = {
        'partition_name': "partition_name_example",
    }
    query_params = {
        'update_time': 1,
    }
    try:
        # get partition info
        api_response = api_instance.slurm_v0038_get_partition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_partition: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
update_time | UpdateTimeSchema | | optional


# UpdateTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
partition_name | PartitionNameSchema | | 

# PartitionNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_get_partition.ApiResponseFor200) | partition information
default | [ApiResponseForDefault](#slurm_v0038_get_partition.ApiResponseForDefault) | no partitions found

#### slurm_v0038_get_partition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038PartitionsResponse**](../../models/V0038PartitionsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038PartitionsResponse**](../../models/V0038PartitionsResponse.md) |  | 


#### slurm_v0038_get_partition.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_get_partitions**
<a id="slurm_v0038_get_partitions"></a>
> V0038PartitionsResponse slurm_v0038_get_partitions()

get all partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_errors import V0038Errors
from slurmrestapi.model.v0038_partitions_response import V0038PartitionsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'update_time': 1,
    }
    try:
        # get all partition info
        api_response = api_instance.slurm_v0038_get_partitions(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_partitions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
update_time | UpdateTimeSchema | | optional


# UpdateTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_get_partitions.ApiResponseFor200) | partition information
default | [ApiResponseForDefault](#slurm_v0038_get_partitions.ApiResponseForDefault) | no partitions found

#### slurm_v0038_get_partitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038PartitionsResponse**](../../models/V0038PartitionsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038PartitionsResponse**](../../models/V0038PartitionsResponse.md) |  | 


#### slurm_v0038_get_partitions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_get_reservation**
<a id="slurm_v0038_get_reservation"></a>
> V0038ReservationsResponse slurm_v0038_get_reservation(reservation_name)

get reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_reservations_response import V0038ReservationsResponse
from slurmrestapi.model.v0038_errors import V0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'reservation_name': "reservation_name_example",
    }
    query_params = {
    }
    try:
        # get reservation info
        api_response = api_instance.slurm_v0038_get_reservation(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_reservation: %s\n" % e)

    # example passing only optional values
    path_params = {
        'reservation_name': "reservation_name_example",
    }
    query_params = {
        'update_time': 1,
    }
    try:
        # get reservation info
        api_response = api_instance.slurm_v0038_get_reservation(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_reservation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
update_time | UpdateTimeSchema | | optional


# UpdateTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reservation_name | ReservationNameSchema | | 

# ReservationNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_get_reservation.ApiResponseFor200) | reservation information
default | [ApiResponseForDefault](#slurm_v0038_get_reservation.ApiResponseForDefault) | no reservations found

#### slurm_v0038_get_reservation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038ReservationsResponse**](../../models/V0038ReservationsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038ReservationsResponse**](../../models/V0038ReservationsResponse.md) |  | 


#### slurm_v0038_get_reservation.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_get_reservations**
<a id="slurm_v0038_get_reservations"></a>
> V0038ReservationsResponse slurm_v0038_get_reservations()

get all reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_reservations_response import V0038ReservationsResponse
from slurmrestapi.model.v0038_errors import V0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'update_time': 1,
    }
    try:
        # get all reservation info
        api_response = api_instance.slurm_v0038_get_reservations(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_reservations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
update_time | UpdateTimeSchema | | optional


# UpdateTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_get_reservations.ApiResponseFor200) | reservation information
default | [ApiResponseForDefault](#slurm_v0038_get_reservations.ApiResponseForDefault) | no reservations found

#### slurm_v0038_get_reservations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038ReservationsResponse**](../../models/V0038ReservationsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038ReservationsResponse**](../../models/V0038ReservationsResponse.md) |  | 


#### slurm_v0038_get_reservations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_ping**
<a id="slurm_v0038_ping"></a>
> V0038Pings slurm_v0038_ping()

ping test

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_errors import V0038Errors
from slurmrestapi.model.v0038_pings import V0038Pings
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # ping test
        api_response = api_instance.slurm_v0038_ping()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_ping: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_ping.ApiResponseFor200) | results of ping test
default | [ApiResponseForDefault](#slurm_v0038_ping.ApiResponseForDefault) | unable to request ping test

#### slurm_v0038_ping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Pings**](../../models/V0038Pings.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Pings**](../../models/V0038Pings.md) |  | 


#### slurm_v0038_ping.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_slurmctld_get_licenses**
<a id="slurm_v0038_slurmctld_get_licenses"></a>
> V0038Licenses slurm_v0038_slurmctld_get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_licenses import V0038Licenses
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0038_slurmctld_get_licenses()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_slurmctld_get_licenses: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_slurmctld_get_licenses.ApiResponseFor200) | results of get all licenses
default | [ApiResponseForDefault](#slurm_v0038_slurmctld_get_licenses.ApiResponseForDefault) | unable to request licenses

#### slurm_v0038_slurmctld_get_licenses.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Licenses**](../../models/V0038Licenses.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Licenses**](../../models/V0038Licenses.md) |  | 


#### slurm_v0038_slurmctld_get_licenses.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_submit_job**
<a id="slurm_v0038_submit_job"></a>
> V0038JobSubmissionResponse slurm_v0038_submit_job(v0038_job_submission)

submit new job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_errors import V0038Errors
from slurmrestapi.model.v0038_job_submission_response import V0038JobSubmissionResponse
from slurmrestapi.model.v0038_job_submission import V0038JobSubmission
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = V0038JobSubmission(None)
    try:
        # submit new job
        api_response = api_instance.slurm_v0038_submit_job(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_submit_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobSubmission**](../../models/V0038JobSubmission.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobSubmission**](../../models/V0038JobSubmission.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_submit_job.ApiResponseFor200) | job submitted
default | [ApiResponseForDefault](#slurm_v0038_submit_job.ApiResponseForDefault) | job rejected

#### slurm_v0038_submit_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobSubmissionResponse**](../../models/V0038JobSubmissionResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobSubmissionResponse**](../../models/V0038JobSubmissionResponse.md) |  | 


#### slurm_v0038_submit_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038Errors**](../../models/V0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0038_update_job**
<a id="slurm_v0038_update_job"></a>
> slurm_v0038_update_job(job_idv0038_job_properties)

update job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0038_job_properties import V0038JobProperties
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    body = V0038JobProperties(
        account="account_example",
        account_gather_frequency="account_gather_frequency_example",
        argv=[
            "argv_example"
        ],
        array="array_example",
        batch_features="batch_features_example",
        begin_time=1,
        burst_buffer="burst_buffer_example",
        cluster_constraint="cluster_constraint_example",
        comment="comment_example",
        constraints="constraints_example",
        container="container_example",
        core_specification=1,
        cores_per_socket=1,
        cpu_binding="cpu_binding_example",
        cpu_binding_hint="cpu_binding_hint_example",
        cpu_frequency="cpu_frequency_example",
        cpus_per_gpu="cpus_per_gpu_example",
        cpus_per_task=1,
        current_working_directory="current_working_directory_example",
        deadline="deadline_example",
        delay_boot=1,
        dependency="dependency_example",
        distribution="distribution_example",
        environment=dict(),
        exclusive="user",
        get_user_environment=True,
        gres="gres_example",
        gres_flags="disable-binding",
        gpu_binding="gpu_binding_example",
        gpu_frequency="gpu_frequency_example",
        gpus="gpus_example",
        gpus_per_node="gpus_per_node_example",
        gpus_per_socket="gpus_per_socket_example",
        gpus_per_task="gpus_per_task_example",
        hold=True,
        kill_on_invalid_dependency=True,
        licenses="licenses_example",
        mail_type="mail_type_example",
        mail_user="mail_user_example",
        mcs_label="mcs_label_example",
        memory_binding="memory_binding_example",
        memory_per_cpu=1,
        memory_per_gpu=1,
        memory_per_node=1,
        minimum_cpus_per_node=1,
        minimum_nodes=True,
        name="name_example",
        nice=1,
        no_kill=True,
        nodes=[
            1
        ],
        open_mode="append",
        oversubscribe=False,
        partition="partition_example",
        prefer="prefer_example",
        priority="priority_example",
        qos="qos_example",
        requeue=True,
        reservation="reservation_example",
        signal="sig_num",
        sockets_per_node=1,
        spread_job=True,
        standard_error="standard_error_example",
        standard_input="standard_input_example",
        standard_output="standard_output_example",
        tasks=1,
        tasks_per_core=1,
        tasks_per_node=1,
        tasks_per_socket=1,
        thread_specification=1,
        threads_per_core=1,
        time_limit=1,
        time_minimum=1,
        wait_all_nodes=True,
        wckey="wckey_example",
    )
    try:
        # update job
        api_response = api_instance.slurm_v0038_update_job(
            path_params=path_params,
            body=body,
        )
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0038_update_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobProperties**](../../models/V0038JobProperties.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0038JobProperties**](../../models/V0038JobProperties.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | JobIdSchema | | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0038_update_job.ApiResponseFor200) | job information
500 | [ApiResponseFor500](#slurm_v0038_update_job.ApiResponseFor500) | job not found

#### slurm_v0038_update_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slurm_v0038_update_job.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_add_clusters**
<a id="slurmdb_v0038_add_clusters"></a>
> Dbv0038ResponseClusterAdd slurmdb_v0038_add_clusters(dbv0038_clusters_properties)

Add clusters

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_clusters_properties import Dbv0038ClustersProperties
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_response_cluster_add import Dbv0038ResponseClusterAdd
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0038ClustersProperties(
        clusters=Dbv0038ClusterInfo(
            controller=dict(
                host="host_example",
                port=1,
            ),
            flags=[
                "flags_example"
            ],
            name="name_example",
            nodes="nodes_example",
            select_plugin="select_plugin_example",
            associations=dict(
                root=Dbv0038AssociationShortInfo(
                    account="account_example",
                    cluster="cluster_example",
                    partition="partition_example",
                    user="user_example",
                ),
            ),
            rpc_version=1,
            tres=[
                Dbv0038ResponseTres(
                    meta=Dbv0038Meta(
                        plugin=dict(
                            type="type_example",
                            name="name_example",
                        ),
                        slurm=dict(
                            version=dict(
                                major="major_example",
                                micro="micro_example",
                                minor="minor_example",
                            ),
                            release="release_example",
                        ),
                    ),
                    errors=[
                        Dbv0038Error(
                            error_number=1,
                            error="error_example",
                            source="source_example",
                            description="description_example",
                        )
                    ],
                )
            ],
        ),
    )
    try:
        # Add clusters
        api_response = api_instance.slurmdb_v0038_add_clusters(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_add_clusters: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ClustersProperties**](../../models/Dbv0038ClustersProperties.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ClustersProperties**](../../models/Dbv0038ClustersProperties.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_add_clusters.ApiResponseFor200) | List of clusters
default | [ApiResponseForDefault](#slurmdb_v0038_add_clusters.ApiResponseForDefault) | Unable to add cluster

#### slurmdb_v0038_add_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseClusterAdd**](../../models/Dbv0038ResponseClusterAdd.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseClusterAdd**](../../models/Dbv0038ResponseClusterAdd.md) |  | 


#### slurmdb_v0038_add_clusters.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_add_wckeys**
<a id="slurmdb_v0038_add_wckeys"></a>
> Dbv0038ResponseWckeyAdd slurmdb_v0038_add_wckeys()

Add wckeys

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_response_wckey_add import Dbv0038ResponseWckeyAdd
from slurmrestapi.model.dbv0038_wckey_info import Dbv0038WckeyInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    body = Dbv0038WckeyInfo(
        meta=Dbv0038Meta(
            plugin=dict(
                type="type_example",
                name="name_example",
            ),
            slurm=dict(
                version=dict(
                    major="major_example",
                    micro="micro_example",
                    minor="minor_example",
                ),
                release="release_example",
            ),
        ),
        errors=[
            Dbv0038Error(
                error_number=1,
                error="error_example",
                source="source_example",
                description="description_example",
            )
        ],
        wckeys=[
            Dbv0038Wckey(
                cluster="cluster_example",
                id=1,
                name="name_example",
                user="user_example",
                flags=[
                    "flags_example"
                ],
                accounting=[
                    Dbv0038Accounting(
                        allocated=1,
                        id=1,
                        start=1,
                        tres=Dbv0038TresList([
                            dict(
                                type="type_example",
                                name="name_example",
                                id=1,
                                count=1,
                            )
                        ]),
                    )
                ],
            )
        ],
    )
    try:
        # Add wckeys
        api_response = api_instance.slurmdb_v0038_add_wckeys(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_add_wckeys: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038WckeyInfo**](../../models/Dbv0038WckeyInfo.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038WckeyInfo**](../../models/Dbv0038WckeyInfo.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_add_wckeys.ApiResponseFor200) | List of wckeys
default | [ApiResponseForDefault](#slurmdb_v0038_add_wckeys.ApiResponseForDefault) | Unable to add wckey

#### slurmdb_v0038_add_wckeys.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseWckeyAdd**](../../models/Dbv0038ResponseWckeyAdd.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseWckeyAdd**](../../models/Dbv0038ResponseWckeyAdd.md) |  | 


#### slurmdb_v0038_add_wckeys.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_delete_account**
<a id="slurmdb_v0038_delete_account"></a>
> Dbv0038ResponseAccountDelete slurmdb_v0038_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_response_account_delete import Dbv0038ResponseAccountDelete
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_name': "account_name_example",
    }
    try:
        # Delete account
        api_response = api_instance.slurmdb_v0038_delete_account(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_account: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_name | AccountNameSchema | | 

# AccountNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_delete_account.ApiResponseFor200) | Delete account
default | [ApiResponseForDefault](#slurmdb_v0038_delete_account.ApiResponseForDefault) | Unable to delete account

#### slurmdb_v0038_delete_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseAccountDelete**](../../models/Dbv0038ResponseAccountDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseAccountDelete**](../../models/Dbv0038ResponseAccountDelete.md) |  | 


#### slurmdb_v0038_delete_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_delete_association**
<a id="slurmdb_v0038_delete_association"></a>
> Dbv0038ResponseAssociationsDelete slurmdb_v0038_delete_association()

Delete association

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_response_associations_delete import Dbv0038ResponseAssociationsDelete
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'cluster': "cluster_example",
        'account': "account_example",
        'user': "user_example",
        'partition': "partition_example",
    }
    try:
        # Delete association
        api_response = api_instance.slurmdb_v0038_delete_association(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_association: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cluster | ClusterSchema | | optional
account | AccountSchema | | optional
user | UserSchema | | optional
partition | PartitionSchema | | optional


# ClusterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartitionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_delete_association.ApiResponseFor200) | Delete associations
default | [ApiResponseForDefault](#slurmdb_v0038_delete_association.ApiResponseForDefault) | Association not found or unable to delete association

#### slurmdb_v0038_delete_association.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseAssociationsDelete**](../../models/Dbv0038ResponseAssociationsDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseAssociationsDelete**](../../models/Dbv0038ResponseAssociationsDelete.md) |  | 


#### slurmdb_v0038_delete_association.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_delete_associations**
<a id="slurmdb_v0038_delete_associations"></a>
> Dbv0038ResponseAssociationsDelete slurmdb_v0038_delete_associations()

Delete associations

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_response_associations_delete import Dbv0038ResponseAssociationsDelete
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'cluster': "cluster_example",
        'account': "account_example",
        'user': "user_example",
        'partition': "partition_example",
    }
    try:
        # Delete associations
        api_response = api_instance.slurmdb_v0038_delete_associations(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_associations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cluster | ClusterSchema | | optional
account | AccountSchema | | optional
user | UserSchema | | optional
partition | PartitionSchema | | optional


# ClusterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartitionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_delete_associations.ApiResponseFor200) | Delete associations
default | [ApiResponseForDefault](#slurmdb_v0038_delete_associations.ApiResponseForDefault) | Associations not found or unable to delete association

#### slurmdb_v0038_delete_associations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseAssociationsDelete**](../../models/Dbv0038ResponseAssociationsDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseAssociationsDelete**](../../models/Dbv0038ResponseAssociationsDelete.md) |  | 


#### slurmdb_v0038_delete_associations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_delete_cluster**
<a id="slurmdb_v0038_delete_cluster"></a>
> Dbv0038ResponseClusterDelete slurmdb_v0038_delete_cluster(cluster_name)

Delete cluster

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_response_cluster_delete import Dbv0038ResponseClusterDelete
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'cluster_name': "cluster_name_example",
    }
    try:
        # Delete cluster
        api_response = api_instance.slurmdb_v0038_delete_cluster(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cluster_name | ClusterNameSchema | | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_delete_cluster.ApiResponseFor200) | Delete cluster
default | [ApiResponseForDefault](#slurmdb_v0038_delete_cluster.ApiResponseForDefault) | Cluster not found or unable to delete cluster

#### slurmdb_v0038_delete_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseClusterDelete**](../../models/Dbv0038ResponseClusterDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseClusterDelete**](../../models/Dbv0038ResponseClusterDelete.md) |  | 


#### slurmdb_v0038_delete_cluster.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_delete_qos**
<a id="slurmdb_v0038_delete_qos"></a>
> Dbv0038ResponseQosDelete slurmdb_v0038_delete_qos(qos_name)

Delete QOS

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_response_qos_delete import Dbv0038ResponseQosDelete
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'qos_name': "qos_name_example",
    }
    try:
        # Delete QOS
        api_response = api_instance.slurmdb_v0038_delete_qos(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_qos: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
qos_name | QosNameSchema | | 

# QosNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_delete_qos.ApiResponseFor200) | Delete qos
default | [ApiResponseForDefault](#slurmdb_v0038_delete_qos.ApiResponseForDefault) | Unable to delete QOS

#### slurmdb_v0038_delete_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseQosDelete**](../../models/Dbv0038ResponseQosDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseQosDelete**](../../models/Dbv0038ResponseQosDelete.md) |  | 


#### slurmdb_v0038_delete_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_delete_user**
<a id="slurmdb_v0038_delete_user"></a>
> Dbv0038ResponseUserDelete slurmdb_v0038_delete_user(user_name)

Delete user

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_response_user_delete import Dbv0038ResponseUserDelete
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_name': "user_name_example",
    }
    try:
        # Delete user
        api_response = api_instance.slurmdb_v0038_delete_user(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_name | UserNameSchema | | 

# UserNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_delete_user.ApiResponseFor200) | Delete user
default | [ApiResponseForDefault](#slurmdb_v0038_delete_user.ApiResponseForDefault) | User not found or unable to delete user

#### slurmdb_v0038_delete_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseUserDelete**](../../models/Dbv0038ResponseUserDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseUserDelete**](../../models/Dbv0038ResponseUserDelete.md) |  | 


#### slurmdb_v0038_delete_user.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_delete_wckey**
<a id="slurmdb_v0038_delete_wckey"></a>
> Dbv0038ResponseWckeyDelete slurmdb_v0038_delete_wckey(wckey)

Delete wckey

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_response_wckey_delete import Dbv0038ResponseWckeyDelete
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'wckey': "wckey_example",
    }
    try:
        # Delete wckey
        api_response = api_instance.slurmdb_v0038_delete_wckey(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_delete_wckey: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
wckey | WckeySchema | | 

# WckeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_delete_wckey.ApiResponseFor200) | Delete wckey
default | [ApiResponseForDefault](#slurmdb_v0038_delete_wckey.ApiResponseForDefault) | wckey not found or unable to delete wckey

#### slurmdb_v0038_delete_wckey.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseWckeyDelete**](../../models/Dbv0038ResponseWckeyDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseWckeyDelete**](../../models/Dbv0038ResponseWckeyDelete.md) |  | 


#### slurmdb_v0038_delete_wckey.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_diag**
<a id="slurmdb_v0038_diag"></a>
> Dbv0038Diag slurmdb_v0038_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_diag import Dbv0038Diag
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdb_v0038_diag()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_diag: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_diag.ApiResponseFor200) | Dictionary of statistics
default | [ApiResponseForDefault](#slurmdb_v0038_diag.ApiResponseForDefault) | Unable to query diagnostics

#### slurmdb_v0038_diag.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Diag**](../../models/Dbv0038Diag.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Diag**](../../models/Dbv0038Diag.md) |  | 


#### slurmdb_v0038_diag.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_account**
<a id="slurmdb_v0038_get_account"></a>
> Dbv0038AccountInfo slurmdb_v0038_get_account(account_name)

Get account info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_account_info import Dbv0038AccountInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_name': "account_name_example",
    }
    query_params = {
    }
    try:
        # Get account info
        api_response = api_instance.slurmdb_v0038_get_account(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_account: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_name': "account_name_example",
    }
    query_params = {
        'with_deleted': True,
    }
    try:
        # Get account info
        api_response = api_instance.slurmdb_v0038_get_account(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_account: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
with_deleted | WithDeletedSchema | | optional


# WithDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_name | AccountNameSchema | | 

# AccountNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_account.ApiResponseFor200) | List of accounts
default | [ApiResponseForDefault](#slurmdb_v0038_get_account.ApiResponseForDefault) | Account not found

#### slurmdb_v0038_get_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AccountInfo**](../../models/Dbv0038AccountInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AccountInfo**](../../models/Dbv0038AccountInfo.md) |  | 


#### slurmdb_v0038_get_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_accounts**
<a id="slurmdb_v0038_get_accounts"></a>
> Dbv0038AccountInfo slurmdb_v0038_get_accounts()

Get account list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_account_info import Dbv0038AccountInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'with_deleted': True,
    }
    try:
        # Get account list
        api_response = api_instance.slurmdb_v0038_get_accounts(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_accounts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
with_deleted | WithDeletedSchema | | optional


# WithDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_accounts.ApiResponseFor200) | List of accounts
default | [ApiResponseForDefault](#slurmdb_v0038_get_accounts.ApiResponseForDefault) | Account not found

#### slurmdb_v0038_get_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AccountInfo**](../../models/Dbv0038AccountInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AccountInfo**](../../models/Dbv0038AccountInfo.md) |  | 


#### slurmdb_v0038_get_accounts.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_association**
<a id="slurmdb_v0038_get_association"></a>
> Dbv0038AssociationsInfo slurmdb_v0038_get_association()

Get association info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_associations_info import Dbv0038AssociationsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'cluster': "cluster_example",
        'account': "account_example",
        'user': "user_example",
        'partition': "partition_example",
    }
    try:
        # Get association info
        api_response = api_instance.slurmdb_v0038_get_association(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_association: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cluster | ClusterSchema | | optional
account | AccountSchema | | optional
user | UserSchema | | optional
partition | PartitionSchema | | optional


# ClusterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartitionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_association.ApiResponseFor200) | List of associations
default | [ApiResponseForDefault](#slurmdb_v0038_get_association.ApiResponseForDefault) | Association not found

#### slurmdb_v0038_get_association.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AssociationsInfo**](../../models/Dbv0038AssociationsInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AssociationsInfo**](../../models/Dbv0038AssociationsInfo.md) |  | 


#### slurmdb_v0038_get_association.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_associations**
<a id="slurmdb_v0038_get_associations"></a>
> Dbv0038AssociationsInfo slurmdb_v0038_get_associations()

Get association list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_associations_info import Dbv0038AssociationsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'cluster': "cluster_example",
        'account': "account_example",
        'user': "user_example",
        'partition': "partition_example",
    }
    try:
        # Get association list
        api_response = api_instance.slurmdb_v0038_get_associations(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_associations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cluster | ClusterSchema | | optional
account | AccountSchema | | optional
user | UserSchema | | optional
partition | PartitionSchema | | optional


# ClusterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartitionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_associations.ApiResponseFor200) | List of associations
default | [ApiResponseForDefault](#slurmdb_v0038_get_associations.ApiResponseForDefault) | Association not found

#### slurmdb_v0038_get_associations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AssociationsInfo**](../../models/Dbv0038AssociationsInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AssociationsInfo**](../../models/Dbv0038AssociationsInfo.md) |  | 


#### slurmdb_v0038_get_associations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_cluster**
<a id="slurmdb_v0038_get_cluster"></a>
> Dbv0038ClusterInfo slurmdb_v0038_get_cluster(cluster_name)

Get cluster info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_cluster_info import Dbv0038ClusterInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'cluster_name': "cluster_name_example",
    }
    try:
        # Get cluster info
        api_response = api_instance.slurmdb_v0038_get_cluster(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cluster_name | ClusterNameSchema | | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_cluster.ApiResponseFor200) | Cluster information
default | [ApiResponseForDefault](#slurmdb_v0038_get_cluster.ApiResponseForDefault) | Cluster not found

#### slurmdb_v0038_get_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ClusterInfo**](../../models/Dbv0038ClusterInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ClusterInfo**](../../models/Dbv0038ClusterInfo.md) |  | 


#### slurmdb_v0038_get_cluster.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_clusters**
<a id="slurmdb_v0038_get_clusters"></a>
> Dbv0038ClusterInfo slurmdb_v0038_get_clusters()

Get cluster list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_cluster_info import Dbv0038ClusterInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0038_get_clusters()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_clusters: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_clusters.ApiResponseFor200) | List of clusters
default | [ApiResponseForDefault](#slurmdb_v0038_get_clusters.ApiResponseForDefault) | Cluster not found

#### slurmdb_v0038_get_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ClusterInfo**](../../models/Dbv0038ClusterInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ClusterInfo**](../../models/Dbv0038ClusterInfo.md) |  | 


#### slurmdb_v0038_get_clusters.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_config**
<a id="slurmdb_v0038_get_config"></a>
> Dbv0038ConfigInfo slurmdb_v0038_get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_config_info import Dbv0038ConfigInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Dump all configuration information
        api_response = api_instance.slurmdb_v0038_get_config()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_config: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_config.ApiResponseFor200) | slurmdbd configuration
default | [ApiResponseForDefault](#slurmdb_v0038_get_config.ApiResponseForDefault) | Unable to dump config

#### slurmdb_v0038_get_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ConfigInfo**](../../models/Dbv0038ConfigInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ConfigInfo**](../../models/Dbv0038ConfigInfo.md) |  | 


#### slurmdb_v0038_get_config.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_job**
<a id="slurmdb_v0038_get_job"></a>
> Dbv0038JobInfo slurmdb_v0038_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_job_info import Dbv0038JobInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    try:
        # Get job info
        api_response = api_instance.slurmdb_v0038_get_job(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | JobIdSchema | | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_job.ApiResponseFor200) | Job description
default | [ApiResponseForDefault](#slurmdb_v0038_get_job.ApiResponseForDefault) | Unable to find job

#### slurmdb_v0038_get_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038JobInfo**](../../models/Dbv0038JobInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038JobInfo**](../../models/Dbv0038JobInfo.md) |  | 


#### slurmdb_v0038_get_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_jobs**
<a id="slurmdb_v0038_get_jobs"></a>
> Dbv0038JobInfo slurmdb_v0038_get_jobs()

Get job list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_job_info import Dbv0038JobInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'submit_time': "submit_time_example",
        'start_time': "start_time_example",
        'end_time': "end_time_example",
        'account': "account_example",
        'association': "association_example",
        'cluster': "cluster_example",
        'constraints': "constraints_example",
        'cpus_max': "cpus_max_example",
        'cpus_min': "cpus_min_example",
        'skip_steps': True,
        'disable_wait_for_result': True,
        'exit_code': "exit_code_example",
        'format': "format_example",
        'group': "group_example",
        'job_name': "job_name_example",
        'nodes_max': "nodes_max_example",
        'nodes_min': "nodes_min_example",
        'partition': "partition_example",
        'qos': "qos_example",
        'reason': "reason_example",
        'reservation': "reservation_example",
        'state': "state_example",
        'step': "step_example",
        'node': "node_example",
        'wckey': "wckey_example",
    }
    try:
        # Get job list
        api_response = api_instance.slurmdb_v0038_get_jobs(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_jobs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
submit_time | SubmitTimeSchema | | optional
start_time | StartTimeSchema | | optional
end_time | EndTimeSchema | | optional
account | AccountSchema | | optional
association | AssociationSchema | | optional
cluster | ClusterSchema | | optional
constraints | ConstraintsSchema | | optional
cpus_max | CpusMaxSchema | | optional
cpus_min | CpusMinSchema | | optional
skip_steps | SkipStepsSchema | | optional
disable_wait_for_result | DisableWaitForResultSchema | | optional
exit_code | ExitCodeSchema | | optional
format | FormatSchema | | optional
group | GroupSchema | | optional
job_name | JobNameSchema | | optional
nodes_max | NodesMaxSchema | | optional
nodes_min | NodesMinSchema | | optional
partition | PartitionSchema | | optional
qos | QosSchema | | optional
reason | ReasonSchema | | optional
reservation | ReservationSchema | | optional
state | StateSchema | | optional
step | StepSchema | | optional
node | NodeSchema | | optional
wckey | WckeySchema | | optional


# SubmitTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssociationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConstraintsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CpusMaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CpusMinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SkipStepsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# DisableWaitForResultSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ExitCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodesMaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodesMinSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartitionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# QosSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ReasonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ReservationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StepSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WckeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_jobs.ApiResponseFor200) | List of jobs
default | [ApiResponseForDefault](#slurmdb_v0038_get_jobs.ApiResponseForDefault) | Unable to query jobs

#### slurmdb_v0038_get_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038JobInfo**](../../models/Dbv0038JobInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038JobInfo**](../../models/Dbv0038JobInfo.md) |  | 


#### slurmdb_v0038_get_jobs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_qos**
<a id="slurmdb_v0038_get_qos"></a>
> Dbv0038QosInfo slurmdb_v0038_get_qos()

Get QOS list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_qos_info import Dbv0038QosInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'with_deleted': True,
    }
    try:
        # Get QOS list
        api_response = api_instance.slurmdb_v0038_get_qos(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_qos: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
with_deleted | WithDeletedSchema | | optional


# WithDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_qos.ApiResponseFor200) | List of QOS&#x27;
default | [ApiResponseForDefault](#slurmdb_v0038_get_qos.ApiResponseForDefault) | QOS not found

#### slurmdb_v0038_get_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038QosInfo**](../../models/Dbv0038QosInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038QosInfo**](../../models/Dbv0038QosInfo.md) |  | 


#### slurmdb_v0038_get_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_single_qos**
<a id="slurmdb_v0038_get_single_qos"></a>
> Dbv0038QosInfo slurmdb_v0038_get_single_qos(qos_name)

Get QOS info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_qos_info import Dbv0038QosInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'qos_name': "qos_name_example",
    }
    query_params = {
    }
    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0038_get_single_qos(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_single_qos: %s\n" % e)

    # example passing only optional values
    path_params = {
        'qos_name': "qos_name_example",
    }
    query_params = {
        'with_deleted': True,
    }
    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0038_get_single_qos(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_single_qos: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
with_deleted | WithDeletedSchema | | optional


# WithDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
qos_name | QosNameSchema | | 

# QosNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_single_qos.ApiResponseFor200) | QOS information
default | [ApiResponseForDefault](#slurmdb_v0038_get_single_qos.ApiResponseForDefault) | QOS not found

#### slurmdb_v0038_get_single_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038QosInfo**](../../models/Dbv0038QosInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038QosInfo**](../../models/Dbv0038QosInfo.md) |  | 


#### slurmdb_v0038_get_single_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_tres**
<a id="slurmdb_v0038_get_tres"></a>
> Dbv0038TresInfo slurmdb_v0038_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_tres_info import Dbv0038TresInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get TRES info
        api_response = api_instance.slurmdb_v0038_get_tres()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_tres: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_tres.ApiResponseFor200) | List of TRES
default | [ApiResponseForDefault](#slurmdb_v0038_get_tres.ApiResponseForDefault) | Unable to retrieve TRES

#### slurmdb_v0038_get_tres.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038TresInfo**](../../models/Dbv0038TresInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038TresInfo**](../../models/Dbv0038TresInfo.md) |  | 


#### slurmdb_v0038_get_tres.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_user**
<a id="slurmdb_v0038_get_user"></a>
> Dbv0038UserInfo slurmdb_v0038_get_user(user_name)

Get user info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_user_info import Dbv0038UserInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_name': "user_name_example",
    }
    query_params = {
    }
    try:
        # Get user info
        api_response = api_instance.slurmdb_v0038_get_user(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_name': "user_name_example",
    }
    query_params = {
        'with_deleted': True,
    }
    try:
        # Get user info
        api_response = api_instance.slurmdb_v0038_get_user(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
with_deleted | WithDeletedSchema | | optional


# WithDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_name | UserNameSchema | | 

# UserNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_user.ApiResponseFor200) | List of users
default | [ApiResponseForDefault](#slurmdb_v0038_get_user.ApiResponseForDefault) | User not found

#### slurmdb_v0038_get_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UserInfo**](../../models/Dbv0038UserInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UserInfo**](../../models/Dbv0038UserInfo.md) |  | 


#### slurmdb_v0038_get_user.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_users**
<a id="slurmdb_v0038_get_users"></a>
> Dbv0038UserInfo slurmdb_v0038_get_users()

Get user list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_user_info import Dbv0038UserInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    query_params = {
        'with_deleted': True,
    }
    try:
        # Get user list
        api_response = api_instance.slurmdb_v0038_get_users(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_users: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
with_deleted | WithDeletedSchema | | optional


# WithDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_users.ApiResponseFor200) | List of users
default | [ApiResponseForDefault](#slurmdb_v0038_get_users.ApiResponseForDefault) | User not found

#### slurmdb_v0038_get_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UserInfo**](../../models/Dbv0038UserInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UserInfo**](../../models/Dbv0038UserInfo.md) |  | 


#### slurmdb_v0038_get_users.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_wckey**
<a id="slurmdb_v0038_get_wckey"></a>
> Dbv0038WckeyInfo slurmdb_v0038_get_wckey(wckey)

Get wckey info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_wckey_info import Dbv0038WckeyInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'wckey': "wckey_example",
    }
    try:
        # Get wckey info
        api_response = api_instance.slurmdb_v0038_get_wckey(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_wckey: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
wckey | WckeySchema | | 

# WckeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_wckey.ApiResponseFor200) | List of wckey
default | [ApiResponseForDefault](#slurmdb_v0038_get_wckey.ApiResponseForDefault) | wckey not found

#### slurmdb_v0038_get_wckey.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038WckeyInfo**](../../models/Dbv0038WckeyInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038WckeyInfo**](../../models/Dbv0038WckeyInfo.md) |  | 


#### slurmdb_v0038_get_wckey.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_get_wckeys**
<a id="slurmdb_v0038_get_wckeys"></a>
> Dbv0038WckeyInfo slurmdb_v0038_get_wckeys()

Get wckey list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_wckey_info import Dbv0038WckeyInfo
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get wckey list
        api_response = api_instance.slurmdb_v0038_get_wckeys()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_get_wckeys: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_get_wckeys.ApiResponseFor200) | List of wckeys
default | [ApiResponseForDefault](#slurmdb_v0038_get_wckeys.ApiResponseForDefault) | wckey not found

#### slurmdb_v0038_get_wckeys.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038WckeyInfo**](../../models/Dbv0038WckeyInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038WckeyInfo**](../../models/Dbv0038WckeyInfo.md) |  | 


#### slurmdb_v0038_get_wckeys.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_set_config**
<a id="slurmdb_v0038_set_config"></a>
> Dbv0038ConfigResponse slurmdb_v0038_set_config()

Load all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_set_config import Dbv0038SetConfig
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_config_response import Dbv0038ConfigResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    body = Dbv0038SetConfig(
        clusters=[
            Dbv0038ClustersProperties(
                clusters=Dbv0038ClusterInfo(
                    controller=dict(
                        host="host_example",
                        port=1,
                    ),
                    flags=[
                        "flags_example"
                    ],
                    name="name_example",
                    nodes="nodes_example",
                    select_plugin="select_plugin_example",
                    associations=dict(
                        root=Dbv0038AssociationShortInfo(
                            account="account_example",
                            cluster="cluster_example",
                            partition="partition_example",
                            user="user_example",
                        ),
                    ),
                    rpc_version=1,
                    tres=[
                        Dbv0038ResponseTres(
                            meta=Dbv0038Meta(
                                plugin=dict(
                                    type="type_example",
                                    name="name_example",
                                ),
                                slurm=dict(
                                    version=dict(
                                        major="major_example",
                                        micro="micro_example",
                                        minor="minor_example",
                                    ),
                                    release="release_example",
                                ),
                            ),
                            errors=[
                                Dbv0038Error(
                                    error_number=1,
                                    error="error_example",
                                    source="source_example",
                                    description="description_example",
                                )
                            ],
                        )
                    ],
                ),
            )
        ],
        tres=[
            Dbv0038TresList([
                dict(
                    type="type_example",
                    name="name_example",
                    id=1,
                    count=1,
                )
            ])
        ],
        accounts=[
            Dbv0038UpdateAccount(
                accounts=[
                    Dbv0038Account(
                        associations=[
                            Dbv0038AssociationShortInfo()
                        ],
                        coordinators=[
                            Dbv0038CoordinatorInfo(
                                name="name_example",
                                direct=1,
                            )
                        ],
                        description="description_example",
                        name="name_example",
                        organization="organization_example",
                        flags=[
                            "flags_example"
                        ],
                    )
                ],
            )
        ],
        users=[
            Dbv0038User(
                administrator_level="administrator_level_example",
                associations=[
                    Dbv0038AssociationShortInfo()
                ],
,
                default=dict(
                    account="account_example",
                    wckey="wckey_example",
                ),
                flags=[
                    "flags_example"
                ],
                name="name_example",
            )
        ],
        qos=[
            Dbv0038Qos(
                description="description_example",
                flags=[
                    "flags_example"
                ],
                id="id_example",
                limits=dict(
                    factor=3.14,
                    max=dict(
                        wall_clock=dict(
                            per=dict(
                                qos=1,
                                job=1,
                            ),
                        ),
                        jobs=dict(
                            active_jobs=dict(
                                per=dict(
                                    account=1,
                                    user=1,
                                ),
                            ),
                        ),
                        accruing=dict(
                            per=dict(
                                account=1,
                                user=1,
                            ),
                        ),
                        tres=dict(
                            minutes=dict(
                                per=dict(
,
,
,
,
                                ),
                            ),
                            per=dict(
,
,
,
,
                            ),
                        ),
                    ),
                    min=dict(
                        priority_threshold=1,
                        tres=dict(
                            per=dict(
,
                            ),
                        ),
                    ),
                ),
                preempt=dict(
                    _list=[
                        "_list_example"
                    ],
                    mode=[
                        "mode_example"
                    ],
                    exempt_time=1,
                ),
                priority=1,
                usage_factor=3.14,
                usage_threshold=3.14,
                name="name_example",
            )
        ],
        wckeys=[
            Dbv0038Wckey(
                cluster="cluster_example",
                id=1,
                name="name_example",
                user="user_example",
                flags=[
                    "flags_example"
                ],
                accounting=[
                    Dbv0038Accounting(
                        allocated=1,
                        id=1,
                        start=1,
,
                    )
                ],
            )
        ],
        associations=[
            Dbv0038Association(
                account="account_example",
                cluster="cluster_example",
                default=dict(
                    qos="qos_example",
                ),
                flags=[
                    "flags_example"
                ],
                max=dict(
                    jobs=dict(
                        per=dict(
                            wall_clock=1,
                        ),
                    ),
                    per=dict(
                        account=dict(
                            wall_clock=1,
                        ),
                    ),
                    tres=dict(
                        per=dict(
,
,
                        ),
,
                        minutes=dict(
                            per=dict(
,
                            ),
,
                        ),
                    ),
                ),
                min=dict(
                    priority_threshold=1,
                ),
                parent_account="parent_account_example",
                partition="partition_example",
                priority=1,
                shares_raw=1,
                usage=dict(
                    accrue_job_count=1,
                    group_used_wallclock=3.14,
                    fairshare_factor=3.14,
                    fairshare_shares=1,
                    normalized_priority=1,
                    normalized_shares=3.14,
                    effective_normalized_usage=3.14,
                    raw_usage=1,
                    job_count=1,
                    fairshare_level=3.14,
                ),
                user="user_example",
                qos=[
                    "qos_example"
                ],
            )
        ],
    )
    try:
        # Load all configuration information
        api_response = api_instance.slurmdb_v0038_set_config(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_set_config: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038SetConfig**](../../models/Dbv0038SetConfig.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038SetConfig**](../../models/Dbv0038SetConfig.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_set_config.ApiResponseFor200) | Load config
default | [ApiResponseForDefault](#slurmdb_v0038_set_config.ApiResponseForDefault) | Unable to set config

#### slurmdb_v0038_set_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ConfigResponse**](../../models/Dbv0038ConfigResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ConfigResponse**](../../models/Dbv0038ConfigResponse.md) |  | 


#### slurmdb_v0038_set_config.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_update_account**
<a id="slurmdb_v0038_update_account"></a>
> Dbv0038AccountResponse slurmdb_v0038_update_account(dbv0038_update_account)

Update accounts

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_account_response import Dbv0038AccountResponse
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_update_account import Dbv0038UpdateAccount
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0038UpdateAccount(
        accounts=[
            Dbv0038Account(
                associations=[
                    Dbv0038AssociationShortInfo(
                        account="account_example",
                        cluster="cluster_example",
                        partition="partition_example",
                        user="user_example",
                    )
                ],
                coordinators=[
                    Dbv0038CoordinatorInfo(
                        name="name_example",
                        direct=1,
                    )
                ],
                description="description_example",
                name="name_example",
                organization="organization_example",
                flags=[
                    "flags_example"
                ],
            )
        ],
    )
    try:
        # Update accounts
        api_response = api_instance.slurmdb_v0038_update_account(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_account: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UpdateAccount**](../../models/Dbv0038UpdateAccount.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UpdateAccount**](../../models/Dbv0038UpdateAccount.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_update_account.ApiResponseFor200) | Add/update list of accounts
default | [ApiResponseForDefault](#slurmdb_v0038_update_account.ApiResponseForDefault) | Unable to add or update accounts

#### slurmdb_v0038_update_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AccountResponse**](../../models/Dbv0038AccountResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AccountResponse**](../../models/Dbv0038AccountResponse.md) |  | 


#### slurmdb_v0038_update_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_update_associations**
<a id="slurmdb_v0038_update_associations"></a>
> Dbv0038ResponseAssociations slurmdb_v0038_update_associations(dbv0038_associations_info)

Set associations info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_response_associations import Dbv0038ResponseAssociations
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_associations_info import Dbv0038AssociationsInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0038AssociationsInfo(
        meta=Dbv0038Meta(
            plugin=dict(
                type="type_example",
                name="name_example",
            ),
            slurm=dict(
                version=dict(
                    major="major_example",
                    micro="micro_example",
                    minor="minor_example",
                ),
                release="release_example",
            ),
        ),
        errors=[
            Dbv0038Error(
                error_number=1,
                error="error_example",
                source="source_example",
                description="description_example",
            )
        ],
        associations=[
            Dbv0038Association(
                account="account_example",
                cluster="cluster_example",
                default=dict(
                    qos="qos_example",
                ),
                flags=[
                    "flags_example"
                ],
                max=dict(
                    jobs=dict(
                        per=dict(
                            wall_clock=1,
                        ),
                    ),
                    per=dict(
                        account=dict(
                            wall_clock=1,
                        ),
                    ),
                    tres=dict(
                        per=dict(
                            job=Dbv0038TresList([
                                dict(
                                    type="type_example",
                                    name="name_example",
                                    id=1,
                                    count=1,
                                )
                            ]),
,
                        ),
,
                        minutes=dict(
                            per=dict(
,
                            ),
,
                        ),
                    ),
                ),
                min=dict(
                    priority_threshold=1,
                ),
                parent_account="parent_account_example",
                partition="partition_example",
                priority=1,
                shares_raw=1,
                usage=dict(
                    accrue_job_count=1,
                    group_used_wallclock=3.14,
                    fairshare_factor=3.14,
                    fairshare_shares=1,
                    normalized_priority=1,
                    normalized_shares=3.14,
                    effective_normalized_usage=3.14,
                    raw_usage=1,
                    job_count=1,
                    fairshare_level=3.14,
                ),
                user="user_example",
                qos=[
                    "qos_example"
                ],
            )
        ],
    )
    try:
        # Set associations info
        api_response = api_instance.slurmdb_v0038_update_associations(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_associations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AssociationsInfo**](../../models/Dbv0038AssociationsInfo.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038AssociationsInfo**](../../models/Dbv0038AssociationsInfo.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_update_associations.ApiResponseFor200) | status of associations update
default | [ApiResponseForDefault](#slurmdb_v0038_update_associations.ApiResponseForDefault) | Unable to update associations

#### slurmdb_v0038_update_associations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseAssociations**](../../models/Dbv0038ResponseAssociations.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseAssociations**](../../models/Dbv0038ResponseAssociations.md) |  | 


#### slurmdb_v0038_update_associations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_update_qos**
<a id="slurmdb_v0038_update_qos"></a>
> Dbv0038ResponseQos slurmdb_v0038_update_qos(dbv0038_update_qos)

Set QOS info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_update_qos import Dbv0038UpdateQos
from slurmrestapi.model.dbv0038_response_qos import Dbv0038ResponseQos
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0038UpdateQos(
        qos=[
            Dbv0038Qos(
                description="description_example",
                flags=[
                    "flags_example"
                ],
                id="id_example",
                limits=dict(
                    factor=3.14,
                    max=dict(
                        wall_clock=dict(
                            per=dict(
                                qos=1,
                                job=1,
                            ),
                        ),
                        jobs=dict(
                            active_jobs=dict(
                                per=dict(
                                    account=1,
                                    user=1,
                                ),
                            ),
                        ),
                        accruing=dict(
                            per=dict(
                                account=1,
                                user=1,
                            ),
                        ),
                        tres=dict(
                            minutes=dict(
                                per=dict(
                                    job=Dbv0038TresList([
                                        dict(
                                            type="type_example",
                                            name="name_example",
                                            id=1,
                                            count=1,
                                        )
                                    ]),
,
,
,
                                ),
                            ),
                            per=dict(
,
,
,
,
                            ),
                        ),
                    ),
                    min=dict(
                        priority_threshold=1,
                        tres=dict(
                            per=dict(
,
                            ),
                        ),
                    ),
                ),
                preempt=dict(
                    _list=[
                        "_list_example"
                    ],
                    mode=[
                        "mode_example"
                    ],
                    exempt_time=1,
                ),
                priority=1,
                usage_factor=3.14,
                usage_threshold=3.14,
                name="name_example",
            )
        ],
    )
    try:
        # Set QOS info
        api_response = api_instance.slurmdb_v0038_update_qos(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_qos: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UpdateQos**](../../models/Dbv0038UpdateQos.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UpdateQos**](../../models/Dbv0038UpdateQos.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_update_qos.ApiResponseFor200) | QOS update response
default | [ApiResponseForDefault](#slurmdb_v0038_update_qos.ApiResponseForDefault) | Unable to update QOSs

#### slurmdb_v0038_update_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseQos**](../../models/Dbv0038ResponseQos.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseQos**](../../models/Dbv0038ResponseQos.md) |  | 


#### slurmdb_v0038_update_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_update_tres**
<a id="slurmdb_v0038_update_tres"></a>
> Dbv0038ResponseTres slurmdb_v0038_update_tres(dbv0038_tres_update)

Set TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_tres_update import Dbv0038TresUpdate
from slurmrestapi.model.dbv0038_response_tres import Dbv0038ResponseTres
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0038TresUpdate(
        tres=Dbv0038TresList([
            dict(
                type="type_example",
                name="name_example",
                id=1,
                count=1,
            )
        ]),
    )
    try:
        # Set TRES info
        api_response = api_instance.slurmdb_v0038_update_tres(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_tres: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038TresUpdate**](../../models/Dbv0038TresUpdate.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038TresUpdate**](../../models/Dbv0038TresUpdate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_update_tres.ApiResponseFor200) | List of TRES
default | [ApiResponseForDefault](#slurmdb_v0038_update_tres.ApiResponseForDefault) | Unable to update TRES

#### slurmdb_v0038_update_tres.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseTres**](../../models/Dbv0038ResponseTres.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseTres**](../../models/Dbv0038ResponseTres.md) |  | 


#### slurmdb_v0038_update_tres.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0038_update_users**
<a id="slurmdb_v0038_update_users"></a>
> Dbv0038ResponseUserUpdate slurmdb_v0038_update_users(dbv0038_update_users)

Update user

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0038_update_users import Dbv0038UpdateUsers
from slurmrestapi.model.dbv0038_errors import Dbv0038Errors
from slurmrestapi.model.dbv0038_response_user_update import Dbv0038ResponseUserUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0038UpdateUsers(
        users=[
            Dbv0038User(
                administrator_level="administrator_level_example",
                associations=[
                    Dbv0038AssociationShortInfo(
                        account="account_example",
                        cluster="cluster_example",
                        partition="partition_example",
                        user="user_example",
                    )
                ],
                coordinators=[
                    Dbv0038CoordinatorInfo(
                        name="name_example",
                        direct=1,
                    )
                ],
                default=dict(
                    account="account_example",
                    wckey="wckey_example",
                ),
                flags=[
                    "flags_example"
                ],
                name="name_example",
            )
        ],
    )
    try:
        # Update user
        api_response = api_instance.slurmdb_v0038_update_users(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0038_update_users: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UpdateUsers**](../../models/Dbv0038UpdateUsers.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038UpdateUsers**](../../models/Dbv0038UpdateUsers.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0038_update_users.ApiResponseFor200) | Update users
default | [ApiResponseForDefault](#slurmdb_v0038_update_users.ApiResponseForDefault) | User not found or not able to update user

#### slurmdb_v0038_update_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseUserUpdate**](../../models/Dbv0038ResponseUserUpdate.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038ResponseUserUpdate**](../../models/Dbv0038ResponseUserUpdate.md) |  | 


#### slurmdb_v0038_update_users.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0038Errors**](../../models/Dbv0038Errors.md) |  | 


### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

