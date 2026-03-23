# slurmrestapi.UtilApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**util_v0044_post_hostlist**](UtilApi.md#util_v0044_post_hostlist) | **POST** /util/v0.0.44/hostlist | Convert an array of host names into hostlist expression
[**util_v0044_post_hostnames**](UtilApi.md#util_v0044_post_hostnames) | **POST** /util/v0.0.44/hostnames | Convert a hostlist expression into array of host names


# **util_v0044_post_hostlist**
> V0044OpenapiHostlistReqResp util_v0044_post_hostlist(v0044_openapi_hostnames_req_resp=v0044_openapi_hostnames_req_resp)

Convert an array of host names into hostlist expression

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_hostlist_req_resp import V0044OpenapiHostlistReqResp
from slurmrestapi.models.v0044_openapi_hostnames_req_resp import V0044OpenapiHostnamesReqResp
from slurmrestapi.rest import ApiException
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
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.UtilApi(api_client)
    v0044_openapi_hostnames_req_resp = slurmrestapi.V0044OpenapiHostnamesReqResp() # V0044OpenapiHostnamesReqResp | Array of host names (optional)

    try:
        # Convert an array of host names into hostlist expression
        api_response = api_instance.util_v0044_post_hostlist(v0044_openapi_hostnames_req_resp=v0044_openapi_hostnames_req_resp)
        print("The response of UtilApi->util_v0044_post_hostlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilApi->util_v0044_post_hostlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0044_openapi_hostnames_req_resp** | [**V0044OpenapiHostnamesReqResp**](V0044OpenapiHostnamesReqResp.md)| Array of host names | [optional] 

### Return type

[**V0044OpenapiHostlistReqResp**](V0044OpenapiHostlistReqResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hostlist expression |  -  |
**0** | Hostlist expression |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **util_v0044_post_hostnames**
> V0044OpenapiHostnamesReqResp util_v0044_post_hostnames(v0044_openapi_hostlist_req_resp=v0044_openapi_hostlist_req_resp)

Convert a hostlist expression into array of host names

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_hostlist_req_resp import V0044OpenapiHostlistReqResp
from slurmrestapi.models.v0044_openapi_hostnames_req_resp import V0044OpenapiHostnamesReqResp
from slurmrestapi.rest import ApiException
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
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.UtilApi(api_client)
    v0044_openapi_hostlist_req_resp = slurmrestapi.V0044OpenapiHostlistReqResp() # V0044OpenapiHostlistReqResp | Hostlist expression (optional)

    try:
        # Convert a hostlist expression into array of host names
        api_response = api_instance.util_v0044_post_hostnames(v0044_openapi_hostlist_req_resp=v0044_openapi_hostlist_req_resp)
        print("The response of UtilApi->util_v0044_post_hostnames:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilApi->util_v0044_post_hostnames: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0044_openapi_hostlist_req_resp** | [**V0044OpenapiHostlistReqResp**](V0044OpenapiHostlistReqResp.md)| Hostlist expression | [optional] 

### Return type

[**V0044OpenapiHostnamesReqResp**](V0044OpenapiHostnamesReqResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of host names |  -  |
**0** | Array of host names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

