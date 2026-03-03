# SlurmV0041PostJobSubmitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | Job batch script contents; Same as the script field in jobs[0] or job. | [optional] 
**jobs** | [**List[SlurmV0041PostJobSubmitRequestJobsInner]**](SlurmV0041PostJobSubmitRequestJobsInner.md) | HetJob description | [optional] 
**job** | [**SlurmV0041PostJobSubmitRequestJob**](SlurmV0041PostJobSubmitRequestJob.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit_request import SlurmV0041PostJobSubmitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmitRequest from a JSON string
slurm_v0041_post_job_submit_request_instance = SlurmV0041PostJobSubmitRequest.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmitRequest.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit_request_dict = slurm_v0041_post_job_submit_request_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmitRequest from a dict
slurm_v0041_post_job_submit_request_from_dict = SlurmV0041PostJobSubmitRequest.from_dict(slurm_v0041_post_job_submit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


