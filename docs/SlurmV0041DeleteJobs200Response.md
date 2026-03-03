# SlurmV0041DeleteJobs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**List[SlurmV0041DeleteJobs200ResponseStatusInner]**](SlurmV0041DeleteJobs200ResponseStatusInner.md) | resultant status of signal request | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_delete_jobs200_response import SlurmV0041DeleteJobs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041DeleteJobs200Response from a JSON string
slurm_v0041_delete_jobs200_response_instance = SlurmV0041DeleteJobs200Response.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041DeleteJobs200Response.to_json())

# convert the object into a dict
slurm_v0041_delete_jobs200_response_dict = slurm_v0041_delete_jobs200_response_instance.to_dict()
# create an instance of SlurmV0041DeleteJobs200Response from a dict
slurm_v0041_delete_jobs200_response_from_dict = SlurmV0041DeleteJobs200Response.from_dict(slurm_v0041_delete_jobs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


