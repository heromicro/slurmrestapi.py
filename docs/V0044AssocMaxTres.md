# V0044AssocMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**group** | [**V0044AssocMaxTresGroup**](V0044AssocMaxTresGroup.md) |  | [optional] 
**minutes** | [**V0044AssocMaxTresMinutes**](V0044AssocMaxTresMinutes.md) |  | [optional] 
**per** | [**V0044AssocMaxTresPer**](V0044AssocMaxTresPer.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_assoc_max_tres import V0044AssocMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AssocMaxTres from a JSON string
v0044_assoc_max_tres_instance = V0044AssocMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0044AssocMaxTres.to_json())

# convert the object into a dict
v0044_assoc_max_tres_dict = v0044_assoc_max_tres_instance.to_dict()
# create an instance of V0044AssocMaxTres from a dict
v0044_assoc_max_tres_from_dict = V0044AssocMaxTres.from_dict(v0044_assoc_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


