# slurmrestapi.model.v0039_job_info.V0039JobInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | str,  | str,  |  | [optional] 
**accrue_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**admin_comment** | str,  | str,  |  | [optional] 
**allocating_node** | str,  | str,  |  | [optional] 
**array_job_id** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**array_task_id** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**array_max_tasks** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**array_task_string** | str,  | str,  |  | [optional] 
**association_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**batch_features** | str,  | str,  |  | [optional] 
**batch_flag** | bool,  | BoolClass,  |  | [optional] 
**batch_host** | str,  | str,  |  | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  |  | [optional] 
**burst_buffer** | str,  | str,  |  | [optional] 
**burst_buffer_state** | str,  | str,  |  | [optional] 
**cluster** | str,  | str,  |  | [optional] 
**cluster_features** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**comment** | str,  | str,  |  | [optional] 
**container** | str,  | str,  |  | [optional] 
**container_id** | str,  | str,  |  | [optional] 
**contiguous** | bool,  | BoolClass,  |  | [optional] 
**core_spec** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**thread_spec** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**cores_per_socket** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**billable_tres** | [**V0039Float64NoVal**](V0039Float64NoVal.md) | [**V0039Float64NoVal**](V0039Float64NoVal.md) |  | [optional] 
**cpus_per_task** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**cpu_frequency_minimum** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**cpu_frequency_maximum** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**cpu_frequency_governor** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**cpus_per_tres** | str,  | str,  |  | [optional] 
**cron** | str,  | str,  |  | [optional] 
**deadline** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**delay_boot** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**dependency** | str,  | str,  |  | [optional] 
**derived_exit_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**eligible_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**excluded_nodes** | str,  | str,  |  | [optional] 
**exit_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**extra** | str,  | str,  |  | [optional] 
**failed_node** | str,  | str,  |  | [optional] 
**features** | str,  | str,  |  | [optional] 
**federation_origin** | str,  | str,  |  | [optional] 
**federation_siblings_active** | str,  | str,  |  | [optional] 
**federation_siblings_viable** | str,  | str,  |  | [optional] 
**gres_detail** | [**V0039JobInfoGresDetail**](V0039JobInfoGresDetail.md) | [**V0039JobInfoGresDetail**](V0039JobInfoGresDetail.md) |  | [optional] 
**group_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**group_name** | str,  | str,  |  | [optional] 
**het_job_id** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**het_job_id_set** | str,  | str,  |  | [optional] 
**het_job_offset** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**job_resources** | [**V0039JobRes**](V0039JobRes.md) | [**V0039JobRes**](V0039JobRes.md) |  | [optional] 
**job_size_str** | [**V0039CsvList**](V0039CsvList.md) | [**V0039CsvList**](V0039CsvList.md) |  | [optional] 
**job_state** | str,  | str,  |  | [optional] 
**last_sched_evaluation** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**licenses** | str,  | str,  |  | [optional] 
**[mail_type](#mail_type)** | list, tuple,  | tuple,  |  | [optional] 
**mail_user** | str,  | str,  |  | [optional] 
**max_cpus** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**max_nodes** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**mcs_label** | str,  | str,  |  | [optional] 
**memory_per_tres** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**network** | str,  | str,  |  | [optional] 
**nodes** | str,  | str,  |  | [optional] 
**nice** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**tasks_per_core** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**tasks_per_tres** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**tasks_per_node** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**tasks_per_socket** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**tasks_per_board** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**cpus** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**node_count** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**tasks** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**partition** | str,  | str,  |  | [optional] 
**prefer** | str,  | str,  |  | [optional] 
**memory_per_cpu** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**memory_per_node** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**minimum_cpus_per_node** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**minimum_tmp_disk_per_node** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**[power](#power)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**preempt_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**preemptable_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**pre_sus_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**priority** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**[profile](#profile)** | list, tuple,  | tuple,  |  | [optional] 
**qos** | str,  | str,  |  | [optional] 
**reboot** | bool,  | BoolClass,  |  | [optional] 
**required_nodes** | str,  | str,  |  | [optional] 
**minimum_switches** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**requeue** | bool,  | BoolClass,  |  | [optional] 
**resize_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**restart_cnt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**resv_name** | str,  | str,  |  | [optional] 
**scheduled_nodes** | str,  | str,  |  | [optional] 
**selinux_context** | str,  | str,  |  | [optional] 
**[shared](#shared)** | list, tuple,  | tuple,  |  | [optional] 
**exclusive** | [**V0039JobExclusive**](V0039JobExclusive.md) | [**V0039JobExclusive**](V0039JobExclusive.md) |  | [optional] 
**[show_flags](#show_flags)** | list, tuple,  | tuple,  |  | [optional] 
**sockets_per_board** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**sockets_per_node** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**state_description** | str,  | str,  |  | [optional] 
**state_reason** | str,  | str,  |  | [optional] 
**standard_error** | str,  | str,  |  | [optional] 
**standard_input** | str,  | str,  |  | [optional] 
**standard_output** | str,  | str,  |  | [optional] 
**submit_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**suspend_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**system_comment** | str,  | str,  |  | [optional] 
**time_limit** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**time_minimum** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**threads_per_core** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**tres_bind** | str,  | str,  |  | [optional] 
**tres_freq** | str,  | str,  |  | [optional] 
**tres_per_job** | str,  | str,  |  | [optional] 
**tres_per_node** | str,  | str,  |  | [optional] 
**tres_per_socket** | str,  | str,  |  | [optional] 
**tres_per_task** | str,  | str,  |  | [optional] 
**tres_req_str** | str,  | str,  |  | [optional] 
**tres_alloc_str** | str,  | str,  |  | [optional] 
**user_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**user_name** | str,  | str,  |  | [optional] 
**maximum_switch_wait_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**wckey** | str,  | str,  |  | [optional] 
**current_working_directory** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["KILL_INVALID_DEPENDENCY", "NO_KILL_INVALID_DEPENDENCY", "HAS_STATE_DIRECTORY", "TESTING_BACKFILL", "GRES_BINDING_ENFORCED", "TEST_NOW_ONLY", "SEND_JOB_ENVIRONMENT", "SPREAD_JOB", "PREFER_MINIMUM_NODE_COUNT", "JOB_KILL_HURRY", "SKIP_TRES_STRING_ACCOUNTING", "SIBLING_CLUSTER_UPDATE_ONLY", "HETEROGENEOUS_JOB", "EXACT_TASK_COUNT_REQUESTED", "EXACT_CPU_COUNT_REQUESTED", "TESTING_WHOLE_NODE_BACKFILL", "TOP_PRIORITY_JOB", "ACCRUE_COUNT_CLEARED", "GRED_BINDING_DISABLED", "JOB_WAS_RUNNING", "JOB_ACCRUE_TIME_RESET", "CRON_JOB", "EXACT_MEMORY_REQUESTED", "JOB_RESIZED", "USING_DEFAULT_ACCOUNT", "USING_DEFAULT_PARTITION", "USING_DEFAULT_QOS", "USING_DEFAULT_WCKEY", "DEPENDENT", "MAGNETIC", "PARTITION_ASSIGNED", "BACKFILL_ATTEMPTED", "SCHEDULING_ATTEMPTED", "SAVE_BATCH_SCRIPT", ] 

# mail_type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["BEGIN", "END", "FAIL", "REQUEUE", "TIME=100%", "TIME=90%", "TIME=80%", "TIME=50%", "STAGE_OUT", "ARRAY_TASKS", "INVALID_DEPENDENCY", ] 

# power

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[flags](#flags)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["EQUAL_POWER", ] 

# profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["NOT_SET", "NONE", "ENERGY", "LUSTRE", "NETWORK", "TASK", ] 

# shared

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["none", "oversubscribe", "user", "mcs", ] 

# show_flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["ALL", "DETAIL", "MIXED", "LOCAL", "SIBLING", "FEDERATION", "FUTURE", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

