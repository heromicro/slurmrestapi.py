# V0044QosLimitsMaxWallClockPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**job** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits_max_wall_clock_per import V0044QosLimitsMaxWallClockPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimitsMaxWallClockPer from a JSON string
v0044_qos_limits_max_wall_clock_per_instance = V0044QosLimitsMaxWallClockPer.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimitsMaxWallClockPer.to_json())

# convert the object into a dict
v0044_qos_limits_max_wall_clock_per_dict = v0044_qos_limits_max_wall_clock_per_instance.to_dict()
# create an instance of V0044QosLimitsMaxWallClockPer from a dict
v0044_qos_limits_max_wall_clock_per_from_dict = V0044QosLimitsMaxWallClockPer.from_dict(v0044_qos_limits_max_wall_clock_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


