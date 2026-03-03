# SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh

Minimum priority required to reserve resources when scheduling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_users_association_request_association_condition_association_minpriothresh import SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh from a JSON string
slurmdb_v0041_post_users_association_request_association_condition_association_minpriothresh_instance = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh.to_json())

# convert the object into a dict
slurmdb_v0041_post_users_association_request_association_condition_association_minpriothresh_dict = slurmdb_v0041_post_users_association_request_association_condition_association_minpriothresh_instance.to_dict()
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh from a dict
slurmdb_v0041_post_users_association_request_association_condition_association_minpriothresh_from_dict = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh.from_dict(slurmdb_v0041_post_users_association_request_association_condition_association_minpriothresh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


