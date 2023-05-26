# slurmrestapi.model.v0039_assoc.V0039Assoc

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user** | str,  | str,  |  | 
**account** | str,  | str,  |  | [optional] 
**cluster** | str,  | str,  |  | [optional] 
**[default](#default)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  |  | [optional] 
**[max](#max)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**is_default** | bool,  | BoolClass,  |  | [optional] 
**[min](#min)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**parent_account** | str,  | str,  |  | [optional] 
**partition** | str,  | str,  |  | [optional] 
**priority** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**qos** | [**V0039QosStringIdList**](V0039QosStringIdList.md) | [**V0039QosStringIdList**](V0039QosStringIdList.md) |  | [optional] 
**shares_raw** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**usage** | [**V0039AssocUsage**](V0039AssocUsage.md) | [**V0039AssocUsage**](V0039AssocUsage.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# default

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**qos** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["DELETED", ] 

# max

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[jobs](#jobs)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# jobs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# per

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wall_clock** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# min

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**priority_threshold** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

