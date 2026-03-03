# SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpsubmitjobs

Maximum number of jobs which can be in a pending or running state at any time in this association and its children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_users_association_request_association_condition_association_grpsubmitjobs import SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpsubmitjobs

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpsubmitjobs from a JSON string
slurmdb_v0041_post_users_association_request_association_condition_association_grpsubmitjobs_instance = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpsubmitjobs.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpsubmitjobs.to_json())

# convert the object into a dict
slurmdb_v0041_post_users_association_request_association_condition_association_grpsubmitjobs_dict = slurmdb_v0041_post_users_association_request_association_condition_association_grpsubmitjobs_instance.to_dict()
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpsubmitjobs from a dict
slurmdb_v0041_post_users_association_request_association_condition_association_grpsubmitjobs_from_dict = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpsubmitjobs.from_dict(slurmdb_v0041_post_users_association_request_association_condition_association_grpsubmitjobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


