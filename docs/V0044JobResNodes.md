# V0044JobResNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of allocated nodes | [optional] 
**select_type** | **List[str]** | Node scheduling selection method | [optional] 
**list** | **str** | Node(s) allocated to the job | [optional] 
**whole** | **bool** | Whether whole nodes were allocated | [optional] 
**allocation** | [**List[V0044JobResNode]**](V0044JobResNode.md) | Job resources for a node | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_res_nodes import V0044JobResNodes

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobResNodes from a JSON string
v0044_job_res_nodes_instance = V0044JobResNodes.from_json(json)
# print the JSON string representation of the object
print(V0044JobResNodes.to_json())

# convert the object into a dict
v0044_job_res_nodes_dict = v0044_job_res_nodes_instance.to_dict()
# create an instance of V0044JobResNodes from a dict
v0044_job_res_nodes_from_dict = V0044JobResNodes.from_dict(v0044_job_res_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


