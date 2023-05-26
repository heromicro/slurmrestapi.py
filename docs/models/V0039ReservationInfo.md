# slurmrestapi.model.v0039_reservation_info.V0039ReservationInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accounts** | str,  | str,  |  | [optional] 
**burst_buffer** | str,  | str,  |  | [optional] 
**core_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**core_specializations** | [**V0039ReservationInfoCoreSpec**](V0039ReservationInfoCoreSpec.md) | [**V0039ReservationInfoCoreSpec**](V0039ReservationInfoCoreSpec.md) |  | [optional] 
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**features** | str,  | str,  |  | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  |  | [optional] 
**groups** | str,  | str,  |  | [optional] 
**licenses** | str,  | str,  |  | [optional] 
**max_start_delay** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**name** | str,  | str,  |  | [optional] 
**node_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**node_list** | str,  | str,  |  | [optional] 
**partition** | str,  | str,  |  | [optional] 
**[purge_completed](#purge_completed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**watts** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**tres** | str,  | str,  |  | [optional] 
**users** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["MAINT", "NO_MAINT", "DAILY", "NO_DAILY", "WEEKLY", "NO_WEEKLY", "IGNORE_JOBS", "NO_IGNORE_JOBS", "ANY_NODES", "STATIC", "NO_STATIC", "PART_NODES", "NO_PART_NODES", "OVERLAP", "SPEC_NODES", "FIRST_CORES", "TIME_FLOAT", "REPLACE", "ALL_NODES", "PURGE_COMP", "WEEKDAY", "NO_WEEKDAY", "WEEKEND", "NO_WEEKEND", "FLEX", "NO_FLEX", "DURATION_PLUS", "DURATION_MINUS", "NO_HOLD_JOBS_AFTER_END", "NO_PURGE_COMP", "MAGNETIC", "SKIP", "HOURLY", "NO_HOURLY", "REOCCURRING", ] 

# purge_completed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**time** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

