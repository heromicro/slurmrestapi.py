# SlurmV0041GetLicenses200ResponseLicensesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_name** | **str** | Name of the license | [optional] 
**total** | **int** | Total number of licenses present | [optional] 
**used** | **int** | Number of licenses in use | [optional] 
**free** | **int** | Number of licenses currently available | [optional] 
**remote** | **bool** | Indicates whether licenses are served by the database | [optional] 
**reserved** | **int** | Number of licenses reserved | [optional] 
**last_consumed** | **int** | Last known number of licenses that were consumed in the license manager (Remote Only) | [optional] 
**last_deficit** | **int** | Number of \&quot;missing licenses\&quot; from the cluster&#39;s perspective | [optional] 
**last_update** | **int** | When the license information was last updated (UNIX Timestamp) | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_licenses200_response_licenses_inner import SlurmV0041GetLicenses200ResponseLicensesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetLicenses200ResponseLicensesInner from a JSON string
slurm_v0041_get_licenses200_response_licenses_inner_instance = SlurmV0041GetLicenses200ResponseLicensesInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetLicenses200ResponseLicensesInner.to_json())

# convert the object into a dict
slurm_v0041_get_licenses200_response_licenses_inner_dict = slurm_v0041_get_licenses200_response_licenses_inner_instance.to_dict()
# create an instance of SlurmV0041GetLicenses200ResponseLicensesInner from a dict
slurm_v0041_get_licenses200_response_licenses_inner_from_dict = SlurmV0041GetLicenses200ResponseLicensesInner.from_dict(slurm_v0041_get_licenses200_response_licenses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


