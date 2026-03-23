# V0044QosLimitsMaxTresMinutesPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**job** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**account** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**user** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits_max_tres_minutes_per import V0044QosLimitsMaxTresMinutesPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimitsMaxTresMinutesPer from a JSON string
v0044_qos_limits_max_tres_minutes_per_instance = V0044QosLimitsMaxTresMinutesPer.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimitsMaxTresMinutesPer.to_json())

# convert the object into a dict
v0044_qos_limits_max_tres_minutes_per_dict = v0044_qos_limits_max_tres_minutes_per_instance.to_dict()
# create an instance of V0044QosLimitsMaxTresMinutesPer from a dict
v0044_qos_limits_max_tres_minutes_per_from_dict = V0044QosLimitsMaxTresMinutesPer.from_dict(v0044_qos_limits_max_tres_minutes_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


