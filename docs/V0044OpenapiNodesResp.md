# V0044OpenapiNodesResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[V0044Node]**](V0044Node.md) |  | 
**last_update** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | 
**meta** | [**V0044OpenapiMeta**](V0044OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0044OpenapiError]**](V0044OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0044OpenapiWarning]**](V0044OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_nodes_resp import V0044OpenapiNodesResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiNodesResp from a JSON string
v0044_openapi_nodes_resp_instance = V0044OpenapiNodesResp.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiNodesResp.to_json())

# convert the object into a dict
v0044_openapi_nodes_resp_dict = v0044_openapi_nodes_resp_instance.to_dict()
# create an instance of V0044OpenapiNodesResp from a dict
v0044_openapi_nodes_resp_from_dict = V0044OpenapiNodesResp.from_dict(v0044_openapi_nodes_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


