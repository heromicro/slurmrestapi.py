# slurmrestapi.model.dbv0037_job.Dbv0037Job

Single job description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Single job description | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | str,  | str,  | Account charged by job | [optional] 
**[comment](#comment)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Job comments by type | [optional] 
**allocation_nodes** | str,  | str,  | Nodes allocated to job | [optional] 
**[array](#array)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Array properties (optional) | [optional] 
**[time](#time)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Time properties | [optional] 
**association** | [**Dbv0037AssociationShortInfo**](Dbv0037AssociationShortInfo.md) | [**Dbv0037AssociationShortInfo**](Dbv0037AssociationShortInfo.md) |  | [optional] 
**cluster** | str,  | str,  | Assigned cluster | [optional] 
**constraints** | str,  | str,  | Constraints on job | [optional] 
**derived_exit_code** | [**Dbv0037JobExitCode**](Dbv0037JobExitCode.md) | [**Dbv0037JobExitCode**](Dbv0037JobExitCode.md) |  | [optional] 
**exit_code** | [**Dbv0037JobExitCode**](Dbv0037JobExitCode.md) | [**Dbv0037JobExitCode**](Dbv0037JobExitCode.md) |  | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  | List of properties of job | [optional] 
**group** | str,  | str,  | User&#x27;s group to run job | [optional] 
**[het](#het)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Heterogeneous Job details (optional) | [optional] 
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  | Job id | [optional] 
**name** | str,  | str,  | Assigned job name | [optional] 
**[mcs](#mcs)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Multi-Category Security | [optional] 
**nodes** | str,  | str,  | List of nodes allocated for job | [optional] 
**partition** | str,  | str,  | Assigned job&#x27;s partition | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | Priority | [optional] 
**qos** | str,  | str,  | Assigned qos name | [optional] 
**[required](#required)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Job run requirements | [optional] 
**kill_request_user** | str,  | str,  | User who requested job killed | [optional] 
**[reservation](#reservation)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Reservation usage details | [optional] 
**[state](#state)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | State properties of job | [optional] 
**[steps](#steps)** | list, tuple,  | tuple,  | Job step description | [optional] 
**[tres](#tres)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | TRES settings | [optional] 
**user** | str,  | str,  | Job user | [optional] 
**[wckey](#wckey)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Job assigned wckey details | [optional] 
**working_directory** | str,  | str,  | Directory where job was initially started | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# comment

Job comments by type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Job comments by type | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**administrator** | str,  | str,  | Administrator set comment | [optional] 
**job** | str,  | str,  | Job comment | [optional] 
**system** | str,  | str,  | System set comment | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# array

Array properties (optional)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Array properties (optional) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  | Job id of array | [optional] 
**[limits](#limits)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on array settings | [optional] 
**task** | str,  | str,  | Array task | [optional] 
**task_id** | decimal.Decimal, int,  | decimal.Decimal,  | Array task id | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# limits

Limits on array settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on array settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[max](#max)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on array settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# max

Limits on array settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on array settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[running](#running)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on array settings | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# running

Limits on array settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Limits on array settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tasks** | decimal.Decimal, int,  | decimal.Decimal,  | Max running tasks in array at any one time | [optional] 
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
**eligible** | decimal.Decimal, int,  | decimal.Decimal,  | Total time eligible to run | [optional] 
**end** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp of when job ended | [optional] 
**start** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp of when job started | [optional] 
**submission** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp of when job submitted | [optional] 
**suspended** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp of when job last suspended | [optional] 
**[system](#system)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | System time values | [optional] 
**[total](#total)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | System time values | [optional] 
**[user](#user)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | User land time values | [optional] 
**limit** | decimal.Decimal, int,  | decimal.Decimal,  | Job wall clock time limit | [optional] 
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

# flags

List of properties of job

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of properties of job | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | String of property name | 

# het

Heterogeneous Job details (optional)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Heterogeneous Job details (optional) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[job_id](#job_id)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Parent HetJob id | [optional] 
**[job_offset](#job_offset)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Offset of this job to parent | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# job_id

Parent HetJob id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Parent HetJob id | 

# job_offset

Offset of this job to parent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Offset of this job to parent | 

# mcs

Multi-Category Security

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Multi-Category Security | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**label** | str,  | str,  | Assigned MCS label | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# required

Job run requirements

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Job run requirements | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**CPUs** | decimal.Decimal, int,  | decimal.Decimal,  | Required number of CPUs | [optional] 
**memory** | decimal.Decimal, int,  | decimal.Decimal,  | Required amount of memory (MiB) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# reservation

Reservation usage details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Reservation usage details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Database id of reservation | [optional] 
**name** | decimal.Decimal, int,  | decimal.Decimal,  | Name of reservation | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# state

State properties of job

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | State properties of job | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**current** | str,  | str,  | Current state of job | [optional] 
**reason** | str,  | str,  | Last reason job didn&#x27;t run | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# steps

Job step description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Job step description | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037JobStep**](Dbv0037JobStep.md) | [**Dbv0037JobStep**](Dbv0037JobStep.md) | [**Dbv0037JobStep**](Dbv0037JobStep.md) |  | 

# tres

TRES settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | TRES settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allocated** | [**Dbv0037TresList**](Dbv0037TresList.md) | [**Dbv0037TresList**](Dbv0037TresList.md) |  | [optional] 
**requested** | [**Dbv0037TresList**](Dbv0037TresList.md) | [**Dbv0037TresList**](Dbv0037TresList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# wckey

Job assigned wckey details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Job assigned wckey details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wckey** | str,  | str,  | Job assigned wckey | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  | wckey flags | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

wckey flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | wckey flags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Flag string | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

