# V0044PartitionInfoGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **str** | AllowGroups - Comma-separated list of group names which may execute jobs in this partition | [optional] 

## Example

```python
from slurmrestapi.models.v0044_partition_info_groups import V0044PartitionInfoGroups

# TODO update the JSON string below
json = "{}"
# create an instance of V0044PartitionInfoGroups from a JSON string
v0044_partition_info_groups_instance = V0044PartitionInfoGroups.from_json(json)
# print the JSON string representation of the object
print(V0044PartitionInfoGroups.to_json())

# convert the object into a dict
v0044_partition_info_groups_dict = v0044_partition_info_groups_instance.to_dict()
# create an instance of V0044PartitionInfoGroups from a dict
v0044_partition_info_groups_from_dict = V0044PartitionInfoGroups.from_dict(v0044_partition_info_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


