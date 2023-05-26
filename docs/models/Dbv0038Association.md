# slurmrestapi.model.dbv0038_association.Dbv0038Association

Association description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Association description | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | str,  | str,  | Assigned account | [optional] 
**cluster** | str,  | str,  | Assigned cluster | [optional] 
**[default](#default)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Default settings | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  | List of properties of association | [optional] 
**[max](#max)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max settings | [optional] 
**[min](#min)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Min settings | [optional] 
**parent_account** | str,  | str,  | Parent account name | [optional] 
**partition** | str,  | str,  | Assigned partition | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | Assigned priority | [optional] 
**shares_raw** | decimal.Decimal, int,  | decimal.Decimal,  | Raw fairshare shares | [optional] 
**[usage](#usage)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Association usage | [optional] 
**user** | str,  | str,  | Assigned user | [optional] 
**[QOS](#QOS)** | list, tuple,  | tuple,  | Assigned QOS | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# default

Default settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Default settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**qos** | str,  | str,  | Default QOS | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

List of properties of association

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of properties of association | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | String of property name | 

# max

Max settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[jobs](#jobs)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max jobs settings | [optional] 
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max per settings | [optional] 
**[tres](#tres)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# jobs

Max jobs settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max jobs settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max jobs per settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# per

Max jobs per settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max jobs per settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wall_clock** | decimal.Decimal, int,  | decimal.Decimal,  | Max wallclock per job | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# per

Max per settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max per settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[account](#account)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max per accounting settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# account

Max per accounting settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max per accounting settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wall_clock** | decimal.Decimal, int,  | decimal.Decimal,  | Max wallclock per account | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tres

Max TRES settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES per settings | [optional] 
**total** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**[minutes](#minutes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES minutes settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# per

Max TRES per settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES per settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**node** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# minutes

Max TRES minutes settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES minutes settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES minutes per settings | [optional] 
**total** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# per

Max TRES minutes per settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES minutes per settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# min

Min settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Min settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**priority_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | Min priority threshold | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# usage

Association usage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Association usage | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accrue_job_count** | decimal.Decimal, int,  | decimal.Decimal,  | Jobs accuring priority | [optional] 
**group_used_wallclock** | decimal.Decimal, int, float,  | decimal.Decimal,  | Group used wallclock time (s) | [optional] 
**fairshare_factor** | decimal.Decimal, int, float,  | decimal.Decimal,  | Fairshare factor | [optional] 
**fairshare_shares** | decimal.Decimal, int,  | decimal.Decimal,  | Fairshare shares | [optional] 
**normalized_priority** | decimal.Decimal, int,  | decimal.Decimal,  | Currently active jobs | [optional] 
**normalized_shares** | decimal.Decimal, int, float,  | decimal.Decimal,  | Normalized shares | [optional] 
**effective_normalized_usage** | decimal.Decimal, int, float,  | decimal.Decimal,  | Effective normalized usage | [optional] 
**raw_usage** | decimal.Decimal, int,  | decimal.Decimal,  | Raw usage | [optional] 
**job_count** | decimal.Decimal, int,  | decimal.Decimal,  | Total jobs submitted | [optional] 
**fairshare_level** | decimal.Decimal, int, float,  | decimal.Decimal,  | Fairshare level | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# QOS

Assigned QOS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Assigned QOS | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Assigned single QOS name | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

