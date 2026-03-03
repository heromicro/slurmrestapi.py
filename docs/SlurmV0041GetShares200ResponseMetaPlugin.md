# SlurmV0041GetShares200ResponseMetaPlugin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Slurm plugin type (if applicable) | [optional] 
**name** | **str** | Slurm plugin name (if applicable) | [optional] 
**data_parser** | **str** | Slurm data_parser plugin | [optional] 
**accounting_storage** | **str** | Slurm accounting plugin | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_meta_plugin import SlurmV0041GetShares200ResponseMetaPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseMetaPlugin from a JSON string
slurm_v0041_get_shares200_response_meta_plugin_instance = SlurmV0041GetShares200ResponseMetaPlugin.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseMetaPlugin.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_meta_plugin_dict = slurm_v0041_get_shares200_response_meta_plugin_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseMetaPlugin from a dict
slurm_v0041_get_shares200_response_meta_plugin_from_dict = SlurmV0041GetShares200ResponseMetaPlugin.from_dict(slurm_v0041_get_shares200_response_meta_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


