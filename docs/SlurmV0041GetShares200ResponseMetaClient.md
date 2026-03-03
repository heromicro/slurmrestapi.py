# SlurmV0041GetShares200ResponseMetaClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Client source description | [optional] 
**user** | **str** | Client user (if known) | [optional] 
**group** | **str** | Client group (if known) | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_meta_client import SlurmV0041GetShares200ResponseMetaClient

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseMetaClient from a JSON string
slurm_v0041_get_shares200_response_meta_client_instance = SlurmV0041GetShares200ResponseMetaClient.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseMetaClient.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_meta_client_dict = slurm_v0041_get_shares200_response_meta_client_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseMetaClient from a dict
slurm_v0041_get_shares200_response_meta_client_from_dict = SlurmV0041GetShares200ResponseMetaClient.from_dict(slurm_v0041_get_shares200_response_meta_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


