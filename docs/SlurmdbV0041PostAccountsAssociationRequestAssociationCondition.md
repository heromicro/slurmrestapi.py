# SlurmdbV0041PostAccountsAssociationRequestAssociationCondition

CSV list of accounts, association limits and options, CSV list of clusters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **List[str]** | CSV accounts list | 
**association** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation.md) |  | [optional] 
**clusters** | **List[str]** | CSV clusters list | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_accounts_association_request_association_condition import SlurmdbV0041PostAccountsAssociationRequestAssociationCondition

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostAccountsAssociationRequestAssociationCondition from a JSON string
slurmdb_v0041_post_accounts_association_request_association_condition_instance = SlurmdbV0041PostAccountsAssociationRequestAssociationCondition.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostAccountsAssociationRequestAssociationCondition.to_json())

# convert the object into a dict
slurmdb_v0041_post_accounts_association_request_association_condition_dict = slurmdb_v0041_post_accounts_association_request_association_condition_instance.to_dict()
# create an instance of SlurmdbV0041PostAccountsAssociationRequestAssociationCondition from a dict
slurmdb_v0041_post_accounts_association_request_association_condition_from_dict = SlurmdbV0041PostAccountsAssociationRequestAssociationCondition.from_dict(slurmdb_v0041_post_accounts_association_request_association_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


