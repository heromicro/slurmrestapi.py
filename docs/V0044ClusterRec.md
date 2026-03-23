# V0044ClusterRec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | [**V0041OpenapiSlurmdbdConfigRespClustersInnerController**](V0041OpenapiSlurmdbdConfigRespClustersInnerController.md) |  | [optional] 
**flags** | **List[str]** | Flags | [optional] 
**name** | **str** | ClusterName | [optional] 
**nodes** | **str** | Node names | [optional] 
**select_plugin** | **str** |  | [optional] 
**associations** | [**V0044ClusterRecAssociations**](V0044ClusterRecAssociations.md) |  | [optional] 
**rpc_version** | **int** | RPC version used in the cluster | [optional] 
**tres** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_cluster_rec import V0044ClusterRec

# TODO update the JSON string below
json = "{}"
# create an instance of V0044ClusterRec from a JSON string
v0044_cluster_rec_instance = V0044ClusterRec.from_json(json)
# print the JSON string representation of the object
print(V0044ClusterRec.to_json())

# convert the object into a dict
v0044_cluster_rec_dict = v0044_cluster_rec_instance.to_dict()
# create an instance of V0044ClusterRec from a dict
v0044_cluster_rec_from_dict = V0044ClusterRec.from_dict(v0044_cluster_rec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


