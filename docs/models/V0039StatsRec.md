# slurmrestapi.model.v0039_stats_rec.V0039StatsRec

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**time_start** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**rollups** | [**V0039RollupStats**](V0039RollupStats.md) | [**V0039RollupStats**](V0039RollupStats.md) |  | [optional] 
**RPCs** | [**V0039StatsRpcList**](V0039StatsRpcList.md) | [**V0039StatsRpcList**](V0039StatsRpcList.md) |  | [optional] 
**users** | [**V0039StatsUserList**](V0039StatsUserList.md) | [**V0039StatsUserList**](V0039StatsUserList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

