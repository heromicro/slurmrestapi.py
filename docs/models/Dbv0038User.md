# slurmrestapi.model.dbv0038_user.Dbv0038User

User description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | User description | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**administrator_level** | str,  | str,  | Description of administrator level | [optional] 
**[associations](#associations)** | list, tuple,  | tuple,  | Assigned associations | [optional] 
**[coordinators](#coordinators)** | list, tuple,  | tuple,  | List of assigned coordinators | [optional] 
**[default](#default)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Default settings | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  | List of properties of user | [optional] 
**name** | str,  | str,  | User name | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# associations

Assigned associations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Assigned associations | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0038AssociationShortInfo**](Dbv0038AssociationShortInfo.md) | [**Dbv0038AssociationShortInfo**](Dbv0038AssociationShortInfo.md) | [**Dbv0038AssociationShortInfo**](Dbv0038AssociationShortInfo.md) |  | 

# coordinators

List of assigned coordinators

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of assigned coordinators | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0038CoordinatorInfo**](Dbv0038CoordinatorInfo.md) | [**Dbv0038CoordinatorInfo**](Dbv0038CoordinatorInfo.md) | [**Dbv0038CoordinatorInfo**](Dbv0038CoordinatorInfo.md) |  | 

# default

Default settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Default settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | str,  | str,  | Default account name | [optional] 
**wckey** | str,  | str,  | Default wckey | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

List of properties of user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of properties of user | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | String of property name | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

