# SlurmdbV0041PostUsersAssociationRequestUser

Admin level of user, DefaultAccount, DefaultWCKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminlevel** | **List[str]** | AdminLevel granted to the user | [optional] 
**defaultaccount** | **str** | Default account | [optional] 
**defaultwckey** | **str** | Default WCKey | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_users_association_request_user import SlurmdbV0041PostUsersAssociationRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostUsersAssociationRequestUser from a JSON string
slurmdb_v0041_post_users_association_request_user_instance = SlurmdbV0041PostUsersAssociationRequestUser.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostUsersAssociationRequestUser.to_json())

# convert the object into a dict
slurmdb_v0041_post_users_association_request_user_dict = slurmdb_v0041_post_users_association_request_user_instance.to_dict()
# create an instance of SlurmdbV0041PostUsersAssociationRequestUser from a dict
slurmdb_v0041_post_users_association_request_user_from_dict = SlurmdbV0041PostUsersAssociationRequestUser.from_dict(slurmdb_v0041_post_users_association_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


