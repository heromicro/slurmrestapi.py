# V0044JobResNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Node index | 
**name** | **str** | Node name | 
**cpus** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerCpus**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerCpus.md) |  | [optional] 
**memory** | [**V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerMemory**](V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerMemory.md) |  | [optional] 
**sockets** | [**List[V0044JobResSocket]**](V0044JobResSocket.md) |  | 

## Example

```python
from slurmrestapi.models.v0044_job_res_node import V0044JobResNode

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobResNode from a JSON string
v0044_job_res_node_instance = V0044JobResNode.from_json(json)
# print the JSON string representation of the object
print(V0044JobResNode.to_json())

# convert the object into a dict
v0044_job_res_node_dict = v0044_job_res_node_instance.to_dict()
# create an instance of V0044JobResNode from a dict
v0044_job_res_node_from_dict = V0044JobResNode.from_dict(v0044_job_res_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


