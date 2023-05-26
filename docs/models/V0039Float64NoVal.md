# slurmrestapi.model.v0039_float64_no_val.V0039Float64NoVal

64 bit floating point number with flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 64 bit floating point number with flags | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**set** | bool,  | BoolClass,  | True if number has been set. False if number is unset | [optional] if omitted the server will use the default value of False
**infinite** | bool,  | BoolClass,  | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | decimal.Decimal, int, float,  | decimal.Decimal,  | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

