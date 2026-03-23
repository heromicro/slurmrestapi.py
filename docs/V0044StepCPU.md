# V0044StepCPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_frequency** | [**V0044StepCPURequestedFrequency**](V0044StepCPURequestedFrequency.md) |  | [optional] 
**governor** | **str** | Requested CPU frequency governor in kHz | [optional] 

## Example

```python
from slurmrestapi.models.v0044_step_cpu import V0044StepCPU

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StepCPU from a JSON string
v0044_step_cpu_instance = V0044StepCPU.from_json(json)
# print the JSON string representation of the object
print(V0044StepCPU.to_json())

# convert the object into a dict
v0044_step_cpu_dict = v0044_step_cpu_instance.to_dict()
# create an instance of V0044StepCPU from a dict
v0044_step_cpu_from_dict = V0044StepCPU.from_dict(v0044_step_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


