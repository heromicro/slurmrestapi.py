# V0044PartitionInfoTimeouts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resume** | [**V0044Uint16NoValStruct**](V0044Uint16NoValStruct.md) |  | [optional] 
**suspend** | [**V0044Uint16NoValStruct**](V0044Uint16NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_partition_info_timeouts import V0044PartitionInfoTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of V0044PartitionInfoTimeouts from a JSON string
v0044_partition_info_timeouts_instance = V0044PartitionInfoTimeouts.from_json(json)
# print the JSON string representation of the object
print(V0044PartitionInfoTimeouts.to_json())

# convert the object into a dict
v0044_partition_info_timeouts_dict = v0044_partition_info_timeouts_instance.to_dict()
# create an instance of V0044PartitionInfoTimeouts from a dict
v0044_partition_info_timeouts_from_dict = V0044PartitionInfoTimeouts.from_dict(v0044_partition_info_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


