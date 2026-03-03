# SlurmdbV0041PostUsersAssociationRequestAssociationCondition

Filters to select associations for users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **List[str]** | CSV accounts list | [optional] 
**association** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation.md) |  | [optional] 
**clusters** | **List[str]** | CSV clusters list | [optional] 
**partitions** | **List[str]** | CSV partitions list | [optional] 
**users** | **List[str]** | CSV users list | 
**wckeys** | **List[str]** | CSV WCKeys list | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_users_association_request_association_condition import SlurmdbV0041PostUsersAssociationRequestAssociationCondition

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationCondition from a JSON string
slurmdb_v0041_post_users_association_request_association_condition_instance = SlurmdbV0041PostUsersAssociationRequestAssociationCondition.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostUsersAssociationRequestAssociationCondition.to_json())

# convert the object into a dict
slurmdb_v0041_post_users_association_request_association_condition_dict = slurmdb_v0041_post_users_association_request_association_condition_instance.to_dict()
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationCondition from a dict
slurmdb_v0041_post_users_association_request_association_condition_from_dict = SlurmdbV0041PostUsersAssociationRequestAssociationCondition.from_dict(slurmdb_v0041_post_users_association_request_association_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


