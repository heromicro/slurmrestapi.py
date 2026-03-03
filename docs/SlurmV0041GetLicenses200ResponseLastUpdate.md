# SlurmV0041GetLicenses200ResponseLastUpdate

Time of last licenses change (UNIX timestamp)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_licenses200_response_last_update import SlurmV0041GetLicenses200ResponseLastUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetLicenses200ResponseLastUpdate from a JSON string
slurm_v0041_get_licenses200_response_last_update_instance = SlurmV0041GetLicenses200ResponseLastUpdate.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetLicenses200ResponseLastUpdate.to_json())

# convert the object into a dict
slurm_v0041_get_licenses200_response_last_update_dict = slurm_v0041_get_licenses200_response_last_update_instance.to_dict()
# create an instance of SlurmV0041GetLicenses200ResponseLastUpdate from a dict
slurm_v0041_get_licenses200_response_last_update_from_dict = SlurmV0041GetLicenses200ResponseLastUpdate.from_dict(slurm_v0041_get_licenses200_response_last_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


