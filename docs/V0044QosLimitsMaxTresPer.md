# V0044QosLimitsMaxTresPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**job** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**node** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**user** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits_max_tres_per import V0044QosLimitsMaxTresPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimitsMaxTresPer from a JSON string
v0044_qos_limits_max_tres_per_instance = V0044QosLimitsMaxTresPer.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimitsMaxTresPer.to_json())

# convert the object into a dict
v0044_qos_limits_max_tres_per_dict = v0044_qos_limits_max_tres_per_instance.to_dict()
# create an instance of V0044QosLimitsMaxTresPer from a dict
v0044_qos_limits_max_tres_per_from_dict = V0044QosLimitsMaxTresPer.from_dict(v0044_qos_limits_max_tres_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


