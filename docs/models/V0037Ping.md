# slurmrestapi.model.v0037_ping.V0037Ping

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hostname** | str,  | str,  | slurm controller hostname | [optional] 
**ping** | str,  | str,  | slurm controller host up | [optional] must be one of ["UP", "DOWN", ] 
**mode** | str,  | str,  | slurm controller mode | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  | slurm controller status | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

