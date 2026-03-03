# V0044QosLimitsMaxTresMinutes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**per** | [**V0044QosLimitsMaxTresMinutesPer**](V0044QosLimitsMaxTresMinutesPer.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits_max_tres_minutes import V0044QosLimitsMaxTresMinutes

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimitsMaxTresMinutes from a JSON string
v0044_qos_limits_max_tres_minutes_instance = V0044QosLimitsMaxTresMinutes.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimitsMaxTresMinutes.to_json())

# convert the object into a dict
v0044_qos_limits_max_tres_minutes_dict = v0044_qos_limits_max_tres_minutes_instance.to_dict()
# create an instance of V0044QosLimitsMaxTresMinutes from a dict
v0044_qos_limits_max_tres_minutes_from_dict = V0044QosLimitsMaxTresMinutes.from_dict(v0044_qos_limits_max_tres_minutes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


