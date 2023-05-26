# slurmrestapi.model.v0038_job_response_properties.V0038JobResponseProperties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | str,  | str,  | Charge resources used by this job to specified account | [optional] 
**accrue_time** | decimal.Decimal, int,  | decimal.Decimal,  | time job is eligible for running | [optional] value must be a 64 bit integer
**admin_comment** | str,  | str,  | administrator&#x27;s arbitrary comment | [optional] 
**array_job_id** | decimal.Decimal, int,  | decimal.Decimal,  | job_id of a job array or 0 if N/A | [optional] 
**array_task_id** | decimal.Decimal, int,  | decimal.Decimal,  | task_id of a job array | [optional] 
**array_max_tasks** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of running array tasks | [optional] 
**array_task_string** | str,  | str,  | string expression of task IDs in this record | [optional] 
**association_id** | decimal.Decimal, int,  | decimal.Decimal,  | association id for job | [optional] 
**batch_features** | str,  | str,  | features required for batch script&#x27;s node | [optional] 
**batch_flag** | bool,  | BoolClass,  | if batch: queued job with script | [optional] 
**batch_host** | str,  | str,  | name of host running batch script | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  | Job flags | [optional] 
**burst_buffer** | str,  | str,  | burst buffer specifications | [optional] 
**burst_buffer_state** | str,  | str,  | burst buffer state info | [optional] 
**cluster** | str,  | str,  | name of cluster that the job is on | [optional] 
**cluster_features** | str,  | str,  | comma separated list of required cluster features | [optional] 
**command** | str,  | str,  | command to be executed | [optional] 
**comment** | str,  | str,  | arbitrary comment | [optional] 
**container** | str,  | str,  | absolute path to OCI container bundle | [optional] 
**contiguous** | bool,  | BoolClass,  | job requires contiguous nodes | [optional] 
**core_spec** | str,  | str,  | specialized core count | [optional] 
**thread_spec** | str,  | str,  | specialized thread count | [optional] 
**cores_per_socket** | str,  | str,  | cores per socket required by job | [optional] 
**billable_tres** | decimal.Decimal, int, float,  | decimal.Decimal,  | billable TRES | [optional] 
**cpus_per_task** | str,  | str,  | number of processors required for each task | [optional] 
**cpu_frequency_minimum** | str,  | str,  | Minimum cpu frequency | [optional] 
**cpu_frequency_maximum** | str,  | str,  | Maximum cpu frequency | [optional] 
**cpu_frequency_governor** | str,  | str,  | cpu frequency governor | [optional] 
**cpus_per_tres** | str,  | str,  | semicolon delimited list of TRES&#x3D;# values | [optional] 
**deadline** | decimal.Decimal, int,  | decimal.Decimal,  | job start deadline  | [optional] 
**delay_boot** | decimal.Decimal, int,  | decimal.Decimal,  | command to be executed | [optional] 
**dependency** | str,  | str,  | synchronize job execution with other jobs | [optional] 
**derived_exit_code** | decimal.Decimal, int,  | decimal.Decimal,  | highest exit code of all job steps | [optional] 
**eligible_time** | decimal.Decimal, int,  | decimal.Decimal,  | time job is eligible for running | [optional] value must be a 64 bit integer
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  | time of termination, actual or expected | [optional] value must be a 64 bit integer
**excluded_nodes** | str,  | str,  | comma separated list of excluded nodes | [optional] 
**exit_code** | decimal.Decimal, int,  | decimal.Decimal,  | exit code for job | [optional] 
**features** | str,  | str,  | comma separated list of required features | [optional] 
**federation_origin** | str,  | str,  | Origin cluster&#x27;s name | [optional] 
**federation_siblings_active** | str,  | str,  | string of active sibling names | [optional] 
**federation_siblings_viable** | str,  | str,  | string of viable sibling names | [optional] 
**[gres_detail](#gres_detail)** | list, tuple,  | tuple,  | Job flags | [optional] 
**group_id** | decimal.Decimal, int,  | decimal.Decimal,  | group job submitted as | [optional] 
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  | job ID | [optional] 
**job_resources** | [**V0038JobResources**](V0038JobResources.md) | [**V0038JobResources**](V0038JobResources.md) |  | [optional] 
**job_state** | str,  | str,  | state of the job | [optional] 
**last_sched_evaluation** | decimal.Decimal, int,  | decimal.Decimal,  | last time job was evaluated for scheduling | [optional] 
**licenses** | str,  | str,  | licenses required by the job | [optional] 
**max_cpus** | decimal.Decimal, int,  | decimal.Decimal,  | maximum number of cpus usable by job | [optional] 
**max_nodes** | decimal.Decimal, int,  | decimal.Decimal,  | maximum number of nodes usable by job | [optional] 
**mcs_label** | str,  | str,  | mcs_label if mcs plugin in use | [optional] 
**memory_per_tres** | str,  | str,  | semicolon delimited list of TRES&#x3D;# values | [optional] 
**name** | str,  | str,  | name of the job | [optional] 
**nodes** | str,  | str,  | list of nodes allocated to job | [optional] 
**nice** | decimal.Decimal, int,  | decimal.Decimal,  | requested priority change | [optional] 
**tasks_per_core** | decimal.Decimal, int,  | decimal.Decimal,  | number of tasks to invoke on each core | [optional] 
**tasks_per_socket** | decimal.Decimal, int,  | decimal.Decimal,  | number of tasks to invoke on each socket | [optional] 
**tasks_per_board** | decimal.Decimal, int,  | decimal.Decimal,  | number of tasks to invoke on each board | [optional] 
**cpus** | decimal.Decimal, int,  | decimal.Decimal,  | minimum number of cpus required by job | [optional] 
**node_count** | decimal.Decimal, int,  | decimal.Decimal,  | minimum number of nodes required by job | [optional] 
**tasks** | decimal.Decimal, int,  | decimal.Decimal,  | requested task count | [optional] 
**het_job_id** | decimal.Decimal, int,  | decimal.Decimal,  | job ID of hetjob leader | [optional] 
**het_job_id_set** | str,  | str,  | job IDs for all components | [optional] 
**het_job_offset** | decimal.Decimal, int,  | decimal.Decimal,  | HetJob component offset from leader | [optional] 
**partition** | str,  | str,  | name of assigned partition | [optional] 
**memory_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | minimum real memory per node | [optional] 
**memory_per_cpu** | decimal.Decimal, int,  | decimal.Decimal,  | minimum real memory per cpu | [optional] 
**minimum_cpus_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | minimum # CPUs per node | [optional] 
**minimum_tmp_disk_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | minimum tmp disk per node | [optional] 
**preempt_time** | decimal.Decimal, int,  | decimal.Decimal,  | preemption signal time | [optional] value must be a 64 bit integer
**pre_sus_time** | decimal.Decimal, int,  | decimal.Decimal,  | time job ran prior to last suspend | [optional] value must be a 64 bit integer
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | relative priority of the job | [optional] 
**[profile](#profile)** | list, tuple,  | tuple,  | Job profiling requested | [optional] 
**qos** | str,  | str,  | Quality of Service | [optional] 
**reboot** | bool,  | BoolClass,  | node reboot requested before start | [optional] 
**required_nodes** | str,  | str,  | comma separated list of required nodes | [optional] 
**requeue** | bool,  | BoolClass,  | enable or disable job requeue option | [optional] 
**resize_time** | decimal.Decimal, int,  | decimal.Decimal,  | time of latest size change | [optional] value must be a 64 bit integer
**restart_cnt** | decimal.Decimal, int,  | decimal.Decimal,  | count of job restarts | [optional] 
**resv_name** | str,  | str,  | reservation name | [optional] 
**shared** | str,  | str,  | type and if job can share nodes with other jobs | [optional] 
**[show_flags](#show_flags)** | list, tuple,  | tuple,  | details requested | [optional] 
**sockets_per_board** | decimal.Decimal, int,  | decimal.Decimal,  | sockets per board required by job | [optional] 
**sockets_per_node** | decimal.Decimal, int,  | decimal.Decimal,  | sockets per node required by job | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | time execution begins, actual or expected | [optional] value must be a 64 bit integer
**state_description** | str,  | str,  | optional details for state_reason | [optional] 
**state_reason** | str,  | str,  | reason job still pending or failed | [optional] 
**standard_error** | str,  | str,  | pathname of job&#x27;s stderr file | [optional] 
**standard_input** | str,  | str,  | pathname of job&#x27;s stdin file | [optional] 
**standard_output** | str,  | str,  | pathname of job&#x27;s stdout file | [optional] 
**submit_time** | decimal.Decimal, int,  | decimal.Decimal,  | time of job submission | [optional] value must be a 64 bit integer
**suspend_time** | decimal.Decimal, int,  | decimal.Decimal,  | time job last suspended or resumed | [optional] value must be a 64 bit integer
**system_comment** | str,  | str,  | slurmctld&#x27;s arbitrary comment | [optional] 
**time_limit** | decimal.Decimal, int,  | decimal.Decimal,  | maximum run time in minutes | [optional] value must be a 64 bit integer
**time_minimum** | decimal.Decimal, int,  | decimal.Decimal,  | minimum run time in minutes | [optional] value must be a 64 bit integer
**threads_per_core** | decimal.Decimal, int,  | decimal.Decimal,  | threads per core required by job | [optional] 
**tres_bind** | str,  | str,  | Task to TRES binding directives | [optional] 
**tres_freq** | str,  | str,  | TRES frequency directives | [optional] 
**tres_per_job** | str,  | str,  | semicolon delimited list of TRES&#x3D;# values | [optional] 
**tres_per_node** | str,  | str,  | semicolon delimited list of TRES&#x3D;# values | [optional] 
**tres_per_socket** | str,  | str,  | semicolon delimited list of TRES&#x3D;# values | [optional] 
**tres_per_task** | str,  | str,  | semicolon delimited list of TRES&#x3D;# values | [optional] 
**tres_req_str** | str,  | str,  | tres reqeusted in the job | [optional] 
**tres_alloc_str** | str,  | str,  | tres used in the job | [optional] 
**user_id** | decimal.Decimal, int,  | decimal.Decimal,  | user id the job runs as | [optional] value must be a 64 bit integer
**user_name** | str,  | str,  | user the job runs as | [optional] 
**wckey** | str,  | str,  | wckey for job | [optional] 
**current_working_directory** | str,  | str,  | pathname of working directory | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

Job flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Job flags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# gres_detail

Job flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Job flags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# profile

Job profiling requested

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Job profiling requested | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# show_flags

details requested

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | details requested | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

