# V0044OpenapiClustersResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[V0044ClusterRec]**](V0044ClusterRec.md) |  | 
**meta** | [**V0044OpenapiMeta**](V0044OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0044OpenapiError]**](V0044OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0044OpenapiWarning]**](V0044OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_clusters_resp import V0044OpenapiClustersResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiClustersResp from a JSON string
v0044_openapi_clusters_resp_instance = V0044OpenapiClustersResp.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiClustersResp.to_json())

# convert the object into a dict
v0044_openapi_clusters_resp_dict = v0044_openapi_clusters_resp_instance.to_dict()
# create an instance of V0044OpenapiClustersResp from a dict
v0044_openapi_clusters_resp_from_dict = V0044OpenapiClustersResp.from_dict(v0044_openapi_clusters_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


