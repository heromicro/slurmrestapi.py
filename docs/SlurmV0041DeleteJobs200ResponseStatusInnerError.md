# SlurmV0041DeleteJobs200ResponseStatusInnerError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | **str** | String error encountered signaling job | [optional] 
**code** | **int** | Numeric error encountered signaling job | [optional] 
**message** | **str** | Error message why signaling job failed | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_delete_jobs200_response_status_inner_error import SlurmV0041DeleteJobs200ResponseStatusInnerError

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041DeleteJobs200ResponseStatusInnerError from a JSON string
slurm_v0041_delete_jobs200_response_status_inner_error_instance = SlurmV0041DeleteJobs200ResponseStatusInnerError.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041DeleteJobs200ResponseStatusInnerError.to_json())

# convert the object into a dict
slurm_v0041_delete_jobs200_response_status_inner_error_dict = slurm_v0041_delete_jobs200_response_status_inner_error_instance.to_dict()
# create an instance of SlurmV0041DeleteJobs200ResponseStatusInnerError from a dict
slurm_v0041_delete_jobs200_response_status_inner_error_from_dict = SlurmV0041DeleteJobs200ResponseStatusInnerError.from_dict(slurm_v0041_delete_jobs200_response_status_inner_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


