# slurmrestapi.model.v0039_job_array_response_msg.V0039JobArrayResponseMsg

Result per ArrayJob

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Result per ArrayJob | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | ArrayJob | 

# items

ArrayJob

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArrayJob | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  | JobId | [optional] value must be a 32 bit integer
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  | numeric error code | [optional] value must be a 32 bit integer
**error** | str,  | str,  | error code description | [optional] 
**why** | str,  | str,  | error message | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

