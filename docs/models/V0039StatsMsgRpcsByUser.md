# slurmrestapi.model.v0039_stats_msg_rpcs_by_user.V0039StatsMsgRpcsByUser

RPCs by user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | RPCs by user | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | user | 

# items

user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | user | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user** | str,  | str,  | user name | [optional] 
**user_id** | decimal.Decimal, int,  | decimal.Decimal,  | user id (numeric) | [optional] value must be a 32 bit integer
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of RPCs received | [optional] value must be a 64 bit integer
**average_time** | decimal.Decimal, int,  | decimal.Decimal,  | Average time spent processing RPC in seconds | [optional] value must be a 64 bit integer
**total_time** | decimal.Decimal, int,  | decimal.Decimal,  | Total time spent processing RPC in seconds | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

