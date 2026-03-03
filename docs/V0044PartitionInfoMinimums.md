# V0044PartitionInfoMinimums


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **int** | MinNodes - Minimum count of nodes which may be allocated to any single job | [optional] 

## Example

```python
from slurmrestapi.models.v0044_partition_info_minimums import V0044PartitionInfoMinimums

# TODO update the JSON string below
json = "{}"
# create an instance of V0044PartitionInfoMinimums from a JSON string
v0044_partition_info_minimums_instance = V0044PartitionInfoMinimums.from_json(json)
# print the JSON string representation of the object
print(V0044PartitionInfoMinimums.to_json())

# convert the object into a dict
v0044_partition_info_minimums_dict = v0044_partition_info_minimums_instance.to_dict()
# create an instance of V0044PartitionInfoMinimums from a dict
v0044_partition_info_minimums_from_dict = V0044PartitionInfoMinimums.from_dict(v0044_partition_info_minimums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


