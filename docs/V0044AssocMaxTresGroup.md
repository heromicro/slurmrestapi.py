# V0044AssocMaxTresGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**active** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_assoc_max_tres_group import V0044AssocMaxTresGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AssocMaxTresGroup from a JSON string
v0044_assoc_max_tres_group_instance = V0044AssocMaxTresGroup.from_json(json)
# print the JSON string representation of the object
print(V0044AssocMaxTresGroup.to_json())

# convert the object into a dict
v0044_assoc_max_tres_group_dict = v0044_assoc_max_tres_group_instance.to_dict()
# create an instance of V0044AssocMaxTresGroup from a dict
v0044_assoc_max_tres_group_from_dict = V0044AssocMaxTresGroup.from_dict(v0044_assoc_max_tres_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


