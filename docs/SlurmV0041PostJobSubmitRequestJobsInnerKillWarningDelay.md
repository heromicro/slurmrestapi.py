# SlurmV0041PostJobSubmitRequestJobsInnerKillWarningDelay

Number of seconds before end time to send the warning signal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit_request_jobs_inner_kill_warning_delay import SlurmV0041PostJobSubmitRequestJobsInnerKillWarningDelay

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerKillWarningDelay from a JSON string
slurm_v0041_post_job_submit_request_jobs_inner_kill_warning_delay_instance = SlurmV0041PostJobSubmitRequestJobsInnerKillWarningDelay.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmitRequestJobsInnerKillWarningDelay.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit_request_jobs_inner_kill_warning_delay_dict = slurm_v0041_post_job_submit_request_jobs_inner_kill_warning_delay_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerKillWarningDelay from a dict
slurm_v0041_post_job_submit_request_jobs_inner_kill_warning_delay_from_dict = SlurmV0041PostJobSubmitRequestJobsInnerKillWarningDelay.from_dict(slurm_v0041_post_job_submit_request_jobs_inner_kill_warning_delay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


