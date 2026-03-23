# V0044PartitionInfoDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_per_cpu** | **int** | Raw value for DefMemPerCPU or DefMemPerNode | [optional] 
**partition_memory_per_cpu** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**partition_memory_per_node** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**time** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**job** | **str** | JobDefaults - Comma-separated list of job default values (this field is only used to set new defaults) | [optional] 

## Example

```python
from slurmrestapi.models.v0044_partition_info_defaults import V0044PartitionInfoDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of V0044PartitionInfoDefaults from a JSON string
v0044_partition_info_defaults_instance = V0044PartitionInfoDefaults.from_json(json)
# print the JSON string representation of the object
print(V0044PartitionInfoDefaults.to_json())

# convert the object into a dict
v0044_partition_info_defaults_dict = v0044_partition_info_defaults_instance.to_dict()
# create an instance of V0044PartitionInfoDefaults from a dict
v0044_partition_info_defaults_from_dict = V0044PartitionInfoDefaults.from_dict(v0044_partition_info_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


