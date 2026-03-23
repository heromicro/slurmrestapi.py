# V0044Uint64NoValStruct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.v0044_uint64_no_val_struct import V0044Uint64NoValStruct

# TODO update the JSON string below
json = "{}"
# create an instance of V0044Uint64NoValStruct from a JSON string
v0044_uint64_no_val_struct_instance = V0044Uint64NoValStruct.from_json(json)
# print the JSON string representation of the object
print(V0044Uint64NoValStruct.to_json())

# convert the object into a dict
v0044_uint64_no_val_struct_dict = v0044_uint64_no_val_struct_instance.to_dict()
# create an instance of V0044Uint64NoValStruct from a dict
v0044_uint64_no_val_struct_from_dict = V0044Uint64NoValStruct.from_dict(v0044_uint64_no_val_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


