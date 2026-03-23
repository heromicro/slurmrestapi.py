# V0044OpenapiInstancesResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[V0044Instance]**](V0044Instance.md) |  | 
**meta** | [**V0044OpenapiMeta**](V0044OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0044OpenapiError]**](V0044OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0044OpenapiWarning]**](V0044OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_instances_resp import V0044OpenapiInstancesResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiInstancesResp from a JSON string
v0044_openapi_instances_resp_instance = V0044OpenapiInstancesResp.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiInstancesResp.to_json())

# convert the object into a dict
v0044_openapi_instances_resp_dict = v0044_openapi_instances_resp_instance.to_dict()
# create an instance of V0044OpenapiInstancesResp from a dict
v0044_openapi_instances_resp_from_dict = V0044OpenapiInstancesResp.from_dict(v0044_openapi_instances_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


