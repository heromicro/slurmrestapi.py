# slurmrestapi.model.dbv0038_job_info.Dbv0038JobInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**meta** | [**Dbv0038Meta**](Dbv0038Meta.md) | [**Dbv0038Meta**](Dbv0038Meta.md) |  | [optional] 
**[errors](#errors)** | list, tuple,  | tuple,  | Slurm errors | [optional] 
**[jobs](#jobs)** | list, tuple,  | tuple,  | Array of jobs | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

Slurm errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Slurm errors | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0038Error**](Dbv0038Error.md) | [**Dbv0038Error**](Dbv0038Error.md) | [**Dbv0038Error**](Dbv0038Error.md) |  | 

# jobs

Array of jobs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of jobs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0038Job**](Dbv0038Job.md) | [**Dbv0038Job**](Dbv0038Job.md) | [**Dbv0038Job**](Dbv0038Job.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

