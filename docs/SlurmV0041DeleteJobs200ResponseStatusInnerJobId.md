# SlurmV0041DeleteJobs200ResponseStatusInnerJobId

Job ID that signaling failed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_delete_jobs200_response_status_inner_job_id import SlurmV0041DeleteJobs200ResponseStatusInnerJobId

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041DeleteJobs200ResponseStatusInnerJobId from a JSON string
slurm_v0041_delete_jobs200_response_status_inner_job_id_instance = SlurmV0041DeleteJobs200ResponseStatusInnerJobId.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041DeleteJobs200ResponseStatusInnerJobId.to_json())

# convert the object into a dict
slurm_v0041_delete_jobs200_response_status_inner_job_id_dict = slurm_v0041_delete_jobs200_response_status_inner_job_id_instance.to_dict()
# create an instance of SlurmV0041DeleteJobs200ResponseStatusInnerJobId from a dict
slurm_v0041_delete_jobs200_response_status_inner_job_id_from_dict = SlurmV0041DeleteJobs200ResponseStatusInnerJobId.from_dict(slurm_v0041_delete_jobs200_response_status_inner_job_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


