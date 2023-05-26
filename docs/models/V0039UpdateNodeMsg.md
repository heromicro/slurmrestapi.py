# slurmrestapi.model.v0039_update_node_msg.V0039UpdateNodeMsg

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**comment** | str,  | str,  |  | [optional] 
**cpu_bind** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**extra** | str,  | str,  |  | [optional] 
**features** | [**V0039CsvList**](V0039CsvList.md) | [**V0039CsvList**](V0039CsvList.md) |  | [optional] 
**features_act** | [**V0039CsvList**](V0039CsvList.md) | [**V0039CsvList**](V0039CsvList.md) |  | [optional] 
**gres** | str,  | str,  |  | [optional] 
**address** | [**V0039HostlistString**](V0039HostlistString.md) | [**V0039HostlistString**](V0039HostlistString.md) |  | [optional] 
**hostname** | [**V0039HostlistString**](V0039HostlistString.md) | [**V0039HostlistString**](V0039HostlistString.md) |  | [optional] 
**name** | [**V0039HostlistString**](V0039HostlistString.md) | [**V0039HostlistString**](V0039HostlistString.md) |  | [optional] 
**[state](#state)** | list, tuple,  | tuple,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**reason_uid** | str,  | str,  |  | [optional] 
**resume_after** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**weight** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

