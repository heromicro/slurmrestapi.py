# V0044Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[V0044AssocShort]**](V0044AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0044Coord]**](V0044Coord.md) |  | [optional] 
**description** | **str** | Arbitrary string describing the account | 
**name** | **str** | Account name | 
**organization** | **str** | Organization to which the account belongs | 
**flags** | **List[str]** | Flags associated with this account | [optional] 

## Example

```python
from slurmrestapi.models.v0044_account import V0044Account

# TODO update the JSON string below
json = "{}"
# create an instance of V0044Account from a JSON string
v0044_account_instance = V0044Account.from_json(json)
# print the JSON string representation of the object
print(V0044Account.to_json())

# convert the object into a dict
v0044_account_dict = v0044_account_instance.to_dict()
# create an instance of V0044Account from a dict
v0044_account_from_dict = V0044Account.from_dict(v0044_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


