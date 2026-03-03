# SlurmV0041PostJobSubmitRequestJobsInnerMemoryPerCpu

Minimum memory in megabytes per allocated CPU

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit_request_jobs_inner_memory_per_cpu import SlurmV0041PostJobSubmitRequestJobsInnerMemoryPerCpu

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerMemoryPerCpu from a JSON string
slurm_v0041_post_job_submit_request_jobs_inner_memory_per_cpu_instance = SlurmV0041PostJobSubmitRequestJobsInnerMemoryPerCpu.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmitRequestJobsInnerMemoryPerCpu.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit_request_jobs_inner_memory_per_cpu_dict = slurm_v0041_post_job_submit_request_jobs_inner_memory_per_cpu_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerMemoryPerCpu from a dict
slurm_v0041_post_job_submit_request_jobs_inner_memory_per_cpu_from_dict = SlurmV0041PostJobSubmitRequestJobsInnerMemoryPerCpu.from_dict(slurm_v0041_post_job_submit_request_jobs_inner_memory_per_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


