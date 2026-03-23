# V0041OpenapiSharesRespMetaPlugin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Slurm plugin type (if applicable) | [optional] 
**name** | **str** | Slurm plugin name (if applicable) | [optional] 
**data_parser** | **str** | Slurm data_parser plugin | [optional] 
**accounting_storage** | **str** | Slurm accounting plugin | [optional] 

## Example

```python
from slurmrestapi.models.v0041_openapi_shares_resp_meta_plugin import V0041OpenapiSharesRespMetaPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSharesRespMetaPlugin from a JSON string
v0041_openapi_shares_resp_meta_plugin_instance = V0041OpenapiSharesRespMetaPlugin.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSharesRespMetaPlugin.to_json())

# convert the object into a dict
v0041_openapi_shares_resp_meta_plugin_dict = v0041_openapi_shares_resp_meta_plugin_instance.to_dict()
# create an instance of V0041OpenapiSharesRespMetaPlugin from a dict
v0041_openapi_shares_resp_meta_plugin_from_dict = V0041OpenapiSharesRespMetaPlugin.from_dict(v0041_openapi_shares_resp_meta_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


