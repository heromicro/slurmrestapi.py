<a id="__pageTop"></a>
# slurmrestapi.apis.tags.openapi_api.OpenapiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openapi_get**](#openapi_get) | **get** /openapi | Retrieve OpenAPI Specification
[**openapi_json_get**](#openapi_json_get) | **get** /openapi.json | Retrieve OpenAPI Specification
[**openapi_v3_get**](#openapi_v3_get) | **get** /openapi/v3 | Retrieve OpenAPI Specification
[**openapi_yaml_get**](#openapi_yaml_get) | **get** /openapi.yaml | Retrieve OpenAPI Specification

# **openapi_get**
<a id="openapi_get"></a>
> openapi_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import openapi_api
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
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve OpenAPI Specification
        api_response = api_instance.openapi_get()
    except slurmrestapi.ApiException as e:
        print("Exception when calling OpenapiApi->openapi_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#openapi_get.ApiResponseFor200) | OpenAPI Specification

#### openapi_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **openapi_json_get**
<a id="openapi_json_get"></a>
> openapi_json_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import openapi_api
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
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve OpenAPI Specification
        api_response = api_instance.openapi_json_get()
    except slurmrestapi.ApiException as e:
        print("Exception when calling OpenapiApi->openapi_json_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#openapi_json_get.ApiResponseFor200) | OpenAPI Specification

#### openapi_json_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **openapi_v3_get**
<a id="openapi_v3_get"></a>
> openapi_v3_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import openapi_api
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
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve OpenAPI Specification
        api_response = api_instance.openapi_v3_get()
    except slurmrestapi.ApiException as e:
        print("Exception when calling OpenapiApi->openapi_v3_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#openapi_v3_get.ApiResponseFor200) | OpenAPI Specification

#### openapi_v3_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **openapi_yaml_get**
<a id="openapi_yaml_get"></a>
> openapi_yaml_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):
```python
import slurmrestapi
from slurmrestapi.apis.tags import openapi_api
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
    api_instance = openapi_api.OpenapiApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve OpenAPI Specification
        api_response = api_instance.openapi_yaml_get()
    except slurmrestapi.ApiException as e:
        print("Exception when calling OpenapiApi->openapi_yaml_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#openapi_yaml_get.ApiResponseFor200) | OpenAPI Specification

#### openapi_yaml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[user](../../../README.md#user), [token](../../../README.md#token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

