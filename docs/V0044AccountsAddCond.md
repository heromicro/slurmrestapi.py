# V0044AccountsAddCond


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **List[str]** |  | 
**association** | [**V0044AssocRecSet**](V0044AssocRecSet.md) |  | [optional] 
**clusters** | **List[str]** |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_accounts_add_cond import V0044AccountsAddCond

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AccountsAddCond from a JSON string
v0044_accounts_add_cond_instance = V0044AccountsAddCond.from_json(json)
# print the JSON string representation of the object
print(V0044AccountsAddCond.to_json())

# convert the object into a dict
v0044_accounts_add_cond_dict = v0044_accounts_add_cond_instance.to_dict()
# create an instance of V0044AccountsAddCond from a dict
v0044_accounts_add_cond_from_dict = V0044AccountsAddCond.from_dict(v0044_accounts_add_cond_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


