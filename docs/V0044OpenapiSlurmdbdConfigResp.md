# V0044OpenapiSlurmdbdConfigResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[V0044ClusterRec]**](V0044ClusterRec.md) |  | [optional] 
**tres** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**accounts** | [**List[V0044Account]**](V0044Account.md) |  | [optional] 
**users** | [**List[V0044User]**](V0044User.md) |  | [optional] 
**qos** | [**List[V0044Qos]**](V0044Qos.md) |  | [optional] 
**wckeys** | [**List[V0044Wckey]**](V0044Wckey.md) |  | [optional] 
**associations** | [**List[V0044Assoc]**](V0044Assoc.md) |  | [optional] 
**instances** | [**List[V0044Instance]**](V0044Instance.md) |  | [optional] 
**meta** | [**V0044OpenapiMeta**](V0044OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0044OpenapiError]**](V0044OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0044OpenapiWarning]**](V0044OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_slurmdbd_config_resp import V0044OpenapiSlurmdbdConfigResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiSlurmdbdConfigResp from a JSON string
v0044_openapi_slurmdbd_config_resp_instance = V0044OpenapiSlurmdbdConfigResp.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiSlurmdbdConfigResp.to_json())

# convert the object into a dict
v0044_openapi_slurmdbd_config_resp_dict = v0044_openapi_slurmdbd_config_resp_instance.to_dict()
# create an instance of V0044OpenapiSlurmdbdConfigResp from a dict
v0044_openapi_slurmdbd_config_resp_from_dict = V0044OpenapiSlurmdbdConfigResp.from_dict(v0044_openapi_slurmdbd_config_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


