# SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxsubmitjobs

Maximum number of jobs which can be in a pending or running state at any time in this association

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_users_association_request_association_condition_association_maxsubmitjobs import SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxsubmitjobs

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxsubmitjobs from a JSON string
slurmdb_v0041_post_users_association_request_association_condition_association_maxsubmitjobs_instance = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxsubmitjobs.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxsubmitjobs.to_json())

# convert the object into a dict
slurmdb_v0041_post_users_association_request_association_condition_association_maxsubmitjobs_dict = slurmdb_v0041_post_users_association_request_association_condition_association_maxsubmitjobs_instance.to_dict()
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxsubmitjobs from a dict
slurmdb_v0041_post_users_association_request_association_condition_association_maxsubmitjobs_from_dict = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxsubmitjobs.from_dict(slurmdb_v0041_post_users_association_request_association_condition_association_maxsubmitjobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


