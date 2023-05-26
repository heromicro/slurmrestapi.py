# slurmrestapi.model.v0039_node.V0039Node

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**architecture** | str,  | str,  |  | [optional] 
**burstbuffer_network_address** | str,  | str,  |  | [optional] 
**boards** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**boot_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**cluster_name** | str,  | str,  |  | [optional] 
**cores** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**specialized_cores** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**cpu_binding** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**cpu_load** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**free_mem** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**cpus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**effective_cpus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**specialized_cpus** | str,  | str,  |  | [optional] 
**energy** | [**V0039AcctGatherEnergy**](V0039AcctGatherEnergy.md) | [**V0039AcctGatherEnergy**](V0039AcctGatherEnergy.md) |  | [optional] 
**external_sensors** | [**V0039ExtSensorsData**](V0039ExtSensorsData.md) | [**V0039ExtSensorsData**](V0039ExtSensorsData.md) |  | [optional] 
**extra** | str,  | str,  |  | [optional] 
**power** | [**V0039PowerMgmtData**](V0039PowerMgmtData.md) | [**V0039PowerMgmtData**](V0039PowerMgmtData.md) |  | [optional] 
**features** | [**V0039CsvList**](V0039CsvList.md) | [**V0039CsvList**](V0039CsvList.md) |  | [optional] 
**active_features** | [**V0039CsvList**](V0039CsvList.md) | [**V0039CsvList**](V0039CsvList.md) |  | [optional] 
**gres** | str,  | str,  |  | [optional] 
**gres_drained** | str,  | str,  |  | [optional] 
**gres_used** | str,  | str,  |  | [optional] 
**last_busy** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**mcs_label** | str,  | str,  |  | [optional] 
**specialized_memory** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**name** | str,  | str,  |  | [optional] 
**[next_state_after_reboot](#next_state_after_reboot)** | list, tuple,  | tuple,  |  | [optional] 
**address** | str,  | str,  |  | [optional] 
**hostname** | str,  | str,  |  | [optional] 
**[state](#state)** | list, tuple,  | tuple,  |  | [optional] 
**operating_system** | str,  | str,  |  | [optional] 
**owner** | str,  | str,  |  | [optional] 
**partitions** | [**V0039CsvList**](V0039CsvList.md) | [**V0039CsvList**](V0039CsvList.md) |  | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**real_memory** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**comment** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**reason_changed_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**reason_set_by_user** | str,  | str,  |  | [optional] 
**resume_after** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**reservation** | str,  | str,  |  | [optional] 
**alloc_memory** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**alloc_cpus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**alloc_idle_cpus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**tres_used** | str,  | str,  |  | [optional] 
**tres_weighted** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**slurmd_start_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**sockets** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**threads** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**temporary_disk** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**weight** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**tres** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# next_state_after_reboot

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["INVALID", "UNKNOWN", "DOWN", "IDLE", "ALLOCATED", "ERROR", "MIXED", "FUTURE", "PERFCTRS", "RESERVED", "UNDRAIN", "CLOUD", "RESUME", "DRAIN", "COMPLETING", "NOT_RESPONDING", "POWERED_DOWN", "FAIL", "POWERING_UP", "MAINTENANCE", "REBOOT_REQUESTED", "REBOOT_CANCELED", "POWERING_DOWN", "DYNAMIC_FUTURE", "REBOOT_ISSUED", "PLANNED", "INVALID_REG", "POWER_DOWN", "POWER_UP", "POWER_DRAIN", "DYNAMIC_NORM", ] 

# state

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["INVALID", "UNKNOWN", "DOWN", "IDLE", "ALLOCATED", "ERROR", "MIXED", "FUTURE", "PERFCTRS", "RESERVED", "UNDRAIN", "CLOUD", "RESUME", "DRAIN", "COMPLETING", "NOT_RESPONDING", "POWERED_DOWN", "FAIL", "POWERING_UP", "MAINTENANCE", "REBOOT_REQUESTED", "REBOOT_CANCELED", "POWERING_DOWN", "DYNAMIC_FUTURE", "REBOOT_ISSUED", "PLANNED", "INVALID_REG", "POWER_DOWN", "POWER_UP", "POWER_DRAIN", "DYNAMIC_NORM", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

