# V0044StepCPURequestedFrequency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**max** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_step_cpu_requested_frequency import V0044StepCPURequestedFrequency

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StepCPURequestedFrequency from a JSON string
v0044_step_cpu_requested_frequency_instance = V0044StepCPURequestedFrequency.from_json(json)
# print the JSON string representation of the object
print(V0044StepCPURequestedFrequency.to_json())

# convert the object into a dict
v0044_step_cpu_requested_frequency_dict = v0044_step_cpu_requested_frequency_instance.to_dict()
# create an instance of V0044StepCPURequestedFrequency from a dict
v0044_step_cpu_requested_frequency_from_dict = V0044StepCPURequestedFrequency.from_dict(v0044_step_cpu_requested_frequency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


