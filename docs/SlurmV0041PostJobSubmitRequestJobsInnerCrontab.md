# SlurmV0041PostJobSubmitRequestJobsInnerCrontab

Specification for scrontab job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **List[str]** | Flags | [optional] 
**minute** | **str** | Ranged string specifying eligible minute values (e.g. 0-10,50) | [optional] 
**hour** | **str** | Ranged string specifying eligible hour values (e.g. 0-5,23) | [optional] 
**day_of_month** | **str** | Ranged string specifying eligible day of month values (e.g. 0-10,29) | [optional] 
**month** | **str** | Ranged string specifying eligible month values (e.g. 0-5,12) | [optional] 
**day_of_week** | **str** | Ranged string specifying eligible day of week values (e.g.0-3,7) | [optional] 
**specification** | **str** | Time specification (* means valid for all allowed values) - minute hour day_of_month month day_of_week | [optional] 
**command** | **str** | Command to run | [optional] 
**line** | [**SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine**](SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit_request_jobs_inner_crontab import SlurmV0041PostJobSubmitRequestJobsInnerCrontab

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerCrontab from a JSON string
slurm_v0041_post_job_submit_request_jobs_inner_crontab_instance = SlurmV0041PostJobSubmitRequestJobsInnerCrontab.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmitRequestJobsInnerCrontab.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit_request_jobs_inner_crontab_dict = slurm_v0041_post_job_submit_request_jobs_inner_crontab_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerCrontab from a dict
slurm_v0041_post_job_submit_request_jobs_inner_crontab_from_dict = SlurmV0041PostJobSubmitRequestJobsInnerCrontab.from_dict(slurm_v0041_post_job_submit_request_jobs_inner_crontab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


