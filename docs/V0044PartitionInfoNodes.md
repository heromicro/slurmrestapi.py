# V0044PartitionInfoNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_allocation** | **str** | AllocNodes - Comma-separated list of nodes from which users can submit jobs in the partition | [optional] 
**configured** | **str** | Nodes - Comma-separated list of nodes which are associated with this partition | [optional] 
**total** | **int** | TotalNodes - Number of nodes available in this partition | [optional] 

## Example

```python
from slurmrestapi.models.v0044_partition_info_nodes import V0044PartitionInfoNodes

# TODO update the JSON string below
json = "{}"
# create an instance of V0044PartitionInfoNodes from a JSON string
v0044_partition_info_nodes_instance = V0044PartitionInfoNodes.from_json(json)
# print the JSON string representation of the object
print(V0044PartitionInfoNodes.to_json())

# convert the object into a dict
v0044_partition_info_nodes_dict = v0044_partition_info_nodes_instance.to_dict()
# create an instance of V0044PartitionInfoNodes from a dict
v0044_partition_info_nodes_from_dict = V0044PartitionInfoNodes.from_dict(v0044_partition_info_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


