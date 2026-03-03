# SlurmV0041GetLicenses200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licenses** | [**List[SlurmV0041GetLicenses200ResponseLicensesInner]**](SlurmV0041GetLicenses200ResponseLicensesInner.md) | List of licenses | 
**last_update** | [**SlurmV0041GetLicenses200ResponseLastUpdate**](SlurmV0041GetLicenses200ResponseLastUpdate.md) |  | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_licenses200_response import SlurmV0041GetLicenses200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetLicenses200Response from a JSON string
slurm_v0041_get_licenses200_response_instance = SlurmV0041GetLicenses200Response.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetLicenses200Response.to_json())

# convert the object into a dict
slurm_v0041_get_licenses200_response_dict = slurm_v0041_get_licenses200_response_instance.to_dict()
# create an instance of SlurmV0041GetLicenses200Response from a dict
slurm_v0041_get_licenses200_response_from_dict = SlurmV0041GetLicenses200Response.from_dict(slurm_v0041_get_licenses200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


