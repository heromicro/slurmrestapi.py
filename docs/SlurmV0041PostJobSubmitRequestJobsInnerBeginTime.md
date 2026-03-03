# SlurmV0041PostJobSubmitRequestJobsInnerBeginTime

Defer the allocation of the job until the specified time (UNIX timestamp)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit_request_jobs_inner_begin_time import SlurmV0041PostJobSubmitRequestJobsInnerBeginTime

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerBeginTime from a JSON string
slurm_v0041_post_job_submit_request_jobs_inner_begin_time_instance = SlurmV0041PostJobSubmitRequestJobsInnerBeginTime.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmitRequestJobsInnerBeginTime.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit_request_jobs_inner_begin_time_dict = slurm_v0041_post_job_submit_request_jobs_inner_begin_time_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerBeginTime from a dict
slurm_v0041_post_job_submit_request_jobs_inner_begin_time_from_dict = SlurmV0041PostJobSubmitRequestJobsInnerBeginTime.from_dict(slurm_v0041_post_job_submit_request_jobs_inner_begin_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


