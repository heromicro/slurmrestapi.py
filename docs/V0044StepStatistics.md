# V0044StepStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsCPU**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerStatisticsCPU.md) |  | [optional] 
**energy** | [**V0044StepStatisticsEnergy**](V0044StepStatisticsEnergy.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_step_statistics import V0044StepStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StepStatistics from a JSON string
v0044_step_statistics_instance = V0044StepStatistics.from_json(json)
# print the JSON string representation of the object
print(V0044StepStatistics.to_json())

# convert the object into a dict
v0044_step_statistics_dict = v0044_step_statistics_instance.to_dict()
# create an instance of V0044StepStatistics from a dict
v0044_step_statistics_from_dict = V0044StepStatistics.from_dict(v0044_step_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


