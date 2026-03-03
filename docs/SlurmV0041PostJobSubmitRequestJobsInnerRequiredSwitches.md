# SlurmV0041PostJobSubmitRequestJobsInnerRequiredSwitches

Maximum number of switches

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit_request_jobs_inner_required_switches import SlurmV0041PostJobSubmitRequestJobsInnerRequiredSwitches

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerRequiredSwitches from a JSON string
slurm_v0041_post_job_submit_request_jobs_inner_required_switches_instance = SlurmV0041PostJobSubmitRequestJobsInnerRequiredSwitches.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmitRequestJobsInnerRequiredSwitches.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit_request_jobs_inner_required_switches_dict = slurm_v0041_post_job_submit_request_jobs_inner_required_switches_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerRequiredSwitches from a dict
slurm_v0041_post_job_submit_request_jobs_inner_required_switches_from_dict = SlurmV0041PostJobSubmitRequestJobsInnerRequiredSwitches.from_dict(slurm_v0041_post_job_submit_request_jobs_inner_required_switches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


