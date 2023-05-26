<a id="__pageTop"></a>
# slurmrestapi.apis.tags.slurm_api.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurm_v0039_cancel_job**](#slurm_v0039_cancel_job) | **delete** /slurm/v0.0.39/job/{job_id} | cancel or signal job
[**slurm_v0039_delete_node**](#slurm_v0039_delete_node) | **delete** /slurm/v0.0.39/node/{node_name} | delete node
[**slurm_v0039_diag**](#slurm_v0039_diag) | **get** /slurm/v0.0.39/diag | get diagnostics
[**slurm_v0039_get_job**](#slurm_v0039_get_job) | **get** /slurm/v0.0.39/job/{job_id} | get job info
[**slurm_v0039_get_jobs**](#slurm_v0039_get_jobs) | **get** /slurm/v0.0.39/jobs | get list of jobs
[**slurm_v0039_get_node**](#slurm_v0039_get_node) | **get** /slurm/v0.0.39/node/{node_name} | get node info
[**slurm_v0039_get_nodes**](#slurm_v0039_get_nodes) | **get** /slurm/v0.0.39/nodes | get all node info
[**slurm_v0039_get_partition**](#slurm_v0039_get_partition) | **get** /slurm/v0.0.39/partition/{partition_name} | get partition info
[**slurm_v0039_get_partitions**](#slurm_v0039_get_partitions) | **get** /slurm/v0.0.39/partitions | get all partition info
[**slurm_v0039_get_reservation**](#slurm_v0039_get_reservation) | **get** /slurm/v0.0.39/reservation/{reservation_name} | get reservation info
[**slurm_v0039_get_reservations**](#slurm_v0039_get_reservations) | **get** /slurm/v0.0.39/reservations | get all reservation info
[**slurm_v0039_ping**](#slurm_v0039_ping) | **get** /slurm/v0.0.39/ping | ping test
[**slurm_v0039_slurmctld_get_licenses**](#slurm_v0039_slurmctld_get_licenses) | **get** /slurm/v0.0.39/licenses | get all Slurm tracked license info
[**slurm_v0039_submit_job**](#slurm_v0039_submit_job) | **post** /slurm/v0.0.39/job/submit | submit new job
[**slurm_v0039_update_job**](#slurm_v0039_update_job) | **post** /slurm/v0.0.39/job/{job_id} | update job
[**slurm_v0039_update_node**](#slurm_v0039_update_node) | **post** /slurm/v0.0.39/node/{node_name} | update node properties
[**slurmdb_v0039_add_clusters**](#slurmdb_v0039_add_clusters) | **post** /slurmdb/v0.0.39/clusters | Add clusters
[**slurmdb_v0039_add_wckeys**](#slurmdb_v0039_add_wckeys) | **post** /slurmdb/v0.0.39/wckeys | Add wckeys
[**slurmdb_v0039_delete_account**](#slurmdb_v0039_delete_account) | **delete** /slurmdb/v0.0.39/account/{account_name} | Delete account
[**slurmdb_v0039_delete_association**](#slurmdb_v0039_delete_association) | **delete** /slurmdb/v0.0.39/association | Delete association
[**slurmdb_v0039_delete_associations**](#slurmdb_v0039_delete_associations) | **delete** /slurmdb/v0.0.39/associations | Delete associations
[**slurmdb_v0039_delete_cluster**](#slurmdb_v0039_delete_cluster) | **delete** /slurmdb/v0.0.39/cluster/{cluster_name} | Delete cluster
[**slurmdb_v0039_delete_qos**](#slurmdb_v0039_delete_qos) | **delete** /slurmdb/v0.0.39/qos/{qos_name} | Delete QOS
[**slurmdb_v0039_delete_user**](#slurmdb_v0039_delete_user) | **delete** /slurmdb/v0.0.39/user/{user_name} | Delete user
[**slurmdb_v0039_delete_wckey**](#slurmdb_v0039_delete_wckey) | **delete** /slurmdb/v0.0.39/wckey/{wckey} | Delete wckey
[**slurmdb_v0039_diag**](#slurmdb_v0039_diag) | **get** /slurmdb/v0.0.39/diag | Get slurmdb diagnostics
[**slurmdb_v0039_get_account**](#slurmdb_v0039_get_account) | **get** /slurmdb/v0.0.39/account/{account_name} | Get account info
[**slurmdb_v0039_get_accounts**](#slurmdb_v0039_get_accounts) | **get** /slurmdb/v0.0.39/accounts | Get account list
[**slurmdb_v0039_get_association**](#slurmdb_v0039_get_association) | **get** /slurmdb/v0.0.39/association | Get association info
[**slurmdb_v0039_get_associations**](#slurmdb_v0039_get_associations) | **get** /slurmdb/v0.0.39/associations | Get association list
[**slurmdb_v0039_get_cluster**](#slurmdb_v0039_get_cluster) | **get** /slurmdb/v0.0.39/cluster/{cluster_name} | Get cluster info
[**slurmdb_v0039_get_clusters**](#slurmdb_v0039_get_clusters) | **get** /slurmdb/v0.0.39/clusters | Get cluster list
[**slurmdb_v0039_get_config**](#slurmdb_v0039_get_config) | **get** /slurmdb/v0.0.39/config | Dump all configuration information
[**slurmdb_v0039_get_job**](#slurmdb_v0039_get_job) | **get** /slurmdb/v0.0.39/job/{job_id} | Get job info
[**slurmdb_v0039_get_jobs**](#slurmdb_v0039_get_jobs) | **get** /slurmdb/v0.0.39/jobs | Get job list
[**slurmdb_v0039_get_qos**](#slurmdb_v0039_get_qos) | **get** /slurmdb/v0.0.39/qos | Get QOS list
[**slurmdb_v0039_get_single_qos**](#slurmdb_v0039_get_single_qos) | **get** /slurmdb/v0.0.39/qos/{qos_name} | Get QOS info
[**slurmdb_v0039_get_tres**](#slurmdb_v0039_get_tres) | **get** /slurmdb/v0.0.39/tres | Get TRES info
[**slurmdb_v0039_get_user**](#slurmdb_v0039_get_user) | **get** /slurmdb/v0.0.39/user/{user_name} | Get user info
[**slurmdb_v0039_get_users**](#slurmdb_v0039_get_users) | **get** /slurmdb/v0.0.39/users | Get user list
[**slurmdb_v0039_get_wckey**](#slurmdb_v0039_get_wckey) | **get** /slurmdb/v0.0.39/wckey/{wckey} | Get wckey info
[**slurmdb_v0039_get_wckeys**](#slurmdb_v0039_get_wckeys) | **get** /slurmdb/v0.0.39/wckeys | Get wckey list
[**slurmdb_v0039_set_config**](#slurmdb_v0039_set_config) | **post** /slurmdb/v0.0.39/config | Load all configuration information
[**slurmdb_v0039_update_accounts**](#slurmdb_v0039_update_accounts) | **post** /slurmdb/v0.0.39/accounts | Update accounts
[**slurmdb_v0039_update_associations**](#slurmdb_v0039_update_associations) | **post** /slurmdb/v0.0.39/associations | Set associations info
[**slurmdb_v0039_update_qos**](#slurmdb_v0039_update_qos) | **post** /slurmdb/v0.0.39/qos | Set QOS info
[**slurmdb_v0039_update_tres**](#slurmdb_v0039_update_tres) | **post** /slurmdb/v0.0.39/tres | Set TRES info
[**slurmdb_v0039_update_users**](#slurmdb_v0039_update_users) | **post** /slurmdb/v0.0.39/users | Update user

# **slurm_v0039_cancel_job**
<a id="slurm_v0039_cancel_job"></a>
> Status slurm_v0039_cancel_job(job_id)

cancel or signal job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_cancel_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_cancel_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'job_id': "job_id_example",
    }
    query_params = {
        'signal': "HUP",
    }
    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0039_cancel_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_cancel_job: %s\n" % e)
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
signal | SignalSchema | | optional


# SignalSchema

POSIX signal name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | POSIX signal name | must be one of ["HUP", "INT", "QUIT", "ABRT", "KILL", "ALRM", "TERM", "USR1", "USR2", "URG", "CONT", "STOP", "TSTP", "TTIN", "TTOU", ] 

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
200 | [ApiResponseFor200](#slurm_v0039_cancel_job.ApiResponseFor200) | job cancelled or sent signal
default | [ApiResponseForDefault](#slurm_v0039_cancel_job.ApiResponseForDefault) | Job cancel request failed

#### slurm_v0039_cancel_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurm_v0039_cancel_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_delete_node**
<a id="slurm_v0039_delete_node"></a>
> Status slurm_v0039_delete_node(node_name)

delete node

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        # delete node
        api_response = api_instance.slurm_v0039_delete_node(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_delete_node: %s\n" % e)
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
200 | [ApiResponseFor200](#slurm_v0039_delete_node.ApiResponseFor200) | node deleted
default | [ApiResponseForDefault](#slurm_v0039_delete_node.ApiResponseForDefault) | node delete request failed

#### slurm_v0039_delete_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurm_v0039_delete_node.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_diag**
<a id="slurm_v0039_diag"></a>
> V0039Diag slurm_v0039_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_diag import V0039Diag
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_diag()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_diag: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0039_diag.ApiResponseFor200) | diagnostic results
default | [ApiResponseForDefault](#slurm_v0039_diag.ApiResponseForDefault) | unable to request ping test

#### slurm_v0039_diag.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039Diag**](../../models/V0039Diag.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039Diag**](../../models/V0039Diag.md) |  | 


#### slurm_v0039_diag.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_get_job**
<a id="slurm_v0039_get_job"></a>
> V0039JobsResponse slurm_v0039_get_job(job_id)

get job info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0039_jobs_response import V0039JobsResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_get_job(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_job: %s\n" % e)
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
200 | [ApiResponseFor200](#slurm_v0039_get_job.ApiResponseFor200) | job(s) information
default | [ApiResponseForDefault](#slurm_v0039_get_job.ApiResponseForDefault) | job matching JobId not found

#### slurm_v0039_get_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobsResponse**](../../models/V0039JobsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobsResponse**](../../models/V0039JobsResponse.md) |  | 


#### slurm_v0039_get_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_get_jobs**
<a id="slurm_v0039_get_jobs"></a>
> V0039JobsResponse slurm_v0039_get_jobs()

get list of jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0039_jobs_response import V0039JobsResponse
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_get_jobs(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_jobs: %s\n" % e)
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
200 | [ApiResponseFor200](#slurm_v0039_get_jobs.ApiResponseFor200) | job(s) information
default | [ApiResponseForDefault](#slurm_v0039_get_jobs.ApiResponseForDefault) | job not found

#### slurm_v0039_get_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobsResponse**](../../models/V0039JobsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobsResponse**](../../models/V0039JobsResponse.md) |  | 


#### slurm_v0039_get_jobs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_get_node**
<a id="slurm_v0039_get_node"></a>
> V0039NodesResponse slurm_v0039_get_node(node_name)

get node info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_nodes_response import V0039NodesResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_get_node(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_node: %s\n" % e)
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
200 | [ApiResponseFor200](#slurm_v0039_get_node.ApiResponseFor200) | node information
default | [ApiResponseForDefault](#slurm_v0039_get_node.ApiResponseForDefault) | node not found

#### slurm_v0039_get_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039NodesResponse**](../../models/V0039NodesResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039NodesResponse**](../../models/V0039NodesResponse.md) |  | 


#### slurm_v0039_get_node.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_get_nodes**
<a id="slurm_v0039_get_nodes"></a>
> V0039NodesResponse slurm_v0039_get_nodes()

get all node info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_nodes_response import V0039NodesResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_get_nodes(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_nodes: %s\n" % e)
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
200 | [ApiResponseFor200](#slurm_v0039_get_nodes.ApiResponseFor200) | node information
default | [ApiResponseForDefault](#slurm_v0039_get_nodes.ApiResponseForDefault) | no nodes in cluster

#### slurm_v0039_get_nodes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039NodesResponse**](../../models/V0039NodesResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039NodesResponse**](../../models/V0039NodesResponse.md) |  | 


#### slurm_v0039_get_nodes.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_get_partition**
<a id="slurm_v0039_get_partition"></a>
> V0039PartitionsResponse slurm_v0039_get_partition(partition_name)

get partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_partitions_response import V0039PartitionsResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_get_partition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_partition: %s\n" % e)

    # example passing only optional values
    path_params = {
        'partition_name': "partition_name_example",
    }
    query_params = {
        'update_time': 1,
    }
    try:
        # get partition info
        api_response = api_instance.slurm_v0039_get_partition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_partition: %s\n" % e)
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
200 | [ApiResponseFor200](#slurm_v0039_get_partition.ApiResponseFor200) | partition information
default | [ApiResponseForDefault](#slurm_v0039_get_partition.ApiResponseForDefault) | no partitions found

#### slurm_v0039_get_partition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039PartitionsResponse**](../../models/V0039PartitionsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039PartitionsResponse**](../../models/V0039PartitionsResponse.md) |  | 


#### slurm_v0039_get_partition.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_get_partitions**
<a id="slurm_v0039_get_partitions"></a>
> V0039PartitionsResponse slurm_v0039_get_partitions()

get all partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_partitions_response import V0039PartitionsResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_get_partitions(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_partitions: %s\n" % e)
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
200 | [ApiResponseFor200](#slurm_v0039_get_partitions.ApiResponseFor200) | partition information
default | [ApiResponseForDefault](#slurm_v0039_get_partitions.ApiResponseForDefault) | no partitions found

#### slurm_v0039_get_partitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039PartitionsResponse**](../../models/V0039PartitionsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039PartitionsResponse**](../../models/V0039PartitionsResponse.md) |  | 


#### slurm_v0039_get_partitions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_get_reservation**
<a id="slurm_v0039_get_reservation"></a>
> V0039ReservationsResponse slurm_v0039_get_reservation(reservation_name)

get reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_reservations_response import V0039ReservationsResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_get_reservation(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_reservation: %s\n" % e)

    # example passing only optional values
    path_params = {
        'reservation_name': "reservation_name_example",
    }
    query_params = {
        'update_time': 1,
    }
    try:
        # get reservation info
        api_response = api_instance.slurm_v0039_get_reservation(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_reservation: %s\n" % e)
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
200 | [ApiResponseFor200](#slurm_v0039_get_reservation.ApiResponseFor200) | reservation information
default | [ApiResponseForDefault](#slurm_v0039_get_reservation.ApiResponseForDefault) | no reservations found

#### slurm_v0039_get_reservation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039ReservationsResponse**](../../models/V0039ReservationsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039ReservationsResponse**](../../models/V0039ReservationsResponse.md) |  | 


#### slurm_v0039_get_reservation.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_get_reservations**
<a id="slurm_v0039_get_reservations"></a>
> V0039ReservationsResponse slurm_v0039_get_reservations()

get all reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_reservations_response import V0039ReservationsResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_get_reservations(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_get_reservations: %s\n" % e)
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
200 | [ApiResponseFor200](#slurm_v0039_get_reservations.ApiResponseFor200) | reservation information
default | [ApiResponseForDefault](#slurm_v0039_get_reservations.ApiResponseForDefault) | no reservations found

#### slurm_v0039_get_reservations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039ReservationsResponse**](../../models/V0039ReservationsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039ReservationsResponse**](../../models/V0039ReservationsResponse.md) |  | 


#### slurm_v0039_get_reservations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_ping**
<a id="slurm_v0039_ping"></a>
> V0039Pings slurm_v0039_ping()

ping test

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0039_pings import V0039Pings
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_ping()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_ping: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0039_ping.ApiResponseFor200) | results of ping test
default | [ApiResponseForDefault](#slurm_v0039_ping.ApiResponseForDefault) | unable to request ping test

#### slurm_v0039_ping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039Pings**](../../models/V0039Pings.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039Pings**](../../models/V0039Pings.md) |  | 


#### slurm_v0039_ping.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_slurmctld_get_licenses**
<a id="slurm_v0039_slurmctld_get_licenses"></a>
> V0039LicensesInfo slurm_v0039_slurmctld_get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0039_licenses_info import V0039LicensesInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurm_v0039_slurmctld_get_licenses()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_slurmctld_get_licenses: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0039_slurmctld_get_licenses.ApiResponseFor200) | results of get all licenses
default | [ApiResponseForDefault](#slurm_v0039_slurmctld_get_licenses.ApiResponseForDefault) | unable to request licenses

#### slurm_v0039_slurmctld_get_licenses.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039LicensesInfo**](../../models/V0039LicensesInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039LicensesInfo**](../../models/V0039LicensesInfo.md) |  | 


#### slurm_v0039_slurmctld_get_licenses.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_submit_job**
<a id="slurm_v0039_submit_job"></a>
> V0039JobSubmissionResponse slurm_v0039_submit_job(v0039_job_submission)

submit new job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_job_submission_response import V0039JobSubmissionResponse
from slurmrestapi.model.v0039_job_submission import V0039JobSubmission
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = V0039JobSubmission(None)
    try:
        # submit new job
        api_response = api_instance.slurm_v0039_submit_job(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_submit_job: %s\n" % e)
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
[**V0039JobSubmission**](../../models/V0039JobSubmission.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobSubmission**](../../models/V0039JobSubmission.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurm_v0039_submit_job.ApiResponseFor200) | job submitted
default | [ApiResponseForDefault](#slurm_v0039_submit_job.ApiResponseForDefault) | job rejected

#### slurm_v0039_submit_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobSubmissionResponse**](../../models/V0039JobSubmissionResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobSubmissionResponse**](../../models/V0039JobSubmissionResponse.md) |  | 


#### slurm_v0039_submit_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_update_job**
<a id="slurm_v0039_update_job"></a>
> V0039JobUpdateResponse slurm_v0039_update_job(job_idv0039_job_desc_msg)

update job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.v0039_job_desc_msg import V0039JobDescMsg
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_job_update_response import V0039JobUpdateResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
    body = V0039JobDescMsg(
        account="account_example",
        account_gather_frequency="account_gather_frequency_example",
        admin_comment="admin_comment_example",
        allocation_node_list="allocation_node_list_example",
        allocation_node_port=1,
        argv=V0039StringArray([
            "argv_example"
        ]),
        array="array_example",
        batch_features="batch_features_example",
        begin_time=1,
        flags=[
            "KILL_INVALID_DEPENDENCY"
        ],
        burst_buffer="burst_buffer_example",
        clusters="clusters_example",
        cluster_constraint="cluster_constraint_example",
        comment="comment_example",
        contiguous=True,
        container="container_example",
        container_id="container_id_example",
        core_specification=1,
        thread_specification=1,
        cpu_binding="cpu_binding_example",
        cpu_binding_flags=[
            "VERBOSE"
        ],
        cpu_frequency="cpu_frequency_example",
        cpus_per_tres="cpus_per_tres_example",
        crontab=V0039CronEntry(
            flags=[
                "WILD_MINUTE"
            ],
            minute="minute_example",
            hour="hour_example",
            day_of_month="day_of_month_example",
            month="month_example",
            day_of_week="day_of_week_example",
            specification="specification_example",
            command="command_example",
            line=dict(
                end=1,
            ),
        ),
        deadline=1,
        delay_boot=1,
        dependency="dependency_example",
        end_time=1,
,
,
        extra="extra_example",
        constraints="constraints_example",
        group_id="group_id_example",
        hetjob_group=1,
        immediate=True,
        job_id=1,
        kill_on_node_fail=True,
        licenses="licenses_example",
        mail_type=[
            "BEGIN"
        ],
        mail_user="mail_user_example",
        mcs_label="mcs_label_example",
        memory_binding="memory_binding_example",
        memory_binding_type=[
            "VERBOSE"
        ],
        memory_per_tres="memory_per_tres_example",
        name="name_example",
        network="network_example",
        nice=1,
        tasks=1,
        open_mode=[
            "APPEND"
        ],
        reserve_ports=1,
        overcommit=True,
        partition="partition_example",
        distribution_plane_size=1,
        power_flags=[
            "EQUAL_POWER"
        ],
        prefer="prefer_example",
        priority=1,
        profile=[
            "NOT_SET"
        ],
        qos="qos_example",
        reboot=True,
,
        requeue=True,
        reservation="reservation_example",
        script="script_example",
        shared=[
            "none"
        ],
        exclusive=V0039JobExclusive([
            "true"
        ]),
        site_factor=1,
,
        distribution="distribution_example",
        time_limit=V0039Uint32NoVal(
            set=False,
            infinite=True,
            number=1,
        ),
,
        tres_bind="tres_bind_example",
        tres_freq="tres_freq_example",
        tres_per_job="tres_per_job_example",
        tres_per_node="tres_per_node_example",
        tres_per_socket="tres_per_socket_example",
        tres_per_task="tres_per_task_example",
        user_id="user_id_example",
        wait_all_nodes=True,
        kill_warning_flags=[
            "BATCH_JOB"
        ],
        kill_warning_signal="kill_warning_signal_example",
        kill_warning_delay=V0039Uint16NoVal(),
        current_working_directory="current_working_directory_example",
        cpus_per_task=1,
        minimum_cpus=1,
        maximum_cpus=1,
        nodes="nodes_example",
        minimum_nodes=1,
        maximum_nodes=1,
        minimum_boards_per_node=1,
        minimum_sockets_per_board=1,
        sockets_per_node=1,
        threads_per_core=1,
        tasks_per_node=1,
        tasks_per_socket=1,
        tasks_per_core=1,
        tasks_per_board=1,
        ntasks_per_tres=1,
        minimum_cpus_per_node=1,
        memory_per_cpu=V0039Uint64NoVal(),
        memory_per_node=V0039Uint64NoVal(),
        temporary_disk_per_node=1,
        selinux_context="selinux_context_example",
        required_switches=V0039Uint32NoVal(),
        standard_error="standard_error_example",
        standard_input="standard_input_example",
        standard_output="standard_output_example",
        wait_for_switch=1,
        wckey="wckey_example",
        x11=[
            "FORWARD_ALL_NODES"
        ],
        x11_magic_cookie="x11_magic_cookie_example",
        x11_target_host="x11_target_host_example",
        x11_target_port=1,
    )
    try:
        # update job
        api_response = api_instance.slurm_v0039_update_job(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_update_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobDescMsg**](../../models/V0039JobDescMsg.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobDescMsg**](../../models/V0039JobDescMsg.md) |  | 


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
200 | [ApiResponseFor200](#slurm_v0039_update_job.ApiResponseFor200) | job updated
default | [ApiResponseForDefault](#slurm_v0039_update_job.ApiResponseForDefault) | job update failed

#### slurm_v0039_update_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobUpdateResponse**](../../models/V0039JobUpdateResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039JobUpdateResponse**](../../models/V0039JobUpdateResponse.md) |  | 


#### slurm_v0039_update_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurm_v0039_update_node**
<a id="slurm_v0039_update_node"></a>
> Status slurm_v0039_update_node(node_namev0039_update_node_msg)

update node properties

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.v0039_update_node_msg import V0039UpdateNodeMsg
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
    body = V0039UpdateNodeMsg(
        comment="comment_example",
        cpu_bind=1,
        extra="extra_example",
        features=V0039CsvList([
            "features_example"
        ]),
,
        gres="gres_example",
,
,
,
        state=[
            "INVALID"
        ],
        reason="reason_example",
        reason_uid="reason_uid_example",
        resume_after=V0039Uint32NoVal(
            set=False,
            infinite=True,
            number=1,
        ),
,
    )
    try:
        # update node properties
        api_response = api_instance.slurm_v0039_update_node(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0039_update_node: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXYaml] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/x-yaml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039UpdateNodeMsg**](../../models/V0039UpdateNodeMsg.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V0039UpdateNodeMsg**](../../models/V0039UpdateNodeMsg.md) |  | 


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
200 | [ApiResponseFor200](#slurm_v0039_update_node.ApiResponseFor200) | node information
default | [ApiResponseForDefault](#slurm_v0039_update_node.ApiResponseForDefault) | node update failed

#### slurm_v0039_update_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurm_v0039_update_node.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_add_clusters**
<a id="slurmdb_v0039_add_clusters"></a>
> Status slurmdb_v0039_add_clusters(dbv0039_clusters_info)

Add clusters

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0039_clusters_info import Dbv0039ClustersInfo
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0039ClustersInfo(
        meta=Dbv0039Meta(
            plugin=dict(
                type="type_example",
                name="name_example",
            ),
            slurm=dict(
                version=dict(
                    major=1,
                    micro=1,
                    minor=1,
                ),
                release="release_example",
            ),
        ),
        errors=Dbv0039Errors([
            Dbv0039Error(
                error_number=1,
                error="error_example",
                source="source_example",
                description="description_example",
            )
        ]),
        warnings=Dbv0039Warnings([
            Dbv0039Warning(
                warning="warning_example",
                source="source_example",
                description="description_example",
            )
        ]),
        clusters=V0039ClusterRecList([
            V0039ClusterRec(
                controller=dict(
                    port=1,
                ),
                flags=[
                    "REGISTERING"
                ],
                name="name_example",
                nodes="nodes_example",
                select_plugin="select_plugin_example",
                associations=dict(
                    root=V0039AssocShort(
                        account="account_example",
                        cluster="cluster_example",
                        partition="partition_example",
                        user="user_example",
                    ),
                ),
                rpc_version=1,
                tres=V0039TresList([
                    V0039Tres(
                        type="type_example",
                        name="name_example",
                        id=1,
                        count=1,
                    )
                ]),
            )
        ]),
    )
    try:
        # Add clusters
        api_response = api_instance.slurmdb_v0039_add_clusters(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_add_clusters: %s\n" % e)
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
[**Dbv0039ClustersInfo**](../../models/Dbv0039ClustersInfo.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ClustersInfo**](../../models/Dbv0039ClustersInfo.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_add_clusters.ApiResponseFor200) | List of clusters
default | [ApiResponseForDefault](#slurmdb_v0039_add_clusters.ApiResponseForDefault) | Unable to add cluster

#### slurmdb_v0039_add_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_add_clusters.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_add_wckeys**
<a id="slurmdb_v0039_add_wckeys"></a>
> Status slurmdb_v0039_add_wckeys()

Add wckeys

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_wckey_info import Dbv0039WckeyInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    body = Dbv0039WckeyInfo(
        meta=Dbv0039Meta(
            plugin=dict(
                type="type_example",
                name="name_example",
            ),
            slurm=dict(
                version=dict(
                    major=1,
                    micro=1,
                    minor=1,
                ),
                release="release_example",
            ),
        ),
        errors=Dbv0039Errors([
            Dbv0039Error(
                error_number=1,
                error="error_example",
                source="source_example",
                description="description_example",
            )
        ]),
        wckeys=V0039WckeyList([
            V0039Wckey(
                accounting=V0039AccountingList([
                    V0039Accounting(
                        allocated=dict(
                            seconds=1,
                        ),
                        id=1,
                        start=1,
                        tres=V0039Tres(
                            type="type_example",
                            name="name_example",
                            id=1,
                            count=1,
                        ),
                    )
                ]),
                cluster="cluster_example",
                id=1,
                name="name_example",
                user="user_example",
                flags=[
                    "DELETED"
                ],
            )
        ]),
    )
    try:
        # Add wckeys
        api_response = api_instance.slurmdb_v0039_add_wckeys(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_add_wckeys: %s\n" % e)
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
[**Dbv0039WckeyInfo**](../../models/Dbv0039WckeyInfo.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039WckeyInfo**](../../models/Dbv0039WckeyInfo.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_add_wckeys.ApiResponseFor200) | List of wckeys
default | [ApiResponseForDefault](#slurmdb_v0039_add_wckeys.ApiResponseForDefault) | Unable to add wckey

#### slurmdb_v0039_add_wckeys.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_add_wckeys.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_delete_account**
<a id="slurmdb_v0039_delete_account"></a>
> Status slurmdb_v0039_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_delete_account(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_account: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_delete_account.ApiResponseFor200) | Delete account
default | [ApiResponseForDefault](#slurmdb_v0039_delete_account.ApiResponseForDefault) | Unable to delete account

#### slurmdb_v0039_delete_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_delete_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_delete_association**
<a id="slurmdb_v0039_delete_association"></a>
> Dbv0039ResponseAssociationsDelete slurmdb_v0039_delete_association()

Delete association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_response_associations_delete import Dbv0039ResponseAssociationsDelete
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_delete_association(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_association: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_delete_association.ApiResponseFor200) | Delete associations
default | [ApiResponseForDefault](#slurmdb_v0039_delete_association.ApiResponseForDefault) | Association not found or unable to delete association

#### slurmdb_v0039_delete_association.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ResponseAssociationsDelete**](../../models/Dbv0039ResponseAssociationsDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ResponseAssociationsDelete**](../../models/Dbv0039ResponseAssociationsDelete.md) |  | 


#### slurmdb_v0039_delete_association.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_delete_associations**
<a id="slurmdb_v0039_delete_associations"></a>
> Dbv0039ResponseAssociationsDelete slurmdb_v0039_delete_associations()

Delete associations

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_response_associations_delete import Dbv0039ResponseAssociationsDelete
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_delete_associations(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_associations: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_delete_associations.ApiResponseFor200) | Delete associations
default | [ApiResponseForDefault](#slurmdb_v0039_delete_associations.ApiResponseForDefault) | Associations not found or unable to delete association

#### slurmdb_v0039_delete_associations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ResponseAssociationsDelete**](../../models/Dbv0039ResponseAssociationsDelete.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ResponseAssociationsDelete**](../../models/Dbv0039ResponseAssociationsDelete.md) |  | 


#### slurmdb_v0039_delete_associations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_delete_cluster**
<a id="slurmdb_v0039_delete_cluster"></a>
> Status slurmdb_v0039_delete_cluster(cluster_name)

Delete cluster

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_delete_cluster(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_cluster: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_delete_cluster.ApiResponseFor200) | Delete cluster
default | [ApiResponseForDefault](#slurmdb_v0039_delete_cluster.ApiResponseForDefault) | Cluster not found or unable to delete cluster

#### slurmdb_v0039_delete_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_delete_cluster.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_delete_qos**
<a id="slurmdb_v0039_delete_qos"></a>
> Status slurmdb_v0039_delete_qos(qos_name)

Delete QOS

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_delete_qos(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_qos: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_delete_qos.ApiResponseFor200) | Delete qos
default | [ApiResponseForDefault](#slurmdb_v0039_delete_qos.ApiResponseForDefault) | Unable to delete QOS

#### slurmdb_v0039_delete_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_delete_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_delete_user**
<a id="slurmdb_v0039_delete_user"></a>
> Status slurmdb_v0039_delete_user(user_name)

Delete user

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_delete_user(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_user: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_delete_user.ApiResponseFor200) | User deleted
default | [ApiResponseForDefault](#slurmdb_v0039_delete_user.ApiResponseForDefault) | User not found or unable to delete user

#### slurmdb_v0039_delete_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_delete_user.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_delete_wckey**
<a id="slurmdb_v0039_delete_wckey"></a>
> Status slurmdb_v0039_delete_wckey(wckey)

Delete wckey

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_delete_wckey(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_delete_wckey: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_delete_wckey.ApiResponseFor200) | Delete wckey
default | [ApiResponseForDefault](#slurmdb_v0039_delete_wckey.ApiResponseForDefault) | wckey not found or unable to delete wckey

#### slurmdb_v0039_delete_wckey.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_delete_wckey.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_diag**
<a id="slurmdb_v0039_diag"></a>
> Dbv0039Diag slurmdb_v0039_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_diag import Dbv0039Diag
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_diag()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_diag: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_diag.ApiResponseFor200) | Dictionary of statistics
default | [ApiResponseForDefault](#slurmdb_v0039_diag.ApiResponseForDefault) | Unable to query diagnostics

#### slurmdb_v0039_diag.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039Diag**](../../models/Dbv0039Diag.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039Diag**](../../models/Dbv0039Diag.md) |  | 


#### slurmdb_v0039_diag.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_account**
<a id="slurmdb_v0039_get_account"></a>
> Dbv0039AccountInfo slurmdb_v0039_get_account(account_name)

Get account info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_account_info import Dbv0039AccountInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_account(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_account: %s\n" % e)

    # example passing only optional values
    path_params = {
        'account_name': "account_name_example",
    }
    query_params = {
        'with_deleted': "false",
    }
    try:
        # Get account info
        api_response = api_instance.slurmdb_v0039_get_account(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_account: %s\n" % e)
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
str,  | str,  |  | must be one of ["true", "false", ] if omitted the server will use the default value of "false"

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
200 | [ApiResponseFor200](#slurmdb_v0039_get_account.ApiResponseFor200) | List of accounts
default | [ApiResponseForDefault](#slurmdb_v0039_get_account.ApiResponseForDefault) | Account not found

#### slurmdb_v0039_get_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AccountInfo**](../../models/Dbv0039AccountInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AccountInfo**](../../models/Dbv0039AccountInfo.md) |  | 


#### slurmdb_v0039_get_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_accounts**
<a id="slurmdb_v0039_get_accounts"></a>
> Dbv0039AccountInfo slurmdb_v0039_get_accounts()

Get account list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_account_info import Dbv0039AccountInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        'with_deleted': "false",
    }
    try:
        # Get account list
        api_response = api_instance.slurmdb_v0039_get_accounts(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_accounts: %s\n" % e)
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
str,  | str,  |  | must be one of ["true", "false", ] if omitted the server will use the default value of "false"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_get_accounts.ApiResponseFor200) | List of accounts
default | [ApiResponseForDefault](#slurmdb_v0039_get_accounts.ApiResponseForDefault) | Account not found

#### slurmdb_v0039_get_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AccountInfo**](../../models/Dbv0039AccountInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AccountInfo**](../../models/Dbv0039AccountInfo.md) |  | 


#### slurmdb_v0039_get_accounts.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_association**
<a id="slurmdb_v0039_get_association"></a>
> Dbv0039AssociationsInfo slurmdb_v0039_get_association()

Get association info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_associations_info import Dbv0039AssociationsInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_association(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_association: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_get_association.ApiResponseFor200) | List of associations
default | [ApiResponseForDefault](#slurmdb_v0039_get_association.ApiResponseForDefault) | Association not found

#### slurmdb_v0039_get_association.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AssociationsInfo**](../../models/Dbv0039AssociationsInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AssociationsInfo**](../../models/Dbv0039AssociationsInfo.md) |  | 


#### slurmdb_v0039_get_association.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_associations**
<a id="slurmdb_v0039_get_associations"></a>
> Dbv0039AssociationsInfo slurmdb_v0039_get_associations()

Get association list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_associations_info import Dbv0039AssociationsInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_associations(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_associations: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_get_associations.ApiResponseFor200) | List of associations
default | [ApiResponseForDefault](#slurmdb_v0039_get_associations.ApiResponseForDefault) | Association not found

#### slurmdb_v0039_get_associations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AssociationsInfo**](../../models/Dbv0039AssociationsInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AssociationsInfo**](../../models/Dbv0039AssociationsInfo.md) |  | 


#### slurmdb_v0039_get_associations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_cluster**
<a id="slurmdb_v0039_get_cluster"></a>
> Dbv0039ClustersInfo slurmdb_v0039_get_cluster(cluster_name)

Get cluster info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0039_clusters_info import Dbv0039ClustersInfo
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_cluster(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_cluster: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_get_cluster.ApiResponseFor200) | Cluster information
default | [ApiResponseForDefault](#slurmdb_v0039_get_cluster.ApiResponseForDefault) | Cluster not found

#### slurmdb_v0039_get_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ClustersInfo**](../../models/Dbv0039ClustersInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ClustersInfo**](../../models/Dbv0039ClustersInfo.md) |  | 


#### slurmdb_v0039_get_cluster.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_clusters**
<a id="slurmdb_v0039_get_clusters"></a>
> Dbv0039ClustersInfo slurmdb_v0039_get_clusters()

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0039_clusters_info import Dbv0039ClustersInfo
from slurmrestapi.model.status import Status
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_clusters()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_clusters: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_get_clusters.ApiResponseFor200) | List of clusters
default | [ApiResponseForDefault](#slurmdb_v0039_get_clusters.ApiResponseForDefault) | Cluster not found

#### slurmdb_v0039_get_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ClustersInfo**](../../models/Dbv0039ClustersInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ClustersInfo**](../../models/Dbv0039ClustersInfo.md) |  | 


#### slurmdb_v0039_get_clusters.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_config**
<a id="slurmdb_v0039_get_config"></a>
> Dbv0039ConfigInfo slurmdb_v0039_get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_config_info import Dbv0039ConfigInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_config()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_config: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_get_config.ApiResponseFor200) | slurmdbd configuration
default | [ApiResponseForDefault](#slurmdb_v0039_get_config.ApiResponseForDefault) | Unable to dump config

#### slurmdb_v0039_get_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ConfigInfo**](../../models/Dbv0039ConfigInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039ConfigInfo**](../../models/Dbv0039ConfigInfo.md) |  | 


#### slurmdb_v0039_get_config.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_job**
<a id="slurmdb_v0039_get_job"></a>
> Dbv0039JobInfo slurmdb_v0039_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_job_info import Dbv0039JobInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_job(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_job: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_get_job.ApiResponseFor200) | Job description
default | [ApiResponseForDefault](#slurmdb_v0039_get_job.ApiResponseForDefault) | Unable to find job

#### slurmdb_v0039_get_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039JobInfo**](../../models/Dbv0039JobInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039JobInfo**](../../models/Dbv0039JobInfo.md) |  | 


#### slurmdb_v0039_get_job.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_jobs**
<a id="slurmdb_v0039_get_jobs"></a>
> Dbv0039JobInfo slurmdb_v0039_get_jobs()

Get job list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_job_info import Dbv0039JobInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        'users': "users_example",
        'submit_time': "submit_time_example",
        'start_time': "start_time_example",
        'end_time': "end_time_example",
        'account': "account_example",
        'association': "association_example",
        'cluster': "cluster_example",
        'constraints': "constraints_example",
        'cpus_max': "cpus_max_example",
        'cpus_min': "cpus_min_example",
        'skip_steps': "false",
        'disable_wait_for_result': "false",
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
        api_response = api_instance.slurmdb_v0039_get_jobs(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_jobs: %s\n" % e)
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
users | UsersSchema | | optional
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


# UsersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
str,  | str,  |  | must be one of ["true", "false", ] if omitted the server will use the default value of "false"

# DisableWaitForResultSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["true", "false", ] if omitted the server will use the default value of "false"

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
200 | [ApiResponseFor200](#slurmdb_v0039_get_jobs.ApiResponseFor200) | List of jobs
default | [ApiResponseForDefault](#slurmdb_v0039_get_jobs.ApiResponseForDefault) | Unable to query jobs

#### slurmdb_v0039_get_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039JobInfo**](../../models/Dbv0039JobInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039JobInfo**](../../models/Dbv0039JobInfo.md) |  | 


#### slurmdb_v0039_get_jobs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_qos**
<a id="slurmdb_v0039_get_qos"></a>
> Dbv0039QosInfo slurmdb_v0039_get_qos()

Get QOS list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_qos_info import Dbv0039QosInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        'with_deleted': "false",
    }
    try:
        # Get QOS list
        api_response = api_instance.slurmdb_v0039_get_qos(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_qos: %s\n" % e)
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
str,  | str,  |  | must be one of ["true", "false", ] if omitted the server will use the default value of "false"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_get_qos.ApiResponseFor200) | List of QOS&#x27;
default | [ApiResponseForDefault](#slurmdb_v0039_get_qos.ApiResponseForDefault) | QOS not found

#### slurmdb_v0039_get_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039QosInfo**](../../models/Dbv0039QosInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039QosInfo**](../../models/Dbv0039QosInfo.md) |  | 


#### slurmdb_v0039_get_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_single_qos**
<a id="slurmdb_v0039_get_single_qos"></a>
> Dbv0039QosInfo slurmdb_v0039_get_single_qos(qos_name)

Get QOS info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_qos_info import Dbv0039QosInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_single_qos(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_single_qos: %s\n" % e)

    # example passing only optional values
    path_params = {
        'qos_name': "qos_name_example",
    }
    query_params = {
        'with_deleted': "false",
    }
    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0039_get_single_qos(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_single_qos: %s\n" % e)
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
str,  | str,  |  | must be one of ["true", "false", ] if omitted the server will use the default value of "false"

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
200 | [ApiResponseFor200](#slurmdb_v0039_get_single_qos.ApiResponseFor200) | QOS information
default | [ApiResponseForDefault](#slurmdb_v0039_get_single_qos.ApiResponseForDefault) | QOS not found

#### slurmdb_v0039_get_single_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039QosInfo**](../../models/Dbv0039QosInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039QosInfo**](../../models/Dbv0039QosInfo.md) |  | 


#### slurmdb_v0039_get_single_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_tres**
<a id="slurmdb_v0039_get_tres"></a>
> Dbv0039TresInfo slurmdb_v0039_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.dbv0039_tres_info import Dbv0039TresInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_tres()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_tres: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_get_tres.ApiResponseFor200) | List of TRES
default | [ApiResponseForDefault](#slurmdb_v0039_get_tres.ApiResponseForDefault) | Unable to retrieve TRES

#### slurmdb_v0039_get_tres.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039TresInfo**](../../models/Dbv0039TresInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039TresInfo**](../../models/Dbv0039TresInfo.md) |  | 


#### slurmdb_v0039_get_tres.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_user**
<a id="slurmdb_v0039_get_user"></a>
> Dbv0039UserInfo slurmdb_v0039_get_user(user_name)

Get user info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_user_info import Dbv0039UserInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_user(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_name': "user_name_example",
    }
    query_params = {
        'with_deleted': "false",
    }
    try:
        # Get user info
        api_response = api_instance.slurmdb_v0039_get_user(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_user: %s\n" % e)
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
str,  | str,  |  | must be one of ["true", "false", ] if omitted the server will use the default value of "false"

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
200 | [ApiResponseFor200](#slurmdb_v0039_get_user.ApiResponseFor200) | List of users
default | [ApiResponseForDefault](#slurmdb_v0039_get_user.ApiResponseForDefault) | User not found

#### slurmdb_v0039_get_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039UserInfo**](../../models/Dbv0039UserInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039UserInfo**](../../models/Dbv0039UserInfo.md) |  | 


#### slurmdb_v0039_get_user.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_users**
<a id="slurmdb_v0039_get_users"></a>
> Dbv0039UserInfo slurmdb_v0039_get_users()

Get user list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_user_info import Dbv0039UserInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        'with_deleted': "false",
    }
    try:
        # Get user list
        api_response = api_instance.slurmdb_v0039_get_users(
            query_params=query_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_users: %s\n" % e)
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
str,  | str,  |  | must be one of ["true", "false", ] if omitted the server will use the default value of "false"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_get_users.ApiResponseFor200) | List of users
default | [ApiResponseForDefault](#slurmdb_v0039_get_users.ApiResponseForDefault) | User not found

#### slurmdb_v0039_get_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039UserInfo**](../../models/Dbv0039UserInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039UserInfo**](../../models/Dbv0039UserInfo.md) |  | 


#### slurmdb_v0039_get_users.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_wckey**
<a id="slurmdb_v0039_get_wckey"></a>
> Dbv0039WckeyInfo slurmdb_v0039_get_wckey(wckey)

Get wckey info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_wckey_info import Dbv0039WckeyInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_wckey(
            path_params=path_params,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_wckey: %s\n" % e)
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
200 | [ApiResponseFor200](#slurmdb_v0039_get_wckey.ApiResponseFor200) | List of wckey
default | [ApiResponseForDefault](#slurmdb_v0039_get_wckey.ApiResponseForDefault) | wckey not found

#### slurmdb_v0039_get_wckey.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039WckeyInfo**](../../models/Dbv0039WckeyInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039WckeyInfo**](../../models/Dbv0039WckeyInfo.md) |  | 


#### slurmdb_v0039_get_wckey.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_get_wckeys**
<a id="slurmdb_v0039_get_wckeys"></a>
> Dbv0039WckeyInfo slurmdb_v0039_get_wckeys()

Get wckey list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_wckey_info import Dbv0039WckeyInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

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
        api_response = api_instance.slurmdb_v0039_get_wckeys()
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_get_wckeys: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_get_wckeys.ApiResponseFor200) | List of wckeys
default | [ApiResponseForDefault](#slurmdb_v0039_get_wckeys.ApiResponseForDefault) | wckey not found

#### slurmdb_v0039_get_wckeys.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039WckeyInfo**](../../models/Dbv0039WckeyInfo.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039WckeyInfo**](../../models/Dbv0039WckeyInfo.md) |  | 


#### slurmdb_v0039_get_wckeys.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_set_config**
<a id="slurmdb_v0039_set_config"></a>
> Status slurmdb_v0039_set_config()

Load all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_set_config import Dbv0039SetConfig
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only optional values
    body = Dbv0039SetConfig(
        clusters=V0039ClusterRecList([
            V0039ClusterRec(
                controller=dict(
                    port=1,
                ),
                flags=[
                    "REGISTERING"
                ],
                name="name_example",
                nodes="nodes_example",
                select_plugin="select_plugin_example",
                associations=dict(
                    root=V0039AssocShort(
                        account="account_example",
                        cluster="cluster_example",
                        partition="partition_example",
                        user="user_example",
                    ),
                ),
                rpc_version=1,
                tres=V0039TresList([
                    V0039Tres(
                        type="type_example",
                        name="name_example",
                        id=1,
                        count=1,
                    )
                ]),
            )
        ]),
        tres=[],
        accounts=V0039AccountList([
            V0039Account(
                associations=V0039AssocShortList([
                    V0039AssocShort()
                ]),
                coordinators=V0039CoordList([
                    V0039Coord(
                        name="name_example",
                        direct=True,
                    )
                ]),
                description="description_example",
                name="name_example",
                organization="organization_example",
                flags=[
                    "DELETED"
                ],
            )
        ]),
        users=V0039UserList([
            V0039User(
                administrator_level=[
                    "Not Set"
                ],
,
,
                default=dict(
                    wckey="wckey_example",
                ),
                flags=[
                    "NONE"
                ],
                name="name_example",
                old_name="old_name_example",
                wckeys=V0039WckeyList([
                    V0039Wckey(
                        accounting=V0039AccountingList([
                            V0039Accounting(
                                allocated=dict(
                                    seconds=1,
                                ),
                                id=1,
                                start=1,
                                tres=V0039Tres(),
                            )
                        ]),
                        cluster="cluster_example",
                        id=1,
                        name="name_example",
                        user="user_example",
,
                    )
                ]),
            )
        ]),
        qos=V0039QosList([
            V0039Qos(
                description="description_example",
                flags=[
                    "NOT_SET"
                ],
                id=1,
                limits=dict(
                    min=dict(
                        tres=dict(
                            per=dict(
,
                            ),
                        ),
                    ),
                ),
                name="name_example",
                preempt=dict(
                    exempt_time=V0039Uint32NoVal(
                        set=False,
                        infinite=True,
                        number=1,
                    ),
                ),
                priority=1,
                usage_factor=V0039Float64NoVal(
                    set=False,
                    infinite=True,
                    number=3.14,
                ),
,
            )
        ]),
,
        associations=V0039AssocList([
            V0039Assoc(
                account="account_example",
                cluster="cluster_example",
                default=dict(
                    qos="qos_example",
                ),
,
                max=dict(
                    jobs=dict(
                        per=dict(
                            wall_clock=V0039Uint32NoVal(),
                        ),
                    ),
                ),
                is_default=True,
                min=dict(
                    priority_threshold=V0039Uint32NoVal(),
                ),
                parent_account="parent_account_example",
                partition="partition_example",
                priority=V0039Uint32NoVal(),
                qos=V0039QosStringIdList([
                    "qos_example"
                ]),
                shares_raw=1,
                usage=V0039AssocUsage(
                    accrue_job_count=1,
                    group_used_wallclock=3.14,
                    fairshare_factor=3.14,
                    fairshare_shares=1,
                    normalized_priority=3.14,
                    normalized_shares=3.14,
                    effective_normalized_usage=3.14,
                    normalized_usage=3.14,
                    raw_usage=3.14,
                    active_jobs=1,
                    job_count=1,
                    fairshare_level=3.14,
                ),
                user="user_example",
            )
        ]),
    )
    try:
        # Load all configuration information
        api_response = api_instance.slurmdb_v0039_set_config(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_set_config: %s\n" % e)
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
[**Dbv0039SetConfig**](../../models/Dbv0039SetConfig.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039SetConfig**](../../models/Dbv0039SetConfig.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_set_config.ApiResponseFor200) | Load config
default | [ApiResponseForDefault](#slurmdb_v0039_set_config.ApiResponseForDefault) | Unable to set config

#### slurmdb_v0039_set_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_set_config.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_update_accounts**
<a id="slurmdb_v0039_update_accounts"></a>
> Status slurmdb_v0039_update_accounts(dbv0039_account_info)

Update accounts

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_account_info import Dbv0039AccountInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0039AccountInfo(
        meta=Dbv0039Meta(
            plugin=dict(
                type="type_example",
                name="name_example",
            ),
            slurm=dict(
                version=dict(
                    major=1,
                    micro=1,
                    minor=1,
                ),
                release="release_example",
            ),
        ),
        errors=Dbv0039Errors([
            Dbv0039Error(
                error_number=1,
                error="error_example",
                source="source_example",
                description="description_example",
            )
        ]),
        warnings=Dbv0039Warnings([
            Dbv0039Warning(
                warning="warning_example",
                source="source_example",
                description="description_example",
            )
        ]),
        accounts=V0039AccountList([
            V0039Account(
                associations=V0039AssocShortList([
                    V0039AssocShort(
                        account="account_example",
                        cluster="cluster_example",
                        partition="partition_example",
                        user="user_example",
                    )
                ]),
                coordinators=V0039CoordList([
                    V0039Coord(
                        name="name_example",
                        direct=True,
                    )
                ]),
                description="description_example",
                name="name_example",
                organization="organization_example",
                flags=[
                    "DELETED"
                ],
            )
        ]),
    )
    try:
        # Update accounts
        api_response = api_instance.slurmdb_v0039_update_accounts(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_accounts: %s\n" % e)
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
[**Dbv0039AccountInfo**](../../models/Dbv0039AccountInfo.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AccountInfo**](../../models/Dbv0039AccountInfo.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_update_accounts.ApiResponseFor200) | Add/update list of accounts
default | [ApiResponseForDefault](#slurmdb_v0039_update_accounts.ApiResponseForDefault) | Unable to add or update accounts

#### slurmdb_v0039_update_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_update_accounts.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_update_associations**
<a id="slurmdb_v0039_update_associations"></a>
> Status slurmdb_v0039_update_associations(dbv0039_associations_info)

Set associations info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_associations_info import Dbv0039AssociationsInfo
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0039AssociationsInfo(
        meta=Dbv0039Meta(
            plugin=dict(
                type="type_example",
                name="name_example",
            ),
            slurm=dict(
                version=dict(
                    major=1,
                    micro=1,
                    minor=1,
                ),
                release="release_example",
            ),
        ),
        errors=Dbv0039Errors([
            Dbv0039Error(
                error_number=1,
                error="error_example",
                source="source_example",
                description="description_example",
            )
        ]),
        warnings=Dbv0039Warnings([
            Dbv0039Warning(
                warning="warning_example",
                source="source_example",
                description="description_example",
            )
        ]),
        associations=V0039AssocList([
            V0039Assoc(
                account="account_example",
                cluster="cluster_example",
                default=dict(
                    qos="qos_example",
                ),
                flags=[
                    "DELETED"
                ],
                max=dict(
                    jobs=dict(
                        per=dict(
                            wall_clock=V0039Uint32NoVal(
                                set=False,
                                infinite=True,
                                number=1,
                            ),
                        ),
                    ),
                ),
                is_default=True,
                min=dict(
                    priority_threshold=V0039Uint32NoVal(),
                ),
                parent_account="parent_account_example",
                partition="partition_example",
                priority=V0039Uint32NoVal(),
                qos=V0039QosStringIdList([
                    "qos_example"
                ]),
                shares_raw=1,
                usage=V0039AssocUsage(
                    accrue_job_count=1,
                    group_used_wallclock=3.14,
                    fairshare_factor=3.14,
                    fairshare_shares=1,
                    normalized_priority=3.14,
                    normalized_shares=3.14,
                    effective_normalized_usage=3.14,
                    normalized_usage=3.14,
                    raw_usage=3.14,
                    active_jobs=1,
                    job_count=1,
                    fairshare_level=3.14,
                ),
                user="user_example",
            )
        ]),
    )
    try:
        # Set associations info
        api_response = api_instance.slurmdb_v0039_update_associations(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_associations: %s\n" % e)
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
[**Dbv0039AssociationsInfo**](../../models/Dbv0039AssociationsInfo.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039AssociationsInfo**](../../models/Dbv0039AssociationsInfo.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_update_associations.ApiResponseFor200) | status of associations update
default | [ApiResponseForDefault](#slurmdb_v0039_update_associations.ApiResponseForDefault) | Unable to update associations

#### slurmdb_v0039_update_associations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_update_associations.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_update_qos**
<a id="slurmdb_v0039_update_qos"></a>
> Status slurmdb_v0039_update_qos(dbv0039_update_qos)

Set QOS info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_update_qos import Dbv0039UpdateQos
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0039UpdateQos(
        qos=V0039QosList([
            V0039Qos(
                description="description_example",
                flags=[
                    "NOT_SET"
                ],
                id=1,
                limits=dict(
                    min=dict(
                        tres=dict(
                            per=dict(
                                job=V0039TresList([
                                    V0039Tres(
                                        type="type_example",
                                        name="name_example",
                                        id=1,
                                        count=1,
                                    )
                                ]),
                            ),
                        ),
                    ),
                ),
                name="name_example",
                preempt=dict(
                    exempt_time=V0039Uint32NoVal(
                        set=False,
                        infinite=True,
                        number=1,
                    ),
                ),
                priority=1,
                usage_factor=V0039Float64NoVal(
                    set=False,
                    infinite=True,
                    number=3.14,
                ),
,
            )
        ]),
    )
    try:
        # Set QOS info
        api_response = api_instance.slurmdb_v0039_update_qos(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_qos: %s\n" % e)
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
[**Dbv0039UpdateQos**](../../models/Dbv0039UpdateQos.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039UpdateQos**](../../models/Dbv0039UpdateQos.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_update_qos.ApiResponseFor200) | QOS update response
default | [ApiResponseForDefault](#slurmdb_v0039_update_qos.ApiResponseForDefault) | Unable to update QOSs

#### slurmdb_v0039_update_qos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_update_qos.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_update_tres**
<a id="slurmdb_v0039_update_tres"></a>
> Status slurmdb_v0039_update_tres(dbv0039_tres_update)

Set TRES info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_tres_update import Dbv0039TresUpdate
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0039TresUpdate(
        tres=V0039TresList([
            V0039Tres(
                type="type_example",
                name="name_example",
                id=1,
                count=1,
            )
        ]),
    )
    try:
        # Set TRES info
        api_response = api_instance.slurmdb_v0039_update_tres(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_tres: %s\n" % e)
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
[**Dbv0039TresUpdate**](../../models/Dbv0039TresUpdate.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039TresUpdate**](../../models/Dbv0039TresUpdate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_update_tres.ApiResponseFor200) | List of TRES
default | [ApiResponseForDefault](#slurmdb_v0039_update_tres.ApiResponseForDefault) | Unable to update TRES

#### slurmdb_v0039_update_tres.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_update_tres.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **slurmdb_v0039_update_users**
<a id="slurmdb_v0039_update_users"></a>
> Status slurmdb_v0039_update_users(dbv0039_update_users)

Update user

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import slurm_api
from slurmrestapi.model.status import Status
from slurmrestapi.model.dbv0039_update_users import Dbv0039UpdateUsers
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurm_api.SlurmApi(api_client)

    # example passing only required values which don't have defaults set
    body = Dbv0039UpdateUsers(
        users=V0039UserList([
            V0039User(
                administrator_level=[
                    "Not Set"
                ],
                associations=V0039AssocShortList([
                    V0039AssocShort(
                        account="account_example",
                        cluster="cluster_example",
                        partition="partition_example",
                        user="user_example",
                    )
                ]),
                coordinators=V0039CoordList([
                    V0039Coord(
                        name="name_example",
                        direct=True,
                    )
                ]),
                default=dict(
                    wckey="wckey_example",
                ),
                flags=[
                    "NONE"
                ],
                name="name_example",
                old_name="old_name_example",
                wckeys=V0039WckeyList([
                    V0039Wckey(
                        accounting=V0039AccountingList([
                            V0039Accounting(
                                allocated=dict(
                                    seconds=1,
                                ),
                                id=1,
                                start=1,
                                tres=V0039Tres(
                                    type="type_example",
                                    name="name_example",
                                    id=1,
                                    count=1,
                                ),
                            )
                        ]),
                        cluster="cluster_example",
                        id=1,
                        name="name_example",
                        user="user_example",
                        flags=[
                            "DELETED"
                        ],
                    )
                ]),
            )
        ]),
    )
    try:
        # Update user
        api_response = api_instance.slurmdb_v0039_update_users(
            body=body,
        )
        pprint(api_response)
    except slurmrestapi.ApiException as e:
        print("Exception when calling SlurmApi->slurmdb_v0039_update_users: %s\n" % e)
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
[**Dbv0039UpdateUsers**](../../models/Dbv0039UpdateUsers.md) |  | 


# SchemaForRequestBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Dbv0039UpdateUsers**](../../models/Dbv0039UpdateUsers.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#slurmdb_v0039_update_users.ApiResponseFor200) | Update users
default | [ApiResponseForDefault](#slurmdb_v0039_update_users.ApiResponseForDefault) | User not found or not able to update user

#### slurmdb_v0039_update_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor200ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


#### slurmdb_v0039_update_users.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationXYaml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


# SchemaFor0ResponseBodyApplicationXYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**Status**](../../models/Status.md) |  | 


### Authorization

[user](../../../README.md#user), [bearerAuth](../../../README.md#bearerAuth), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

