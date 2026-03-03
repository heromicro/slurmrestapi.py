# V0044SharesUint64Tres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | TRES name | [optional] 
**value** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_shares_uint64_tres import V0044SharesUint64Tres

# TODO update the JSON string below
json = "{}"
# create an instance of V0044SharesUint64Tres from a JSON string
v0044_shares_uint64_tres_instance = V0044SharesUint64Tres.from_json(json)
# print the JSON string representation of the object
print(V0044SharesUint64Tres.to_json())

# convert the object into a dict
v0044_shares_uint64_tres_dict = v0044_shares_uint64_tres_instance.to_dict()
# create an instance of V0044SharesUint64Tres from a dict
v0044_shares_uint64_tres_from_dict = V0044SharesUint64Tres.from_dict(v0044_shares_uint64_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


