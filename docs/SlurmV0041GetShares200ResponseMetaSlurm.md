# SlurmV0041GetShares200ResponseMetaSlurm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**SlurmV0041GetShares200ResponseMetaSlurmVersion**](SlurmV0041GetShares200ResponseMetaSlurmVersion.md) |  | [optional] 
**release** | **str** | Slurm release string | [optional] 
**cluster** | **str** | Slurm cluster name | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_meta_slurm import SlurmV0041GetShares200ResponseMetaSlurm

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseMetaSlurm from a JSON string
slurm_v0041_get_shares200_response_meta_slurm_instance = SlurmV0041GetShares200ResponseMetaSlurm.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseMetaSlurm.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_meta_slurm_dict = slurm_v0041_get_shares200_response_meta_slurm_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseMetaSlurm from a dict
slurm_v0041_get_shares200_response_meta_slurm_from_dict = SlurmV0041GetShares200ResponseMetaSlurm.from_dict(slurm_v0041_get_shares200_response_meta_slurm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


