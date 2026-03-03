# SlurmdbV0041PostUsersAssociationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_condition** | [**SlurmdbV0041PostUsersAssociationRequestAssociationCondition**](SlurmdbV0041PostUsersAssociationRequestAssociationCondition.md) |  | 
**user** | [**SlurmdbV0041PostUsersAssociationRequestUser**](SlurmdbV0041PostUsersAssociationRequestUser.md) |  | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_users_association_request import SlurmdbV0041PostUsersAssociationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostUsersAssociationRequest from a JSON string
slurmdb_v0041_post_users_association_request_instance = SlurmdbV0041PostUsersAssociationRequest.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostUsersAssociationRequest.to_json())

# convert the object into a dict
slurmdb_v0041_post_users_association_request_dict = slurmdb_v0041_post_users_association_request_instance.to_dict()
# create an instance of SlurmdbV0041PostUsersAssociationRequest from a dict
slurmdb_v0041_post_users_association_request_from_dict = SlurmdbV0041PostUsersAssociationRequest.from_dict(slurmdb_v0041_post_users_association_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


