# slurmrestapi.model.v0039_power_mgmt_data.V0039PowerMgmtData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maximum_watts** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**current_watts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**total_energy** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**new_maximum_watts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**peak_watts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**lowest_watts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**new_job_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**state** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**time_start_day** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

