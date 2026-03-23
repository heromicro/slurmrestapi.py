# V0044PartitionInfoMaximums


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus_per_node** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**cpus_per_socket** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**memory_per_cpu** | **int** | Raw value for MaxMemPerCPU or MaxMemPerNode | [optional] 
**partition_memory_per_cpu** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**partition_memory_per_node** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**nodes** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**shares** | **int** | OverSubscribe - Controls the ability of the partition to execute more than one job at a time on each resource | [optional] 
**oversubscribe** | [**V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe**](V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe.md) |  | [optional] 
**time** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**over_time_limit** | [**V0044Uint16NoValStruct**](V0044Uint16NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_partition_info_maximums import V0044PartitionInfoMaximums

# TODO update the JSON string below
json = "{}"
# create an instance of V0044PartitionInfoMaximums from a JSON string
v0044_partition_info_maximums_instance = V0044PartitionInfoMaximums.from_json(json)
# print the JSON string representation of the object
print(V0044PartitionInfoMaximums.to_json())

# convert the object into a dict
v0044_partition_info_maximums_dict = v0044_partition_info_maximums_instance.to_dict()
# create an instance of V0044PartitionInfoMaximums from a dict
v0044_partition_info_maximums_from_dict = V0044PartitionInfoMaximums.from_dict(v0044_partition_info_maximums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


