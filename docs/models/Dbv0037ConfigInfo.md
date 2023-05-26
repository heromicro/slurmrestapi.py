# slurmrestapi.model.dbv0037_config_info.Dbv0037ConfigInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | list, tuple,  | tuple,  | Slurm errors | [optional] 
**[tres](#tres)** | list, tuple,  | tuple,  | Array of TRES | [optional] 
**[accounts](#accounts)** | list, tuple,  | tuple,  | Array of accounts | [optional] 
**[associations](#associations)** | list, tuple,  | tuple,  | Array of associations | [optional] 
**[users](#users)** | list, tuple,  | tuple,  | Array of users | [optional] 
**[qos](#qos)** | list, tuple,  | tuple,  | Array of qos | [optional] 
**[wckeys](#wckeys)** | list, tuple,  | tuple,  | Array of wckeys | [optional] 
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

# tres

Array of TRES

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of TRES | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037TresList**](Dbv0037TresList.md) | [**Dbv0037TresList**](Dbv0037TresList.md) | [**Dbv0037TresList**](Dbv0037TresList.md) |  | 

# accounts

Array of accounts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of accounts | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037Account**](Dbv0037Account.md) | [**Dbv0037Account**](Dbv0037Account.md) | [**Dbv0037Account**](Dbv0037Account.md) |  | 

# associations

Array of associations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of associations | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037Association**](Dbv0037Association.md) | [**Dbv0037Association**](Dbv0037Association.md) | [**Dbv0037Association**](Dbv0037Association.md) |  | 

# users

Array of users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of users | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037User**](Dbv0037User.md) | [**Dbv0037User**](Dbv0037User.md) | [**Dbv0037User**](Dbv0037User.md) |  | 

# qos

Array of qos

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of qos | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037Qos**](Dbv0037Qos.md) | [**Dbv0037Qos**](Dbv0037Qos.md) | [**Dbv0037Qos**](Dbv0037Qos.md) |  | 

# wckeys

Array of wckeys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of wckeys | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037Wckey**](Dbv0037Wckey.md) | [**Dbv0037Wckey**](Dbv0037Wckey.md) | [**Dbv0037Wckey**](Dbv0037Wckey.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

