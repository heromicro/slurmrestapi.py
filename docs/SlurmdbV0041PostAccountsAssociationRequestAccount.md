# SlurmdbV0041PostAccountsAssociationRequestAccount

Account organization and description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Arbitrary string describing the account | [optional] 
**organization** | **str** | Organization to which the account belongs | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_accounts_association_request_account import SlurmdbV0041PostAccountsAssociationRequestAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostAccountsAssociationRequestAccount from a JSON string
slurmdb_v0041_post_accounts_association_request_account_instance = SlurmdbV0041PostAccountsAssociationRequestAccount.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostAccountsAssociationRequestAccount.to_json())

# convert the object into a dict
slurmdb_v0041_post_accounts_association_request_account_dict = slurmdb_v0041_post_accounts_association_request_account_instance.to_dict()
# create an instance of SlurmdbV0041PostAccountsAssociationRequestAccount from a dict
slurmdb_v0041_post_accounts_association_request_account_from_dict = SlurmdbV0041PostAccountsAssociationRequestAccount.from_dict(slurmdb_v0041_post_accounts_association_request_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


