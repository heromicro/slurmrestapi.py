# V0044PartitionInfoCpus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_binding** | **int** | CpuBind - Default method controlling how tasks are bound to allocated resources | [optional] 
**total** | **int** | TotalCPUs - Number of CPUs available in this partition | [optional] 

## Example

```python
from slurmrestapi.models.v0044_partition_info_cpus import V0044PartitionInfoCpus

# TODO update the JSON string below
json = "{}"
# create an instance of V0044PartitionInfoCpus from a JSON string
v0044_partition_info_cpus_instance = V0044PartitionInfoCpus.from_json(json)
# print the JSON string representation of the object
print(V0044PartitionInfoCpus.to_json())

# convert the object into a dict
v0044_partition_info_cpus_dict = v0044_partition_info_cpus_instance.to_dict()
# create an instance of V0044PartitionInfoCpus from a dict
v0044_partition_info_cpus_from_dict = V0044PartitionInfoCpus.from_dict(v0044_partition_info_cpus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


