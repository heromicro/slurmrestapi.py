# SlurmV0041PostJobSubmit200ResponseResult

Job submission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | New job ID | [optional] 
**step_id** | **str** | New job step ID | [optional] 
**error_code** | **int** | Error code | [optional] 
**error** | **str** | Error message | [optional] 
**job_submit_user_msg** | **str** | Message to user from job_submit plugin | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit200_response_result import SlurmV0041PostJobSubmit200ResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmit200ResponseResult from a JSON string
slurm_v0041_post_job_submit200_response_result_instance = SlurmV0041PostJobSubmit200ResponseResult.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmit200ResponseResult.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit200_response_result_dict = slurm_v0041_post_job_submit200_response_result_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmit200ResponseResult from a dict
slurm_v0041_post_job_submit200_response_result_from_dict = SlurmV0041PostJobSubmit200ResponseResult.from_dict(slurm_v0041_post_job_submit200_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


