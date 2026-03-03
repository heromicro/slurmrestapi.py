# V0044StepTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | Elapsed time in seconds | [optional] 
**end** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**start** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**suspended** | **int** | Total time in suspended state in seconds | [optional] 
**system** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeSystem**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeSystem.md) |  | [optional] 
**limit** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**total** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeTotal**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeTotal.md) |  | [optional] 
**user** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeUser**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTimeUser.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_step_time import V0044StepTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StepTime from a JSON string
v0044_step_time_instance = V0044StepTime.from_json(json)
# print the JSON string representation of the object
print(V0044StepTime.to_json())

# convert the object into a dict
v0044_step_time_dict = v0044_step_time_instance.to_dict()
# create an instance of V0044StepTime from a dict
v0044_step_time_from_dict = V0044StepTime.from_dict(v0044_step_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


