# slurmrestapi.model.v0037_job_resources.V0037JobResources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**nodes** | str,  | str,  | list of assigned job nodes | [optional] 
**allocated_cpus** | decimal.Decimal, int,  | decimal.Decimal,  | number of assigned job cpus | [optional] 
**allocated_hosts** | decimal.Decimal, int,  | decimal.Decimal,  | number of assigned job hosts | [optional] 
**[allocated_nodes](#allocated_nodes)** | list, tuple,  | tuple,  | node allocations | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# allocated_nodes

node allocations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | node allocations | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V0037NodeAllocation**](V0037NodeAllocation.md) | [**V0037NodeAllocation**](V0037NodeAllocation.md) | [**V0037NodeAllocation**](V0037NodeAllocation.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

