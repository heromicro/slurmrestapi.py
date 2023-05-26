# slurmrestapi.model.v0039_user.V0039User

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**[administrator_level](#administrator_level)** | list, tuple,  | tuple,  |  | [optional] 
**associations** | [**V0039AssocShortList**](V0039AssocShortList.md) | [**V0039AssocShortList**](V0039AssocShortList.md) |  | [optional] 
**coordinators** | [**V0039CoordList**](V0039CoordList.md) | [**V0039CoordList**](V0039CoordList.md) |  | [optional] 
**[default](#default)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  |  | [optional] 
**old_name** | str,  | str,  |  | [optional] 
**wckeys** | [**V0039WckeyList**](V0039WckeyList.md) | [**V0039WckeyList**](V0039WckeyList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# administrator_level

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["Not Set", "None", "Operator", "Administrator", ] 

# default

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wckey** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["NONE", "DELETED", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

