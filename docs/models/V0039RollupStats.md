# slurmrestapi.model.v0039_rollup_stats.V0039RollupStats

list of recorded rollup statistics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | list of recorded rollup statistics | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | recorded rollup statistics | 

# items

recorded rollup statistics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | recorded rollup statistics | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | type | [optional] must be one of ["internal", "user", "unknown", ] 
**last run** | decimal.Decimal, int,  | decimal.Decimal,  | Last time rollup ran (UNIX timestamp) | [optional] value must be a 32 bit integer
**max_cycle** | decimal.Decimal, int,  | decimal.Decimal,  | longest rollup time (seconds) | [optional] value must be a 64 bit integer
**total_time** | decimal.Decimal, int,  | decimal.Decimal,  | total time spent doing rollups (seconds) | [optional] value must be a 64 bit integer
**total_cycles** | decimal.Decimal, int,  | decimal.Decimal,  | number of rollups since last_run | [optional] value must be a 64 bit integer
**mean_cycles** | decimal.Decimal, int,  | decimal.Decimal,  | average time for rollup (seconds) | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

