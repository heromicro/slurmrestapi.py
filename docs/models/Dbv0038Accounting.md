# slurmrestapi.model.dbv0038_accounting.Dbv0038Accounting

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allocated** | decimal.Decimal, int,  | decimal.Decimal,  | total seconds allocated | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | association/wckey ID | [optional] 
**start** | decimal.Decimal, int,  | decimal.Decimal,  | UNIX timestamp when accounting period started | [optional] 
**TRES** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

