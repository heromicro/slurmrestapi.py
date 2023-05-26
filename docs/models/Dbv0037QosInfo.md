# slurmrestapi.model.dbv0037_qos_info.Dbv0037QosInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | list, tuple,  | tuple,  | Slurm errors | [optional] 
**[qos](#qos)** | list, tuple,  | tuple,  | Array of QOS | [optional] 
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
[**Dbv0037Error**](Dbv0037Error.md) | [**Dbv0037Error**](Dbv0037Error.md) | [**Dbv0037Error**](Dbv0037Error.md) |  | 

# qos

Array of QOS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of QOS | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037Qos**](Dbv0037Qos.md) | [**Dbv0037Qos**](Dbv0037Qos.md) | [**Dbv0037Qos**](Dbv0037Qos.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

