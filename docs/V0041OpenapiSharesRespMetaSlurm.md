# V0041OpenapiSharesRespMetaSlurm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**V0041OpenapiSharesRespMetaSlurmVersion**](V0041OpenapiSharesRespMetaSlurmVersion.md) |  | [optional] 
**release** | **str** | Slurm release string | [optional] 
**cluster** | **str** | Slurm cluster name | [optional] 

## Example

```python
from slurmrestapi.models.v0041_openapi_shares_resp_meta_slurm import V0041OpenapiSharesRespMetaSlurm

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSharesRespMetaSlurm from a JSON string
v0041_openapi_shares_resp_meta_slurm_instance = V0041OpenapiSharesRespMetaSlurm.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSharesRespMetaSlurm.to_json())

# convert the object into a dict
v0041_openapi_shares_resp_meta_slurm_dict = v0041_openapi_shares_resp_meta_slurm_instance.to_dict()
# create an instance of V0041OpenapiSharesRespMetaSlurm from a dict
v0041_openapi_shares_resp_meta_slurm_from_dict = V0041OpenapiSharesRespMetaSlurm.from_dict(v0041_openapi_shares_resp_meta_slurm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


