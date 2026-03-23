# V0041OpenapiSharesRespMeta

Slurm meta values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | [**V0041OpenapiSharesRespMetaPlugin**](V0041OpenapiSharesRespMetaPlugin.md) |  | [optional] 
**client** | [**V0041OpenapiSharesRespMetaClient**](V0041OpenapiSharesRespMetaClient.md) |  | [optional] 
**command** | **List[str]** | CLI command (if applicable) | [optional] 
**slurm** | [**V0041OpenapiSharesRespMetaSlurm**](V0041OpenapiSharesRespMetaSlurm.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0041_openapi_shares_resp_meta import V0041OpenapiSharesRespMeta

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSharesRespMeta from a JSON string
v0041_openapi_shares_resp_meta_instance = V0041OpenapiSharesRespMeta.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSharesRespMeta.to_json())

# convert the object into a dict
v0041_openapi_shares_resp_meta_dict = v0041_openapi_shares_resp_meta_instance.to_dict()
# create an instance of V0041OpenapiSharesRespMeta from a dict
v0041_openapi_shares_resp_meta_from_dict = V0041OpenapiSharesRespMeta.from_dict(v0041_openapi_shares_resp_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


