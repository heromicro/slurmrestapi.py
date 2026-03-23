# V0044QosLimitsMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**minutes** | [**V0044QosLimitsMaxTresMinutes**](V0044QosLimitsMaxTresMinutes.md) |  | [optional] 
**per** | [**V0044QosLimitsMaxTresPer**](V0044QosLimitsMaxTresPer.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits_max_tres import V0044QosLimitsMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimitsMaxTres from a JSON string
v0044_qos_limits_max_tres_instance = V0044QosLimitsMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimitsMaxTres.to_json())

# convert the object into a dict
v0044_qos_limits_max_tres_dict = v0044_qos_limits_max_tres_instance.to_dict()
# create an instance of V0044QosLimitsMaxTres from a dict
v0044_qos_limits_max_tres_from_dict = V0044QosLimitsMaxTres.from_dict(v0044_qos_limits_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


