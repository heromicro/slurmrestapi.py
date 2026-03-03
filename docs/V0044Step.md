# V0044Step


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**V0044StepTime**](V0044StepTime.md) |  | [optional] 
**exit_code** | [**V0044ProcessExitCodeVerbose**](V0044ProcessExitCodeVerbose.md) |  | [optional] 
**nodes** | [**V0044StepNodes**](V0044StepNodes.md) |  | [optional] 
**tasks** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTasks**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTasks.md) |  | [optional] 
**pid** | **str** | Deprecated; Process ID | [optional] 
**cpu** | [**V0044StepCPU**](V0044StepCPU.md) |  | [optional] 
**kill_request_user** | **str** | User ID that requested termination of the step | [optional] 
**state** | **List[str]** | Current state | [optional] 
**statistics** | [**V0044StepStatistics**](V0044StepStatistics.md) |  | [optional] 
**step** | [**V0044StepStep**](V0044StepStep.md) |  | [optional] 
**task** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTask**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTask.md) |  | [optional] 
**tres** | [**V0044StepTres**](V0044StepTres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_step import V0044Step

# TODO update the JSON string below
json = "{}"
# create an instance of V0044Step from a JSON string
v0044_step_instance = V0044Step.from_json(json)
# print the JSON string representation of the object
print(V0044Step.to_json())

# convert the object into a dict
v0044_step_dict = v0044_step_instance.to_dict()
# create an instance of V0044Step from a dict
v0044_step_from_dict = V0044Step.from_dict(v0044_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


