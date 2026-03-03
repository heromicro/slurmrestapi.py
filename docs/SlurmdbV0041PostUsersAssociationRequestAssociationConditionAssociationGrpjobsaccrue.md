# SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobsaccrue

Maximum number of pending jobs able to accrue age priority in this association and its children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_users_association_request_association_condition_association_grpjobsaccrue import SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobsaccrue

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobsaccrue from a JSON string
slurmdb_v0041_post_users_association_request_association_condition_association_grpjobsaccrue_instance = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobsaccrue.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobsaccrue.to_json())

# convert the object into a dict
slurmdb_v0041_post_users_association_request_association_condition_association_grpjobsaccrue_dict = slurmdb_v0041_post_users_association_request_association_condition_association_grpjobsaccrue_instance.to_dict()
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobsaccrue from a dict
slurmdb_v0041_post_users_association_request_association_condition_association_grpjobsaccrue_from_dict = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobsaccrue.from_dict(slurmdb_v0041_post_users_association_request_association_condition_association_grpjobsaccrue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


