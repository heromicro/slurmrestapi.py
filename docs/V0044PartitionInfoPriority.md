# V0044PartitionInfoPriority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_factor** | **int** | PriorityJobFactor - Partition factor used by priority/multifactor plugin in calculating job priority | [optional] 
**tier** | **int** | PriorityTier - Controls the order in which the scheduler evaluates jobs from different partitions | [optional] 

## Example

```python
from slurmrestapi.models.v0044_partition_info_priority import V0044PartitionInfoPriority

# TODO update the JSON string below
json = "{}"
# create an instance of V0044PartitionInfoPriority from a JSON string
v0044_partition_info_priority_instance = V0044PartitionInfoPriority.from_json(json)
# print the JSON string representation of the object
print(V0044PartitionInfoPriority.to_json())

# convert the object into a dict
v0044_partition_info_priority_dict = v0044_partition_info_priority_instance.to_dict()
# create an instance of V0044PartitionInfoPriority from a dict
v0044_partition_info_priority_from_dict = V0044PartitionInfoPriority.from_dict(v0044_partition_info_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


