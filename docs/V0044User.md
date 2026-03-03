# V0044User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_level** | **List[str]** | AdminLevel granted to the user | [optional] 
**associations** | [**List[V0044AssocShort]**](V0044AssocShort.md) |  | [optional] 
**coordinators** | [**List[V0044Coord]**](V0044Coord.md) |  | [optional] 
**default** | [**V0044UserDefault**](V0044UserDefault.md) |  | [optional] 
**flags** | **List[str]** | Flags associated with this user | [optional] 
**name** | **str** | User name | 
**old_name** | **str** | Previous user name | [optional] 
**wckeys** | [**List[V0044Wckey]**](V0044Wckey.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_user import V0044User

# TODO update the JSON string below
json = "{}"
# create an instance of V0044User from a JSON string
v0044_user_instance = V0044User.from_json(json)
# print the JSON string representation of the object
print(V0044User.to_json())

# convert the object into a dict
v0044_user_dict = v0044_user_instance.to_dict()
# create an instance of V0044User from a dict
v0044_user_from_dict = V0044User.from_dict(v0044_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


