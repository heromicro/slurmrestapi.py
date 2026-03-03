# V0041OpenapiTresResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tres** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | TRES | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrestapi.models.v0041_openapi_tres_resp import V0041OpenapiTresResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiTresResp from a JSON string
v0041_openapi_tres_resp_instance = V0041OpenapiTresResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiTresResp.to_json())

# convert the object into a dict
v0041_openapi_tres_resp_dict = v0041_openapi_tres_resp_instance.to_dict()
# create an instance of V0041OpenapiTresResp from a dict
v0041_openapi_tres_resp_from_dict = V0041OpenapiTresResp.from_dict(v0041_openapi_tres_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


