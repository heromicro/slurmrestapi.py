# SlurmV0041GetShares200ResponseMeta

Slurm meta values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | [**SlurmV0041GetShares200ResponseMetaPlugin**](SlurmV0041GetShares200ResponseMetaPlugin.md) |  | [optional] 
**client** | [**SlurmV0041GetShares200ResponseMetaClient**](SlurmV0041GetShares200ResponseMetaClient.md) |  | [optional] 
**command** | **List[str]** | CLI command (if applicable) | [optional] 
**slurm** | [**SlurmV0041GetShares200ResponseMetaSlurm**](SlurmV0041GetShares200ResponseMetaSlurm.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_meta import SlurmV0041GetShares200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseMeta from a JSON string
slurm_v0041_get_shares200_response_meta_instance = SlurmV0041GetShares200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseMeta.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_meta_dict = slurm_v0041_get_shares200_response_meta_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseMeta from a dict
slurm_v0041_get_shares200_response_meta_from_dict = SlurmV0041GetShares200ResponseMeta.from_dict(slurm_v0041_get_shares200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


