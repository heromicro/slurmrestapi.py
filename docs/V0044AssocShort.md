# V0044AssocShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account name | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**partition** | **str** | Partition name | [optional] 
**user** | **str** | User name | 
**id** | **int** | Numeric association ID | [optional] 

## Example

```python
from slurmrestapi.models.v0044_assoc_short import V0044AssocShort

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AssocShort from a JSON string
v0044_assoc_short_instance = V0044AssocShort.from_json(json)
# print the JSON string representation of the object
print(V0044AssocShort.to_json())

# convert the object into a dict
v0044_assoc_short_dict = v0044_assoc_short_instance.to_dict()
# create an instance of V0044AssocShort from a dict
v0044_assoc_short_from_dict = V0044AssocShort.from_dict(v0044_assoc_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


