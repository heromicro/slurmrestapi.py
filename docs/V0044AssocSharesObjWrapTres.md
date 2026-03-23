# V0044AssocSharesObjWrapTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_seconds** | [**List[V0044SharesUint64Tres]**](V0044SharesUint64Tres.md) |  | [optional] 
**group_minutes** | [**List[V0044SharesUint64Tres]**](V0044SharesUint64Tres.md) |  | [optional] 
**usage** | [**List[V0044SharesFloat128Tres]**](V0044SharesFloat128Tres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_assoc_shares_obj_wrap_tres import V0044AssocSharesObjWrapTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AssocSharesObjWrapTres from a JSON string
v0044_assoc_shares_obj_wrap_tres_instance = V0044AssocSharesObjWrapTres.from_json(json)
# print the JSON string representation of the object
print(V0044AssocSharesObjWrapTres.to_json())

# convert the object into a dict
v0044_assoc_shares_obj_wrap_tres_dict = v0044_assoc_shares_obj_wrap_tres_instance.to_dict()
# create an instance of V0044AssocSharesObjWrapTres from a dict
v0044_assoc_shares_obj_wrap_tres_from_dict = V0044AssocSharesObjWrapTres.from_dict(v0044_assoc_shares_obj_wrap_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


