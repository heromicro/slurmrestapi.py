# slurmrestapi.model.dbv0038_qos.Dbv0038Qos

QOS description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | QOS description | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  | QOS description | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  | List of properties of QOS | [optional] 
**id** | str,  | str,  | Database id | [optional] 
**[limits](#limits)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Assigned limits | [optional] 
**[preempt](#preempt)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Preemption settings | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | QOS priority | [optional] 
**usage_factor** | decimal.Decimal, int, float,  | decimal.Decimal,  | Usage factor | [optional] 
**usage_threshold** | decimal.Decimal, int, float,  | decimal.Decimal,  | Usage threshold | [optional] 
**name** | str,  | str,  | Assigned name of QOS | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

List of properties of QOS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of properties of QOS | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | String of property name | 

# limits

Assigned limits

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Assigned limits | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**factor** | decimal.Decimal, int, float,  | decimal.Decimal,  | factor to apply to TRES count for associations using this QOS | [optional] 
**[max](#max)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on max settings | [optional] 
**[min](#min)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Min limit settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# max

Limits on max settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on max settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[wall_clock](#wall_clock)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limit on wallclock settings | [optional] 
**[jobs](#jobs)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on jobs settings | [optional] 
**[accruing](#accruing)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on accruing priority | [optional] 
**[tres](#tres)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on TRES | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# wall_clock

Limit on wallclock settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limit on wallclock settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limit on wallclock per settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# per

Limit on wallclock per settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limit on wallclock per settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**qos** | decimal.Decimal, int,  | decimal.Decimal,  | Max wallclock per QOS | [optional] 
**job** | decimal.Decimal, int,  | decimal.Decimal,  | Max wallclock per job | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# jobs

Limits on jobs settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on jobs settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[active_jobs](#active_jobs)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on active jobs settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# active_jobs

Limits on active jobs settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on active jobs settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on active jobs per settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# per

Limits on active jobs per settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on active jobs per settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | decimal.Decimal, int,  | decimal.Decimal,  | Max jobs per account | [optional] 
**user** | decimal.Decimal, int,  | decimal.Decimal,  | Max jobs per user | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accruing

Limits on accruing priority

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on accruing priority | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max accuring priority per setting | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# per

Max accuring priority per setting

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Max accuring priority per setting | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | decimal.Decimal, int,  | decimal.Decimal,  | Max accuring priority per account | [optional] 
**user** | decimal.Decimal, int,  | decimal.Decimal,  | Max accuring priority per user | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tres

Limits on TRES

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on TRES | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[minutes](#minutes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES minutes settings | [optional] 
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Max TRES per settings | [optional] 
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
**account** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**user** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**qos** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
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
**account** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**job** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**node** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**user** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# min

Min limit settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Min limit settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**priority_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | Min priority threshold | [optional] 
**[tres](#tres)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Min tres settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tres

Min tres settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Min tres settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[per](#per)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Min tres per settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# per

Min tres per settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Min tres per settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# preempt

Preemption settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Preemption settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[list](#list)** | list, tuple,  | tuple,  | List of preemptable QOS | [optional] 
**[mode](#mode)** | list, tuple,  | tuple,  | List of preemption modes | [optional] 
**exempt_time** | decimal.Decimal, int,  | decimal.Decimal,  | Grace period (s) before jobs can preempted | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# list

List of preemptable QOS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of preemptable QOS | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Preemptable QOS | 

# mode

List of preemption modes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of preemption modes | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Preemption mode | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

