# slurmrestapi.model.v0039_assoc_usage.V0039AssocUsage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accrue_job_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**group_used_wallclock** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**fairshare_factor** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**fairshare_shares** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**normalized_priority** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**normalized_shares** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**effective_normalized_usage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**normalized_usage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**raw_usage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**active_jobs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**job_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**fairshare_level** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

