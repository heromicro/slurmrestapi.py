# slurmrestapi.model.v0037_node_allocation.V0037NodeAllocation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**memory** | decimal.Decimal, int,  | decimal.Decimal,  | amount of assigned job memory | [optional] 
**[cpus](#cpus)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | amount of assigned job CPUs | [optional] 
**[sockets](#sockets)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | assignment status of each socket by socket id | [optional] 
**[cores](#cores)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | assignment status of each core by core id | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cpus

amount of assigned job CPUs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | amount of assigned job CPUs | 

# sockets

assignment status of each socket by socket id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | assignment status of each socket by socket id | 

# cores

assignment status of each core by core id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | assignment status of each core by core id | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

