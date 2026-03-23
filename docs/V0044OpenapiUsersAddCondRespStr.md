# V0044OpenapiUsersAddCondRespStr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_users** | **str** | added_users | 
**meta** | [**V0044OpenapiMeta**](V0044OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0044OpenapiError]**](V0044OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0044OpenapiWarning]**](V0044OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_users_add_cond_resp_str import V0044OpenapiUsersAddCondRespStr

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiUsersAddCondRespStr from a JSON string
v0044_openapi_users_add_cond_resp_str_instance = V0044OpenapiUsersAddCondRespStr.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiUsersAddCondRespStr.to_json())

# convert the object into a dict
v0044_openapi_users_add_cond_resp_str_dict = v0044_openapi_users_add_cond_resp_str_instance.to_dict()
# create an instance of V0044OpenapiUsersAddCondRespStr from a dict
v0044_openapi_users_add_cond_resp_str_from_dict = V0044OpenapiUsersAddCondRespStr.from_dict(v0044_openapi_users_add_cond_resp_str_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


