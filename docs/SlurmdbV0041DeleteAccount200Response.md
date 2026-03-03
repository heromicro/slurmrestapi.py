# SlurmdbV0041DeleteAccount200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**removed_accounts** | **List[str]** | removed_accounts | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_delete_account200_response import SlurmdbV0041DeleteAccount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041DeleteAccount200Response from a JSON string
slurmdb_v0041_delete_account200_response_instance = SlurmdbV0041DeleteAccount200Response.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041DeleteAccount200Response.to_json())

# convert the object into a dict
slurmdb_v0041_delete_account200_response_dict = slurmdb_v0041_delete_account200_response_instance.to_dict()
# create an instance of SlurmdbV0041DeleteAccount200Response from a dict
slurmdb_v0041_delete_account200_response_from_dict = SlurmdbV0041DeleteAccount200Response.from_dict(slurmdb_v0041_delete_account200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


