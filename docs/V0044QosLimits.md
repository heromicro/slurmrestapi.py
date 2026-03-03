# V0044QosLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_time** | **int** | GraceTime - Preemption grace time in seconds to be extended to a job which has been selected for preemption | [optional] 
**max** | [**V0044QosLimitsMax**](V0044QosLimitsMax.md) |  | [optional] 
**factor** | [**V0044Float64NoValStruct**](V0044Float64NoValStruct.md) |  | [optional] 
**min** | [**V0044QosLimitsMin**](V0044QosLimitsMin.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits import V0044QosLimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimits from a JSON string
v0044_qos_limits_instance = V0044QosLimits.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimits.to_json())

# convert the object into a dict
v0044_qos_limits_dict = v0044_qos_limits_instance.to_dict()
# create an instance of V0044QosLimits from a dict
v0044_qos_limits_from_dict = V0044QosLimits.from_dict(v0044_qos_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


