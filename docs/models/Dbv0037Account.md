# slurmrestapi.model.dbv0037_account.Dbv0037Account

Account description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Account description | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[associations](#associations)** | list, tuple,  | tuple,  | List of assigned associations | [optional] 
**[coordinators](#coordinators)** | list, tuple,  | tuple,  | List of assigned coordinators | [optional] 
**description** | str,  | str,  | Description of account | [optional] 
**name** | str,  | str,  | Name of account | [optional] 
**organization** | str,  | str,  | Assigned organization of account | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  | List of properties of account | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# associations

List of assigned associations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of assigned associations | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037AssociationShortInfo**](Dbv0037AssociationShortInfo.md) | [**Dbv0037AssociationShortInfo**](Dbv0037AssociationShortInfo.md) | [**Dbv0037AssociationShortInfo**](Dbv0037AssociationShortInfo.md) |  | 

# coordinators

List of assigned coordinators

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of assigned coordinators | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037CoordinatorInfo**](Dbv0037CoordinatorInfo.md) | [**Dbv0037CoordinatorInfo**](Dbv0037CoordinatorInfo.md) | [**Dbv0037CoordinatorInfo**](Dbv0037CoordinatorInfo.md) |  | 

# flags

List of properties of account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of properties of account | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | String of property name | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

