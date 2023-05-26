# slurmrestapi.model.v0039_cron_entry.V0039CronEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[flags](#flags)** | list, tuple,  | tuple,  |  | [optional] 
**minute** | str,  | str,  |  | [optional] 
**hour** | str,  | str,  |  | [optional] 
**day_of_month** | str,  | str,  |  | [optional] 
**month** | str,  | str,  |  | [optional] 
**day_of_week** | str,  | str,  |  | [optional] 
**specification** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**[line](#line)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["WILD_MINUTE", "WILD_HOUR", "WILD_DAY_OF_MONTH", "WILD_MONTH", "WILD_DAY_OF_WEEK", ] 

# line

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**end** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

