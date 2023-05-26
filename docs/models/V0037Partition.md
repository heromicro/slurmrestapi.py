# slurmrestapi.model.v0037_partition.V0037Partition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[flags](#flags)** | list, tuple,  | tuple,  | partition options | [optional] 
**[preemption_mode](#preemption_mode)** | list, tuple,  | tuple,  | preemption type | [optional] 
**allowed_allocation_nodes** | str,  | str,  | list names of allowed allocating nodes | [optional] 
**allowed_accounts** | str,  | str,  | comma delimited list of accounts | [optional] 
**allowed_groups** | str,  | str,  | comma delimited list of groups | [optional] 
**allowed_qos** | str,  | str,  | comma delimited list of qos | [optional] 
**alternative** | str,  | str,  | name of alternate partition | [optional] 
**billing_weights** | str,  | str,  | TRES billing weights | [optional] 
**default_memory_per_cpu** | decimal.Decimal, int,  | decimal.Decimal,  | default MB memory per allocated CPU | [optional] value must be a 64 bit integer
**default_time_limit** | decimal.Decimal, int,  | decimal.Decimal,  | default time limit (minutes) | [optional] value must be a 64 bit integer
**denied_accounts** | str,  | str,  | comma delimited list of denied accounts | [optional] 
**denied_qos** | str,  | str,  | comma delimited list of denied qos | [optional] 
**preemption_grace_time** | decimal.Decimal, int,  | decimal.Decimal,  | preemption grace time (seconds) | [optional] value must be a 64 bit integer
**maximum_cpus_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | maximum allocated CPUs per node | [optional] 
**maximum_memory_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | maximum memory per allocated CPU (MiB) | [optional] value must be a 64 bit integer
**maximum_nodes_per_job** | decimal.Decimal, int,  | decimal.Decimal,  | Max nodes per job | [optional] 
**max_time_limit** | decimal.Decimal, int,  | decimal.Decimal,  | Max time limit per job | [optional] value must be a 64 bit integer
**min_nodes_per_job** | decimal.Decimal, int,  | decimal.Decimal,  | Min number of nodes per job | [optional] 
**name** | str,  | str,  | Partition name | [optional] 
**nodes** | str,  | str,  | list names of nodes in partition | [optional] 
**over_time_limit** | decimal.Decimal, int,  | decimal.Decimal,  | job&#x27;s time limit can be exceeded by this number of minutes before cancellation | [optional] 
**priority_job_factor** | decimal.Decimal, int,  | decimal.Decimal,  | job priority weight factor | [optional] 
**priority_tier** | decimal.Decimal, int,  | decimal.Decimal,  | tier for scheduling and preemption | [optional] 
**qos** | str,  | str,  | partition QOS name | [optional] 
**state** | str,  | str,  | Partition state | [optional] 
**total_cpus** | decimal.Decimal, int,  | decimal.Decimal,  | Total cpus in partition | [optional] 
**total_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of nodes in partition | [optional] 
**tres** | str,  | str,  | configured TRES in partition | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

partition options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | partition options | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# preemption_mode

preemption type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | preemption type | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

