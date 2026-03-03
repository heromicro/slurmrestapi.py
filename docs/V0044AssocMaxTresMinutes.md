# V0044AssocMaxTresMinutes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**per** | [**V0044QosLimitsMinTresPer**](V0044QosLimitsMinTresPer.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_assoc_max_tres_minutes import V0044AssocMaxTresMinutes

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AssocMaxTresMinutes from a JSON string
v0044_assoc_max_tres_minutes_instance = V0044AssocMaxTresMinutes.from_json(json)
# print the JSON string representation of the object
print(V0044AssocMaxTresMinutes.to_json())

# convert the object into a dict
v0044_assoc_max_tres_minutes_dict = v0044_assoc_max_tres_minutes_instance.to_dict()
# create an instance of V0044AssocMaxTresMinutes from a dict
v0044_assoc_max_tres_minutes_from_dict = V0044AssocMaxTresMinutes.from_dict(v0044_assoc_max_tres_minutes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


