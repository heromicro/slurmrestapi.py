# SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | Start of this entry in file | [optional] 
**end** | **int** | End of this entry in file | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit_request_jobs_inner_crontab_line import SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine from a JSON string
slurm_v0041_post_job_submit_request_jobs_inner_crontab_line_instance = SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit_request_jobs_inner_crontab_line_dict = slurm_v0041_post_job_submit_request_jobs_inner_crontab_line_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine from a dict
slurm_v0041_post_job_submit_request_jobs_inner_crontab_line_from_dict = SlurmV0041PostJobSubmitRequestJobsInnerCrontabLine.from_dict(slurm_v0041_post_job_submit_request_jobs_inner_crontab_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


