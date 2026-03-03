# SlurmV0041PostJobSubmit200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**SlurmV0041PostJobSubmit200ResponseResult**](SlurmV0041PostJobSubmit200ResponseResult.md) |  | [optional] 
**job_id** | **int** | Submitted Job ID | [optional] 
**step_id** | **str** | Submitted Step ID | [optional] 
**job_submit_user_msg** | **str** | Job submission user message | [optional] 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit200_response import SlurmV0041PostJobSubmit200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmit200Response from a JSON string
slurm_v0041_post_job_submit200_response_instance = SlurmV0041PostJobSubmit200Response.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmit200Response.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit200_response_dict = slurm_v0041_post_job_submit200_response_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmit200Response from a dict
slurm_v0041_post_job_submit200_response_from_dict = SlurmV0041PostJobSubmit200Response.from_dict(slurm_v0041_post_job_submit200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


