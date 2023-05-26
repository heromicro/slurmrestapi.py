# slurmrestapi.model.dbv0039_response_associations_delete.Dbv0039ResponseAssociationsDelete

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**meta** | [**Dbv0039Meta**](Dbv0039Meta.md) | [**Dbv0039Meta**](Dbv0039Meta.md) |  | [optional] 
**errors** | [**Dbv0039Errors**](Dbv0039Errors.md) | [**Dbv0039Errors**](Dbv0039Errors.md) |  | [optional] 
**warnings** | [**Dbv0039Warnings**](Dbv0039Warnings.md) | [**Dbv0039Warnings**](Dbv0039Warnings.md) |  | [optional] 
**[removed_associations](#removed_associations)** | list, tuple,  | tuple,  | the associations | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# removed_associations

the associations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the associations | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

