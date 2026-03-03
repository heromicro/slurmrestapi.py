# V0041OpenapiResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiResp from a JSON string
v0041_openapi_resp_instance = V0041OpenapiResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiResp.to_json())

# convert the object into a dict
v0041_openapi_resp_dict = v0041_openapi_resp_instance.to_dict()
# create an instance of V0041OpenapiResp from a dict
v0041_openapi_resp_from_dict = V0041OpenapiResp.from_dict(v0041_openapi_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


