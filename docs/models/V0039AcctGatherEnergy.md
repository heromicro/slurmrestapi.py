# slurmrestapi.model.v0039_acct_gather_energy.V0039AcctGatherEnergy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**average_watts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**base_consumed_energy** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**consumed_energy** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**current_watts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**previous_consumed_energy** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**last_collected** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

