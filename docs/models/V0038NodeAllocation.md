# slurmrestapi.model.v0038_node_allocation.V0038NodeAllocation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**memory** | decimal.Decimal, int,  | decimal.Decimal,  | amount of assigned job memory | [optional] 
**cpus** | decimal.Decimal, int,  | decimal.Decimal,  | number of assigned job CPUs | [optional] 
**[sockets](#sockets)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | assignment status of each socket by numeric socket id | [optional] 
**nodename** | str,  | str,  | node name | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sockets

assignment status of each socket by numeric socket id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | assignment status of each socket by numeric socket id | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[cores](#cores)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | assignment status of each core by core id in each socket | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cores

assignment status of each core by core id in each socket

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | assignment status of each core by core id in each socket | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

