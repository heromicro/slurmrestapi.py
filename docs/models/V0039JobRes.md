# slurmrestapi.model.v0039_job_res.V0039JobRes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**nodes** | str,  | str,  |  | [optional] 
**allocated_cores** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**allocated_cpus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**allocated_hosts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**allocated_nodes** | [**V0039JobResNodes**](V0039JobResNodes.md) | [**V0039JobResNodes**](V0039JobResNodes.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

