# SlurmV0041DeleteJobs200ResponseStatusInner

List of jobs signal responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**SlurmV0041DeleteJobs200ResponseStatusInnerError**](SlurmV0041DeleteJobs200ResponseStatusInnerError.md) |  | [optional] 
**step_id** | **str** | Job or Step ID that signaling failed | 
**job_id** | [**SlurmV0041DeleteJobs200ResponseStatusInnerJobId**](SlurmV0041DeleteJobs200ResponseStatusInnerJobId.md) |  | 
**federation** | [**SlurmV0041DeleteJobs200ResponseStatusInnerFederation**](SlurmV0041DeleteJobs200ResponseStatusInnerFederation.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_delete_jobs200_response_status_inner import SlurmV0041DeleteJobs200ResponseStatusInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041DeleteJobs200ResponseStatusInner from a JSON string
slurm_v0041_delete_jobs200_response_status_inner_instance = SlurmV0041DeleteJobs200ResponseStatusInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041DeleteJobs200ResponseStatusInner.to_json())

# convert the object into a dict
slurm_v0041_delete_jobs200_response_status_inner_dict = slurm_v0041_delete_jobs200_response_status_inner_instance.to_dict()
# create an instance of SlurmV0041DeleteJobs200ResponseStatusInner from a dict
slurm_v0041_delete_jobs200_response_status_inner_from_dict = SlurmV0041DeleteJobs200ResponseStatusInner.from_dict(slurm_v0041_delete_jobs200_response_status_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


