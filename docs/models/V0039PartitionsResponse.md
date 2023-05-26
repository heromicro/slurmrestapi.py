# slurmrestapi.model.v0039_partitions_response.V0039PartitionsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**meta** | [**V0039Meta**](V0039Meta.md) | [**V0039Meta**](V0039Meta.md) |  | [optional] 
**errors** | [**V0039Errors**](V0039Errors.md) | [**V0039Errors**](V0039Errors.md) |  | [optional] 
**warnings** | [**V0039Warnings**](V0039Warnings.md) | [**V0039Warnings**](V0039Warnings.md) |  | [optional] 
**partitions** | [**V0039PartitionInfoArray**](V0039PartitionInfoArray.md) | [**V0039PartitionInfoArray**](V0039PartitionInfoArray.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

