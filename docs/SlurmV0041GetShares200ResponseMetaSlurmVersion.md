# SlurmV0041GetShares200ResponseMetaSlurmVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**major** | **str** | Slurm release major version | [optional] 
**micro** | **str** | Slurm release micro version | [optional] 
**minor** | **str** | Slurm release minor version | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_meta_slurm_version import SlurmV0041GetShares200ResponseMetaSlurmVersion

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseMetaSlurmVersion from a JSON string
slurm_v0041_get_shares200_response_meta_slurm_version_instance = SlurmV0041GetShares200ResponseMetaSlurmVersion.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseMetaSlurmVersion.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_meta_slurm_version_dict = slurm_v0041_get_shares200_response_meta_slurm_version_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseMetaSlurmVersion from a dict
slurm_v0041_get_shares200_response_meta_slurm_version_from_dict = SlurmV0041GetShares200ResponseMetaSlurmVersion.from_dict(slurm_v0041_get_shares200_response_meta_slurm_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


