<a id="__pageTop"></a>
# slurmrestapi.apis.tags.slurm_api.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurmctld_cancel_job**](#slurmctld_cancel_job) | **delete** /slurm/v0.0.37/job/{job_id} | cancel or signal job
[**slurmctld_diag**](#slurmctld_diag) | **get** /slurm/v0.0.37/diag | get diagnostics
[**slurmctld_get_job**](#slurmctld_get_job) | **get** /slurm/v0.0.37/job/{job_id} | get job info
[**slurmctld_get_jobs**](#slurmctld_get_jobs) | **get** /slurm/v0.0.37/jobs | get list of jobs
[**slurmctld_get_node**](#slurmctld_get_node) | **get** /slurm/v0.0.37/node/{node_name} | get node info
[**slurmctld_get_nodes**](#slurmctld_get_nodes) | **get** /slurm/v0.0.37/nodes | get all node info
[**slurmctld_get_partition**](#slurmctld_get_partition) | **get** /slurm/v0.0.37/partition/{partition_name} | get partition info
[**slurmctld_get_partitions**](#slurmctld_get_partitions) | **get** /slurm/v0.0.37/partitions | get all partition info
[**slurmctld_get_reservation**](#slurmctld_get_reservation) | **get** /slurm/v0.0.37/reservation/{reservation_name} | get reservation info
[**slurmctld_get_reservations**](#slurmctld_get_reservations) | **get** /slurm/v0.0.37/reservations | get all reservation info
[**slurmctld_ping**](#slurmctld_ping) | **get** /slurm/v0.0.37/ping | ping test
[**slurmctld_submit_job**](#slurmctld_submit_job) | **post** /slurm/v0.0.37/job/submit | submit new job
[**slurmctld_update_job**](#slurmctld_update_job) | **post** /slurm/v0.0.37/job/{job_id} | update job
[**slurmdbd_add_clusters**](#slurmdbd_add_clusters) | **post** /slurmdb/v0.0.37/clusters | Add clusters
[**slurmdbd_add_wckeys**](#slurmdbd_add_wckeys) | **post** /slurmdb/v0.0.37/wckeys | Add wckeys
[**slurmdbd_delete_account**](#slurmdbd_delete_account) | **delete** /slurmdb/v0.0.37/account/{account_name} | Delete account
[**slurmdbd_delete_association**](#slurmdbd_delete_association) | **delete** /slurmdb/v0.0.37/association | Delete association
[**slurmdbd_delete_cluster**](#slurmdbd_delete_cluster) | **delete** /slurmdb/v0.0.37/cluster/{cluster_name} | Delete cluster
[**slurmdbd_delete_qos**](#slurmdbd_delete_qos) | **delete** /slurmdb/v0.0.37/qos/{qos_name} | Delete QOS
[**slurmdbd_delete_user**](#slurmdbd_delete_user) | **delete** /slurmdb/v0.0.37/user/{user_name} | Delete user
[**slurmdbd_delete_wckey**](#slurmdbd_delete_wckey) | **delete** /slurmdb/v0.0.37/wckey/{wckey} | Delete wckey
[**slurmdbd_diag**](#slurmdbd_diag) | **get** /slurmdb/v0.0.37/diag | Get slurmdb diagnostics
[**slurmdbd_get_account**](#slurmdbd_get_account) | **get** /slurmdb/v0.0.37/account/{account_name} | Get account info
[**slurmdbd_get_accounts**](#slurmdbd_get_accounts) | **get** /slurmdb/v0.0.37/accounts | Get account list
[**slurmdbd_get_association**](#slurmdbd_get_association) | **get** /slurmdb/v0.0.37/association | Get association info
[**slurmdbd_get_associations**](#slurmdbd_get_associations) | **get** /slurmdb/v0.0.37/associations | Get association list
[**slurmdbd_get_cluster**](#slurmdbd_get_cluster) | **get** /slurmdb/v0.0.37/cluster/{cluster_name} | Get cluster info
[**slurmdbd_get_clusters**](#slurmdbd_get_clusters) | **get** /slurmdb/v0.0.37/clusters | Get cluster list
[**slurmdbd_get_db_config**](#slurmdbd_get_db_config) | **get** /slurmdb/v0.0.37/config | Dump all configuration information
[**slurmdbd_get_job**](#slurmdbd_get_job) | **get** /slurmdb/v0.0.37/job/{job_id} | Get job info
[**slurmdbd_get_jobs**](#slurmdbd_get_jobs) | **get** /slurmdb/v0.0.37/jobs | Get job list
[**slurmdbd_get_qos**](#slurmdbd_get_qos) | **get** /slurmdb/v0.0.37/qos | Get QOS list
[**slurmdbd_get_single_qos**](#slurmdbd_get_single_qos) | **get** /slurmdb/v0.0.37/qos/{qos_name} | Get QOS info
[**slurmdbd_get_tres**](#slurmdbd_get_tres) | **get** /slurmdb/v0.0.37/tres | Get TRES info
[**slurmdbd_get_user**](#slurmdbd_get_user) | **get** /slurmdb/v0.0.37/user/{user_name} | Get user info
[**slurmdbd_get_users**](#slurmdbd_get_users) | **get** /slurmdb/v0.0.37/users | Get user list
[**slurmdbd_get_wckey**](#slurmdbd_get_wckey) | **get** /slurmdb/v0.0.37/wckey/{wckey} | Get wckey info
[**slurmdbd_get_wckeys**](#slurmdbd_get_wckeys) | **get** /slurmdb/v0.0.37/wckeys | Get wckey list
[**slurmdbd_set_db_config**](#slurmdbd_set_db_config) | **post** /slurmdb/v0.0.37/config | Load all configuration information
[**slurmdbd_update_account**](#slurmdbd_update_account) | **post** /slurmdb/v0.0.37/accounts | Update accounts
[**slurmdbd_update_associations**](#slurmdbd_update_associations) | **post** /slurmdb/v0.0.37/associations | Set associations info
[**slurmdbd_update_tres**](#slurmdbd_update_tres) | **post** /slurmdb/v0.0.37/tres | Set TRES info
[**slurmdbd_update_users**](#slurmdbd_update_users) | **post** /slurmdb/v0.0.37/users | Update user

# **slurmctld_cancel_job**
<a id="slurmctld_cancel_job"></a>
> slurmctld_cancel_job(job_id)

cancel or signal job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_signal import V0037Signal
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
        api_response = api_instance.slurmctld_cancel_job(
            path_params=path_params,
            query_params=query_params,
        )
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_cancel_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'job_id': "job_id_example",
    }
    query_params = {
        'signal': V0037Signal("HUP"),
    }
    try:
        # cancel or signal job
        api_response = api_instance.slurmctld_cancel_job(
            path_params=path_params,
            query_params=query_params,
        )
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_cancel_job: %s\n" % e)
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
[**V0037Signal**](../../models/V0037Signal.md) |  | 


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
200 | [ApiResponseFor200](#slurmctld_cancel_job.ApiResponseFor200) | job cancelled or sent signal
500 | [ApiResponseFor500](#slurmctld_cancel_job.ApiResponseFor500) | job not found

#### slurmctld_cancel_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slurmctld_cancel_job.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_diag**
<a id="slurmctld_diag"></a>
> V0037Diag slurmctld_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_diag import V0037Diag
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
        api_response = api_instance.slurmctld_diag()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_diag: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmctld_diag.ApiResponseFor200) | diagnostic results
default | [ApiResponseForDefault](#slurmctld_diag.ApiResponseForDefault) | unable to request ping test

#### slurmctld_diag.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037Diag**](../../models/V0037Diag.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037Diag**](../../models/V0037Diag.md) |  | 


#### slurmctld_diag.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_get_job**
<a id="slurmctld_get_job"></a>
> V0037JobsResponse slurmctld_get_job(job_id)

get job info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_jobs_response import V0037JobsResponse
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
        api_response = api_instance.slurmctld_get_job(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_job: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmctld_get_job.ApiResponseFor200) | job(s) information
default | [ApiResponseForDefault](#slurmctld_get_job.ApiResponseForDefault) | job matching JobId not found

#### slurmctld_get_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037JobsResponse**](../../models/V0037JobsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037JobsResponse**](../../models/V0037JobsResponse.md) |  | 


#### slurmctld_get_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_get_jobs**
<a id="slurmctld_get_jobs"></a>
> V0037JobsResponse slurmctld_get_jobs()

get list of jobs

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_jobs_response import V0037JobsResponse
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
        api_response = api_instance.slurmctld_get_jobs(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_jobs: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmctld_get_jobs.ApiResponseFor200) | job(s) information
default | [ApiResponseForDefault](#slurmctld_get_jobs.ApiResponseForDefault) | job not found

#### slurmctld_get_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037JobsResponse**](../../models/V0037JobsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037JobsResponse**](../../models/V0037JobsResponse.md) |  | 


#### slurmctld_get_jobs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_get_node**
<a id="slurmctld_get_node"></a>
> V0037NodesResponse slurmctld_get_node(node_name)

get node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_nodes_response import V0037NodesResponse
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
        api_response = api_instance.slurmctld_get_node(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_node: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmctld_get_node.ApiResponseFor200) | node information
default | [ApiResponseForDefault](#slurmctld_get_node.ApiResponseForDefault) | node not found

#### slurmctld_get_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037NodesResponse**](../../models/V0037NodesResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037NodesResponse**](../../models/V0037NodesResponse.md) |  | 


#### slurmctld_get_node.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_get_nodes**
<a id="slurmctld_get_nodes"></a>
> V0037NodesResponse slurmctld_get_nodes()

get all node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_nodes_response import V0037NodesResponse
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
        api_response = api_instance.slurmctld_get_nodes(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_nodes: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmctld_get_nodes.ApiResponseFor200) | node information
default | [ApiResponseForDefault](#slurmctld_get_nodes.ApiResponseForDefault) | no nodes in cluster

#### slurmctld_get_nodes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037NodesResponse**](../../models/V0037NodesResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037NodesResponse**](../../models/V0037NodesResponse.md) |  | 


#### slurmctld_get_nodes.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_get_partition**
<a id="slurmctld_get_partition"></a>
> V0037PartitionsResponse slurmctld_get_partition(partition_name)

get partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_partitions_response import V0037PartitionsResponse
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
        api_response = api_instance.slurmctld_get_partition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_partition: %s\n" % e)

    # example passing only optional values
    path_params = {
        'partition_name': "partition_name_example",
    }
    query_params = {
        'update_time': 1,
    }
    try:
        # get partition info
        api_response = api_instance.slurmctld_get_partition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_partition: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmctld_get_partition.ApiResponseFor200) | partition information
default | [ApiResponseForDefault](#slurmctld_get_partition.ApiResponseForDefault) | no partitions found

#### slurmctld_get_partition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037PartitionsResponse**](../../models/V0037PartitionsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037PartitionsResponse**](../../models/V0037PartitionsResponse.md) |  | 


#### slurmctld_get_partition.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_get_partitions**
<a id="slurmctld_get_partitions"></a>
> V0037PartitionsResponse slurmctld_get_partitions()

get all partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_partitions_response import V0037PartitionsResponse
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
        api_response = api_instance.slurmctld_get_partitions(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_partitions: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmctld_get_partitions.ApiResponseFor200) | partition information
default | [ApiResponseForDefault](#slurmctld_get_partitions.ApiResponseForDefault) | no partitions found

#### slurmctld_get_partitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037PartitionsResponse**](../../models/V0037PartitionsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037PartitionsResponse**](../../models/V0037PartitionsResponse.md) |  | 


#### slurmctld_get_partitions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_get_reservation**
<a id="slurmctld_get_reservation"></a>
> V0037ReservationsResponse slurmctld_get_reservation(reservation_name)

get reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_reservations_response import V0037ReservationsResponse
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
        api_response = api_instance.slurmctld_get_reservation(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_reservation: %s\n" % e)

    # example passing only optional values
    path_params = {
        'reservation_name': "reservation_name_example",
    }
    query_params = {
        'update_time': 1,
    }
    try:
        # get reservation info
        api_response = api_instance.slurmctld_get_reservation(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_reservation: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmctld_get_reservation.ApiResponseFor200) | reservation information
default | [ApiResponseForDefault](#slurmctld_get_reservation.ApiResponseForDefault) | no reservations found

#### slurmctld_get_reservation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037ReservationsResponse**](../../models/V0037ReservationsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037ReservationsResponse**](../../models/V0037ReservationsResponse.md) |  | 


#### slurmctld_get_reservation.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_get_reservations**
<a id="slurmctld_get_reservations"></a>
> V0037ReservationsResponse slurmctld_get_reservations()

get all reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_reservations_response import V0037ReservationsResponse
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
        api_response = api_instance.slurmctld_get_reservations(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_get_reservations: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmctld_get_reservations.ApiResponseFor200) | reservation information
default | [ApiResponseForDefault](#slurmctld_get_reservations.ApiResponseForDefault) | no reservations found

#### slurmctld_get_reservations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037ReservationsResponse**](../../models/V0037ReservationsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037ReservationsResponse**](../../models/V0037ReservationsResponse.md) |  | 


#### slurmctld_get_reservations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_ping**
<a id="slurmctld_ping"></a>
> V0037Pings slurmctld_ping()

ping test

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_pings import V0037Pings
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
        api_response = api_instance.slurmctld_ping()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_ping: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmctld_ping.ApiResponseFor200) | results of ping test
default | [ApiResponseForDefault](#slurmctld_ping.ApiResponseForDefault) | unable to request ping test

#### slurmctld_ping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037Pings**](../../models/V0037Pings.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037Pings**](../../models/V0037Pings.md) |  | 


#### slurmctld_ping.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_submit_job**
<a id="slurmctld_submit_job"></a>
> V0037JobSubmissionResponse slurmctld_submit_job(v0037_job_submission)

submit new job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_job_submission import V0037JobSubmission
from slurmrestapi.model.v0037_job_submission_response import V0037JobSubmissionResponse
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
    body = V0037JobSubmission(None)
    try:
        # submit new job
        api_response = api_instance.slurmctld_submit_job(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_submit_job: %s\n" % e)
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
[**V0037JobSubmission**](../../models/V0037JobSubmission.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037JobSubmission**](../../models/V0037JobSubmission.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmctld_submit_job.ApiResponseFor200) | job submitted
default | [ApiResponseForDefault](#slurmctld_submit_job.ApiResponseForDefault) | job rejected

#### slurmctld_submit_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037JobSubmissionResponse**](../../models/V0037JobSubmissionResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037JobSubmissionResponse**](../../models/V0037JobSubmissionResponse.md) |  | 


#### slurmctld_submit_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmctld_update_job**
<a id="slurmctld_update_job"></a>
> slurmctld_update_job(job_idv0037_job_properties)

update job

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0037_job_properties import V0037JobProperties
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
    body = V0037JobProperties(
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
        nice="nice_example",
        no_kill=True,
        nodes=[
            1
        ],
        open_mode="append",
        partition="partition_example",
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
        api_response = api_instance.slurmctld_update_job(
            path_params=path_params,
            body=body,
        )
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmctld_update_job: %s\n" % e)
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
[**V0037JobProperties**](../../models/V0037JobProperties.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0037JobProperties**](../../models/V0037JobProperties.md) |  | 


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
200 | [ApiResponseFor200](#slurmctld_update_job.ApiResponseFor200) | job information
500 | [ApiResponseFor500](#slurmctld_update_job.ApiResponseFor500) | job not found

#### slurmctld_update_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### slurmctld_update_job.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_add_clusters**
<a id="slurmdbd_add_clusters"></a>
> Dbv0037ResponseClusterAdd slurmdbd_add_clusters()

Add clusters

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_cluster_add import Dbv0037ResponseClusterAdd
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
        # Add clusters
        api_response = api_instance.slurmdbd_add_clusters()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_add_clusters: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_add_clusters.ApiResponseFor200) | List of clusters
default | [ApiResponseForDefault](#slurmdbd_add_clusters.ApiResponseForDefault) | Unable to add cluster

#### slurmdbd_add_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseClusterAdd**](../../models/Dbv0037ResponseClusterAdd.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseClusterAdd**](../../models/Dbv0037ResponseClusterAdd.md) |  | 


#### slurmdbd_add_clusters.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_add_wckeys**
<a id="slurmdbd_add_wckeys"></a>
> Dbv0037ResponseWckeyAdd slurmdbd_add_wckeys()

Add wckeys

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_wckey_add import Dbv0037ResponseWckeyAdd
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
        # Add wckeys
        api_response = api_instance.slurmdbd_add_wckeys()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_add_wckeys: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_add_wckeys.ApiResponseFor200) | List of wckeys
default | [ApiResponseForDefault](#slurmdbd_add_wckeys.ApiResponseForDefault) | Unable to add wckey

#### slurmdbd_add_wckeys.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseWckeyAdd**](../../models/Dbv0037ResponseWckeyAdd.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseWckeyAdd**](../../models/Dbv0037ResponseWckeyAdd.md) |  | 


#### slurmdbd_add_wckeys.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_delete_account**
<a id="slurmdbd_delete_account"></a>
> Dbv0037ResponseAccountDelete slurmdbd_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_account_delete import Dbv0037ResponseAccountDelete
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
        api_response = api_instance.slurmdbd_delete_account(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_account: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_delete_account.ApiResponseFor200) | Delete account
default | [ApiResponseForDefault](#slurmdbd_delete_account.ApiResponseForDefault) | Unable to delete account

#### slurmdbd_delete_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseAccountDelete**](../../models/Dbv0037ResponseAccountDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseAccountDelete**](../../models/Dbv0037ResponseAccountDelete.md) |  | 


#### slurmdbd_delete_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_delete_association**
<a id="slurmdbd_delete_association"></a>
> Dbv0037ResponseAssociationDelete slurmdbd_delete_association(accountuser)

Delete association

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_association_delete import Dbv0037ResponseAssociationDelete
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
    query_params = {
        'account': "account_example",
        'user': "user_example",
    }
    try:
        # Delete association
        api_response = api_instance.slurmdbd_delete_association(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_association: %s\n" % e)

    # example passing only optional values
    query_params = {
        'cluster': "cluster_example",
        'account': "account_example",
        'user': "user_example",
        'partition': "partition_example",
    }
    try:
        # Delete association
        api_response = api_instance.slurmdbd_delete_association(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_association: %s\n" % e)
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
account | AccountSchema | | 
user | UserSchema | | 
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
200 | [ApiResponseFor200](#slurmdbd_delete_association.ApiResponseFor200) | Delete associations
default | [ApiResponseForDefault](#slurmdbd_delete_association.ApiResponseForDefault) | Association not found or unable to delete association

#### slurmdbd_delete_association.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseAssociationDelete**](../../models/Dbv0037ResponseAssociationDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseAssociationDelete**](../../models/Dbv0037ResponseAssociationDelete.md) |  | 


#### slurmdbd_delete_association.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_delete_cluster**
<a id="slurmdbd_delete_cluster"></a>
> Dbv0037ResponseClusterDelete slurmdbd_delete_cluster(cluster_name)

Delete cluster

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_cluster_delete import Dbv0037ResponseClusterDelete
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
        api_response = api_instance.slurmdbd_delete_cluster(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_cluster: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_delete_cluster.ApiResponseFor200) | Delete cluster
default | [ApiResponseForDefault](#slurmdbd_delete_cluster.ApiResponseForDefault) | Cluster not found or unable to delete cluster

#### slurmdbd_delete_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseClusterDelete**](../../models/Dbv0037ResponseClusterDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseClusterDelete**](../../models/Dbv0037ResponseClusterDelete.md) |  | 


#### slurmdbd_delete_cluster.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_delete_qos**
<a id="slurmdbd_delete_qos"></a>
> Dbv0037ResponseQosDelete slurmdbd_delete_qos(qos_name)

Delete QOS

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_qos_delete import Dbv0037ResponseQosDelete
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
        api_response = api_instance.slurmdbd_delete_qos(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_qos: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_delete_qos.ApiResponseFor200) | Delete qos
default | [ApiResponseForDefault](#slurmdbd_delete_qos.ApiResponseForDefault) | Unable to delete QOS

#### slurmdbd_delete_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseQosDelete**](../../models/Dbv0037ResponseQosDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseQosDelete**](../../models/Dbv0037ResponseQosDelete.md) |  | 


#### slurmdbd_delete_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_delete_user**
<a id="slurmdbd_delete_user"></a>
> Dbv0037ResponseUserDelete slurmdbd_delete_user(user_name)

Delete user

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_user_delete import Dbv0037ResponseUserDelete
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
        api_response = api_instance.slurmdbd_delete_user(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_user: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_delete_user.ApiResponseFor200) | Delete user
default | [ApiResponseForDefault](#slurmdbd_delete_user.ApiResponseForDefault) | User not found or unable to delete user

#### slurmdbd_delete_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseUserDelete**](../../models/Dbv0037ResponseUserDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseUserDelete**](../../models/Dbv0037ResponseUserDelete.md) |  | 


#### slurmdbd_delete_user.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_delete_wckey**
<a id="slurmdbd_delete_wckey"></a>
> Dbv0037ResponseWckeyDelete slurmdbd_delete_wckey(wckey)

Delete wckey

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_wckey_delete import Dbv0037ResponseWckeyDelete
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
        api_response = api_instance.slurmdbd_delete_wckey(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_delete_wckey: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_delete_wckey.ApiResponseFor200) | Delete wckey
default | [ApiResponseForDefault](#slurmdbd_delete_wckey.ApiResponseForDefault) | wckey not found or unable to delete wckey

#### slurmdbd_delete_wckey.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseWckeyDelete**](../../models/Dbv0037ResponseWckeyDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseWckeyDelete**](../../models/Dbv0037ResponseWckeyDelete.md) |  | 


#### slurmdbd_delete_wckey.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_diag**
<a id="slurmdbd_diag"></a>
> Dbv0037Diag slurmdbd_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_diag import Dbv0037Diag
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
        api_response = api_instance.slurmdbd_diag()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_diag: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_diag.ApiResponseFor200) | Dictionary of statistics
default | [ApiResponseForDefault](#slurmdbd_diag.ApiResponseForDefault) | Unable to query diagnostics

#### slurmdbd_diag.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037Diag**](../../models/Dbv0037Diag.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037Diag**](../../models/Dbv0037Diag.md) |  | 


#### slurmdbd_diag.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_account**
<a id="slurmdbd_get_account"></a>
> Dbv0037AccountInfo slurmdbd_get_account(account_name)

Get account info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_account_info import Dbv0037AccountInfo
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
        # Get account info
        api_response = api_instance.slurmdbd_get_account(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_account: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_get_account.ApiResponseFor200) | List of accounts
default | [ApiResponseForDefault](#slurmdbd_get_account.ApiResponseForDefault) | Account not found

#### slurmdbd_get_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AccountInfo**](../../models/Dbv0037AccountInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AccountInfo**](../../models/Dbv0037AccountInfo.md) |  | 


#### slurmdbd_get_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_accounts**
<a id="slurmdbd_get_accounts"></a>
> Dbv0037AccountInfo slurmdbd_get_accounts()

Get account list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_account_info import Dbv0037AccountInfo
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
        # Get account list
        api_response = api_instance.slurmdbd_get_accounts()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_accounts: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_get_accounts.ApiResponseFor200) | List of accounts
default | [ApiResponseForDefault](#slurmdbd_get_accounts.ApiResponseForDefault) | Account not found

#### slurmdbd_get_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AccountInfo**](../../models/Dbv0037AccountInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AccountInfo**](../../models/Dbv0037AccountInfo.md) |  | 


#### slurmdbd_get_accounts.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_association**
<a id="slurmdbd_get_association"></a>
> Dbv0037AssociationsInfo slurmdbd_get_association()

Get association info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_associations_info import Dbv0037AssociationsInfo
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
        api_response = api_instance.slurmdbd_get_association(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_association: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_get_association.ApiResponseFor200) | List of associations
default | [ApiResponseForDefault](#slurmdbd_get_association.ApiResponseForDefault) | Association not found

#### slurmdbd_get_association.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AssociationsInfo**](../../models/Dbv0037AssociationsInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AssociationsInfo**](../../models/Dbv0037AssociationsInfo.md) |  | 


#### slurmdbd_get_association.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_associations**
<a id="slurmdbd_get_associations"></a>
> Dbv0037AssociationsInfo slurmdbd_get_associations()

Get association list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_associations_info import Dbv0037AssociationsInfo
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
        # Get association list
        api_response = api_instance.slurmdbd_get_associations()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_associations: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_get_associations.ApiResponseFor200) | List of associations
default | [ApiResponseForDefault](#slurmdbd_get_associations.ApiResponseForDefault) | Association not found

#### slurmdbd_get_associations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AssociationsInfo**](../../models/Dbv0037AssociationsInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AssociationsInfo**](../../models/Dbv0037AssociationsInfo.md) |  | 


#### slurmdbd_get_associations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_cluster**
<a id="slurmdbd_get_cluster"></a>
> Dbv0037ClusterInfo slurmdbd_get_cluster(cluster_name)

Get cluster info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_cluster_info import Dbv0037ClusterInfo
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
        api_response = api_instance.slurmdbd_get_cluster(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_cluster: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_get_cluster.ApiResponseFor200) | Cluster information
default | [ApiResponseForDefault](#slurmdbd_get_cluster.ApiResponseForDefault) | Cluster not found

#### slurmdbd_get_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ClusterInfo**](../../models/Dbv0037ClusterInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ClusterInfo**](../../models/Dbv0037ClusterInfo.md) |  | 


#### slurmdbd_get_cluster.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_clusters**
<a id="slurmdbd_get_clusters"></a>
> Dbv0037ClusterInfo slurmdbd_get_clusters()

Get cluster list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_cluster_info import Dbv0037ClusterInfo
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
        api_response = api_instance.slurmdbd_get_clusters()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_clusters: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_get_clusters.ApiResponseFor200) | List of clusters
default | [ApiResponseForDefault](#slurmdbd_get_clusters.ApiResponseForDefault) | Cluster not found

#### slurmdbd_get_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ClusterInfo**](../../models/Dbv0037ClusterInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ClusterInfo**](../../models/Dbv0037ClusterInfo.md) |  | 


#### slurmdbd_get_clusters.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_db_config**
<a id="slurmdbd_get_db_config"></a>
> Dbv0037ConfigInfo slurmdbd_get_db_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_config_info import Dbv0037ConfigInfo
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
        api_response = api_instance.slurmdbd_get_db_config()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_db_config: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_get_db_config.ApiResponseFor200) | slurmdbd configuration
default | [ApiResponseForDefault](#slurmdbd_get_db_config.ApiResponseForDefault) | Unable to dump config

#### slurmdbd_get_db_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ConfigInfo**](../../models/Dbv0037ConfigInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ConfigInfo**](../../models/Dbv0037ConfigInfo.md) |  | 


#### slurmdbd_get_db_config.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_job**
<a id="slurmdbd_get_job"></a>
> Dbv0037JobInfo slurmdbd_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_job_info import Dbv0037JobInfo
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
        'job_id': 1,
    }
    try:
        # Get job info
        api_response = api_instance.slurmdbd_get_job(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_job: %s\n" % e)
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
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_get_job.ApiResponseFor200) | Job description
default | [ApiResponseForDefault](#slurmdbd_get_job.ApiResponseForDefault) | Unable to find job

#### slurmdbd_get_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037JobInfo**](../../models/Dbv0037JobInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037JobInfo**](../../models/Dbv0037JobInfo.md) |  | 


#### slurmdbd_get_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_jobs**
<a id="slurmdbd_get_jobs"></a>
> Dbv0037JobInfo slurmdbd_get_jobs()

Get job list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_job_info import Dbv0037JobInfo
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
        api_response = api_instance.slurmdbd_get_jobs(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_jobs: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_get_jobs.ApiResponseFor200) | List of jobs
default | [ApiResponseForDefault](#slurmdbd_get_jobs.ApiResponseForDefault) | Unable to query jobs

#### slurmdbd_get_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037JobInfo**](../../models/Dbv0037JobInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037JobInfo**](../../models/Dbv0037JobInfo.md) |  | 


#### slurmdbd_get_jobs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_qos**
<a id="slurmdbd_get_qos"></a>
> Dbv0037QosInfo slurmdbd_get_qos()

Get QOS list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_qos_info import Dbv0037QosInfo
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
        # Get QOS list
        api_response = api_instance.slurmdbd_get_qos()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_qos: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_get_qos.ApiResponseFor200) | List of QOS&#x27;
default | [ApiResponseForDefault](#slurmdbd_get_qos.ApiResponseForDefault) | QOS not found

#### slurmdbd_get_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037QosInfo**](../../models/Dbv0037QosInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037QosInfo**](../../models/Dbv0037QosInfo.md) |  | 


#### slurmdbd_get_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_single_qos**
<a id="slurmdbd_get_single_qos"></a>
> Dbv0037QosInfo slurmdbd_get_single_qos(qos_name)

Get QOS info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_qos_info import Dbv0037QosInfo
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
        # Get QOS info
        api_response = api_instance.slurmdbd_get_single_qos(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_single_qos: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_get_single_qos.ApiResponseFor200) | QOS information
default | [ApiResponseForDefault](#slurmdbd_get_single_qos.ApiResponseForDefault) | QOS not found

#### slurmdbd_get_single_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037QosInfo**](../../models/Dbv0037QosInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037QosInfo**](../../models/Dbv0037QosInfo.md) |  | 


#### slurmdbd_get_single_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_tres**
<a id="slurmdbd_get_tres"></a>
> Dbv0037TresInfo slurmdbd_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_tres_info import Dbv0037TresInfo
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
        api_response = api_instance.slurmdbd_get_tres()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_tres: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_get_tres.ApiResponseFor200) | List of TRES
default | [ApiResponseForDefault](#slurmdbd_get_tres.ApiResponseForDefault) | Unable to retrieve TRES

#### slurmdbd_get_tres.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037TresInfo**](../../models/Dbv0037TresInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037TresInfo**](../../models/Dbv0037TresInfo.md) |  | 


#### slurmdbd_get_tres.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_user**
<a id="slurmdbd_get_user"></a>
> Dbv0037UserInfo slurmdbd_get_user(user_name)

Get user info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_user_info import Dbv0037UserInfo
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
        # Get user info
        api_response = api_instance.slurmdbd_get_user(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_user: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_get_user.ApiResponseFor200) | List of users
default | [ApiResponseForDefault](#slurmdbd_get_user.ApiResponseForDefault) | User not found

#### slurmdbd_get_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037UserInfo**](../../models/Dbv0037UserInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037UserInfo**](../../models/Dbv0037UserInfo.md) |  | 


#### slurmdbd_get_user.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_users**
<a id="slurmdbd_get_users"></a>
> Dbv0037UserInfo slurmdbd_get_users()

Get user list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_user_info import Dbv0037UserInfo
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
        # Get user list
        api_response = api_instance.slurmdbd_get_users()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_users: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_get_users.ApiResponseFor200) | List of users
default | [ApiResponseForDefault](#slurmdbd_get_users.ApiResponseForDefault) | User not found

#### slurmdbd_get_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037UserInfo**](../../models/Dbv0037UserInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037UserInfo**](../../models/Dbv0037UserInfo.md) |  | 


#### slurmdbd_get_users.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_wckey**
<a id="slurmdbd_get_wckey"></a>
> Dbv0037WckeyInfo slurmdbd_get_wckey(wckey)

Get wckey info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_wckey_info import Dbv0037WckeyInfo
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
        api_response = api_instance.slurmdbd_get_wckey(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_wckey: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdbd_get_wckey.ApiResponseFor200) | List of wckey
default | [ApiResponseForDefault](#slurmdbd_get_wckey.ApiResponseForDefault) | wckey not found

#### slurmdbd_get_wckey.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037WckeyInfo**](../../models/Dbv0037WckeyInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037WckeyInfo**](../../models/Dbv0037WckeyInfo.md) |  | 


#### slurmdbd_get_wckey.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_get_wckeys**
<a id="slurmdbd_get_wckeys"></a>
> Dbv0037WckeyInfo slurmdbd_get_wckeys()

Get wckey list

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_wckey_info import Dbv0037WckeyInfo
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
        api_response = api_instance.slurmdbd_get_wckeys()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_get_wckeys: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_get_wckeys.ApiResponseFor200) | List of wckeys
default | [ApiResponseForDefault](#slurmdbd_get_wckeys.ApiResponseForDefault) | wckey not found

#### slurmdbd_get_wckeys.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037WckeyInfo**](../../models/Dbv0037WckeyInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037WckeyInfo**](../../models/Dbv0037WckeyInfo.md) |  | 


#### slurmdbd_get_wckeys.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_set_db_config**
<a id="slurmdbd_set_db_config"></a>
> Dbv0037ConfigResponse slurmdbd_set_db_config()

Load all configuration information

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_config_response import Dbv0037ConfigResponse
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
        # Load all configuration information
        api_response = api_instance.slurmdbd_set_db_config()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_set_db_config: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_set_db_config.ApiResponseFor200) | Load config
default | [ApiResponseForDefault](#slurmdbd_set_db_config.ApiResponseForDefault) | Unable to set config

#### slurmdbd_set_db_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ConfigResponse**](../../models/Dbv0037ConfigResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ConfigResponse**](../../models/Dbv0037ConfigResponse.md) |  | 


#### slurmdbd_set_db_config.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_update_account**
<a id="slurmdbd_update_account"></a>
> Dbv0037AccountResponse slurmdbd_update_account()

Update accounts

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_account_response import Dbv0037AccountResponse
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
        # Update accounts
        api_response = api_instance.slurmdbd_update_account()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_account: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_update_account.ApiResponseFor200) | Add/update list of accounts
default | [ApiResponseForDefault](#slurmdbd_update_account.ApiResponseForDefault) | Unable to add or update accounts

#### slurmdbd_update_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AccountResponse**](../../models/Dbv0037AccountResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037AccountResponse**](../../models/Dbv0037AccountResponse.md) |  | 


#### slurmdbd_update_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_update_associations**
<a id="slurmdbd_update_associations"></a>
> Dbv0037ResponseAssociations slurmdbd_update_associations()

Set associations info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_associations import Dbv0037ResponseAssociations
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
        # Set associations info
        api_response = api_instance.slurmdbd_update_associations()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_associations: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_update_associations.ApiResponseFor200) | status of associations update
default | [ApiResponseForDefault](#slurmdbd_update_associations.ApiResponseForDefault) | Unable to update associations

#### slurmdbd_update_associations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseAssociations**](../../models/Dbv0037ResponseAssociations.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseAssociations**](../../models/Dbv0037ResponseAssociations.md) |  | 


#### slurmdbd_update_associations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_update_tres**
<a id="slurmdbd_update_tres"></a>
> Dbv0037ResponseTres slurmdbd_update_tres()

Set TRES info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_tres import Dbv0037ResponseTres
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
        # Set TRES info
        api_response = api_instance.slurmdbd_update_tres()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_tres: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_update_tres.ApiResponseFor200) | List of TRES
default | [ApiResponseForDefault](#slurmdbd_update_tres.ApiResponseForDefault) | Unable to update TRES

#### slurmdbd_update_tres.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseTres**](../../models/Dbv0037ResponseTres.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseTres**](../../models/Dbv0037ResponseTres.md) |  | 


#### slurmdbd_update_tres.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdbd_update_users**
<a id="slurmdbd_update_users"></a>
> Dbv0037ResponseUserUpdate slurmdbd_update_users()

Update user

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0037_response_user_update import Dbv0037ResponseUserUpdate
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
        # Update user
        api_response = api_instance.slurmdbd_update_users()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdbd_update_users: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdbd_update_users.ApiResponseFor200) | Update users
default | [ApiResponseForDefault](#slurmdbd_update_users.ApiResponseForDefault) | User not found or not able to update user

#### slurmdbd_update_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseUserUpdate**](../../models/Dbv0037ResponseUserUpdate.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0037ResponseUserUpdate**](../../models/Dbv0037ResponseUserUpdate.md) |  | 


#### slurmdbd_update_users.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

