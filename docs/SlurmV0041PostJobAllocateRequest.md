# SlurmV0041PostJobAllocateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hetjob** | [**List[SlurmV0041PostJobSubmitRequestJobsInner]**](SlurmV0041PostJobSubmitRequestJobsInner.md) | HetJob description | [optional] 
**job** | [**SlurmV0041PostJobSubmitRequestJob**](SlurmV0041PostJobSubmitRequestJob.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_allocate_request import SlurmV0041PostJobAllocateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobAllocateRequest from a JSON string
slurm_v0041_post_job_allocate_request_instance = SlurmV0041PostJobAllocateRequest.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobAllocateRequest.to_json())

# convert the object into a dict
slurm_v0041_post_job_allocate_request_dict = slurm_v0041_post_job_allocate_request_instance.to_dict()
# create an instance of SlurmV0041PostJobAllocateRequest from a dict
slurm_v0041_post_job_allocate_request_from_dict = SlurmV0041PostJobAllocateRequest.from_dict(slurm_v0041_post_job_allocate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


