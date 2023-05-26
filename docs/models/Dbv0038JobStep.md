# slurmrestapi.model.dbv0038_job_step.Dbv0038JobStep

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[time](#time)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Time properties | [optional] 
**exit_code** | [**Dbv0038JobExitCode**](Dbv0038JobExitCode.md) | [**Dbv0038JobExitCode**](Dbv0038JobExitCode.md) |  | [optional] 
**[nodes](#nodes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node details | [optional] 
**[tasks](#tasks)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Task properties | [optional] 
**pid** | str,  | str,  | First process PID | [optional] 
**[CPU](#CPU)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | CPU properties | [optional] 
**kill_request_user** | str,  | str,  | User who requested job killed | [optional] 
**state** | str,  | str,  | State of job step | [optional] 
**[statistics](#statistics)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Statistics of job step | [optional] 
**[step](#step)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Step details | [optional] 
**task** | str,  | str,  | Task distribution properties | [optional] 
**[tres](#tres)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | TRES usage | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# time

Time properties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Time properties | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**elapsed** | decimal.Decimal, int,  | decimal.Decimal,  | Total time elapsed | [optional] 
**end** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp of when job ended | [optional] 
**start** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp of when job started | [optional] 
**suspended** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp of when job last suspended | [optional] 
**[system](#system)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | System time values | [optional] 
**[total](#total)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | System time values | [optional] 
**[user](#user)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | User land time values | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# system

System time values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | System time values | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**seconds** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of CPU-seconds used by the system on behalf of the process (in kernel mode), in seconds | [optional] 
**microseconds** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of CPU-seconds used by the system on behalf of the process (in kernel mode), in microseconds | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# total

System time values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | System time values | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**seconds** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of CPU-seconds used by the job, in seconds | [optional] 
**microseconds** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of CPU-seconds used by the job, in microseconds | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user

User land time values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | User land time values | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**seconds** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of CPU-seconds used by the job in user land, in seconds | [optional] 
**microseconds** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of CPU-seconds used by the job in user land, in microseconds | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nodes

Node details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of nodes in step | [optional] 
**range** | str,  | str,  | Nodes in step | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tasks

Task properties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Task properties | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of tasks in step | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# CPU

CPU properties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CPU properties | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[requested_frequency](#requested_frequency)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | CPU frequency requested | [optional] 
**[governor](#governor)** | list, tuple,  | tuple,  | CPU governor | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# requested_frequency

CPU frequency requested

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CPU frequency requested | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**min** | decimal.Decimal, int,  | decimal.Decimal,  | Min CPU frequency | [optional] 
**max** | decimal.Decimal, int,  | decimal.Decimal,  | Max CPU frequency | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# governor

CPU governor

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | CPU governor | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | CPU governor type | 

# statistics

Statistics of job step

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Statistics of job step | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[CPU](#CPU)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Statistics of CPU | [optional] 
**[energy](#energy)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Statistics of energy | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# CPU

Statistics of CPU

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Statistics of CPU | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**actual_frequency** | decimal.Decimal, int,  | decimal.Decimal,  | Actual frequency of CPU during step | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# energy

Statistics of energy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Statistics of energy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**consumed** | decimal.Decimal, int,  | decimal.Decimal,  | Energy consumed during step | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# step

Step details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Step details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  | Parent job id | [optional] 
**[het](#het)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Heterogeneous job details | [optional] 
**id** | str,  | str,  | Step id | [optional] 
**name** | str,  | str,  | Step name | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# het

Heterogeneous job details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Heterogeneous job details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**component** | decimal.Decimal, int,  | decimal.Decimal,  | Parent HetJob component id | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tres

TRES usage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TRES usage | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[requested](#requested)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | TRES requested for job | [optional] 
**[consumed](#consumed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | TRES requested for job | [optional] 
**allocated** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# requested

TRES requested for job

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TRES requested for job | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**average** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**max** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**min** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**total** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# consumed

TRES requested for job

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TRES requested for job | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**average** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**max** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**min** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**total** | [**Dbv0038TresList**](Dbv0038TresList.md) | [**Dbv0038TresList**](Dbv0038TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

