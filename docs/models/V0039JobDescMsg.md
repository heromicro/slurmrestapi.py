# slurmrestapi.model.v0039_job_desc_msg.V0039JobDescMsg

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account** | str,  | str,  |  | [optional] 
**account_gather_frequency** | str,  | str,  |  | [optional] 
**admin_comment** | str,  | str,  |  | [optional] 
**allocation_node_list** | str,  | str,  |  | [optional] 
**allocation_node_port** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**argv** | [**V0039StringArray**](V0039StringArray.md) | [**V0039StringArray**](V0039StringArray.md) |  | [optional] 
**array** | str,  | str,  |  | [optional] 
**batch_features** | str,  | str,  |  | [optional] 
**begin_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**[flags](#flags)** | list, tuple,  | tuple,  |  | [optional] 
**burst_buffer** | str,  | str,  |  | [optional] 
**clusters** | str,  | str,  |  | [optional] 
**cluster_constraint** | str,  | str,  |  | [optional] 
**comment** | str,  | str,  |  | [optional] 
**contiguous** | bool,  | BoolClass,  |  | [optional] 
**container** | str,  | str,  |  | [optional] 
**container_id** | str,  | str,  |  | [optional] 
**core_specification** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**thread_specification** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**cpu_binding** | str,  | str,  |  | [optional] 
**[cpu_binding_flags](#cpu_binding_flags)** | list, tuple,  | tuple,  |  | [optional] 
**cpu_frequency** | str,  | str,  |  | [optional] 
**cpus_per_tres** | str,  | str,  |  | [optional] 
**crontab** | [**V0039CronEntry**](V0039CronEntry.md) | [**V0039CronEntry**](V0039CronEntry.md) |  | [optional] 
**deadline** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**delay_boot** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**dependency** | str,  | str,  |  | [optional] 
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**environment** | [**V0039StringArray**](V0039StringArray.md) | [**V0039StringArray**](V0039StringArray.md) |  | [optional] 
**excluded_nodes** | [**V0039CsvList**](V0039CsvList.md) | [**V0039CsvList**](V0039CsvList.md) |  | [optional] 
**extra** | str,  | str,  |  | [optional] 
**constraints** | str,  | str,  |  | [optional] 
**group_id** | str,  | str,  |  | [optional] 
**hetjob_group** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**immediate** | bool,  | BoolClass,  |  | [optional] 
**job_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**kill_on_node_fail** | bool,  | BoolClass,  |  | [optional] 
**licenses** | str,  | str,  |  | [optional] 
**[mail_type](#mail_type)** | list, tuple,  | tuple,  |  | [optional] 
**mail_user** | str,  | str,  |  | [optional] 
**mcs_label** | str,  | str,  |  | [optional] 
**memory_binding** | str,  | str,  |  | [optional] 
**[memory_binding_type](#memory_binding_type)** | list, tuple,  | tuple,  |  | [optional] 
**memory_per_tres** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**network** | str,  | str,  |  | [optional] 
**nice** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**tasks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[open_mode](#open_mode)** | list, tuple,  | tuple,  |  | [optional] 
**reserve_ports** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**overcommit** | bool,  | BoolClass,  |  | [optional] 
**partition** | str,  | str,  |  | [optional] 
**distribution_plane_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[power_flags](#power_flags)** | list, tuple,  | tuple,  |  | [optional] 
**prefer** | str,  | str,  |  | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[profile](#profile)** | list, tuple,  | tuple,  |  | [optional] 
**qos** | str,  | str,  |  | [optional] 
**reboot** | bool,  | BoolClass,  |  | [optional] 
**required_nodes** | [**V0039CsvList**](V0039CsvList.md) | [**V0039CsvList**](V0039CsvList.md) |  | [optional] 
**requeue** | bool,  | BoolClass,  |  | [optional] 
**reservation** | str,  | str,  |  | [optional] 
**script** | str,  | str,  |  | [optional] 
**[shared](#shared)** | list, tuple,  | tuple,  |  | [optional] 
**exclusive** | [**V0039JobExclusive**](V0039JobExclusive.md) | [**V0039JobExclusive**](V0039JobExclusive.md) |  | [optional] 
**site_factor** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**spank_environment** | [**V0039StringArray**](V0039StringArray.md) | [**V0039StringArray**](V0039StringArray.md) |  | [optional] 
**distribution** | str,  | str,  |  | [optional] 
**time_limit** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**time_minimum** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**tres_bind** | str,  | str,  |  | [optional] 
**tres_freq** | str,  | str,  |  | [optional] 
**tres_per_job** | str,  | str,  |  | [optional] 
**tres_per_node** | str,  | str,  |  | [optional] 
**tres_per_socket** | str,  | str,  |  | [optional] 
**tres_per_task** | str,  | str,  |  | [optional] 
**user_id** | str,  | str,  |  | [optional] 
**wait_all_nodes** | bool,  | BoolClass,  |  | [optional] 
**[kill_warning_flags](#kill_warning_flags)** | list, tuple,  | tuple,  |  | [optional] 
**kill_warning_signal** | str,  | str,  |  | [optional] 
**kill_warning_delay** | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) | [**V0039Uint16NoVal**](V0039Uint16NoVal.md) |  | [optional] 
**current_working_directory** | str,  | str,  |  | [optional] 
**cpus_per_task** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**minimum_cpus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**maximum_cpus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**nodes** | str,  | str,  |  | [optional] 
**minimum_nodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**maximum_nodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**minimum_boards_per_node** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**minimum_sockets_per_board** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**sockets_per_node** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**threads_per_core** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**tasks_per_node** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**tasks_per_socket** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**tasks_per_core** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**tasks_per_board** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**ntasks_per_tres** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**minimum_cpus_per_node** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**memory_per_cpu** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**memory_per_node** | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) | [**V0039Uint64NoVal**](V0039Uint64NoVal.md) |  | [optional] 
**temporary_disk_per_node** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**selinux_context** | str,  | str,  |  | [optional] 
**required_switches** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**standard_error** | str,  | str,  |  | [optional] 
**standard_input** | str,  | str,  |  | [optional] 
**standard_output** | str,  | str,  |  | [optional] 
**wait_for_switch** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**wckey** | str,  | str,  |  | [optional] 
**[x11](#x11)** | list, tuple,  | tuple,  |  | [optional] 
**x11_magic_cookie** | str,  | str,  |  | [optional] 
**x11_target_host** | str,  | str,  |  | [optional] 
**x11_target_port** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
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

# cpu_binding_flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["VERBOSE", "CPU_BIND_TO_THREADS", "CPU_BIND_TO_CORES", "CPU_BIND_TO_SOCKETS", "CPU_BIND_TO_LDOMS", "CPU_BIND_NONE", "CPU_BIND_RANK", "CPU_BIND_MAP", "CPU_BIND_MASK", "CPU_BIND_LDRANK", "CPU_BIND_LDMAP", "CPU_BIND_LDMASK", "CPU_BIND_ONE_THREAD_PER_CORE", "CPU_AUTO_BIND_TO_THREADS", "CPU_AUTO_BIND_TO_CORES", "CPU_AUTO_BIND_TO_SOCKETS", "SLURMD_OFF_SPEC", "CPU_BIND_OFF", ] 

# mail_type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["BEGIN", "END", "FAIL", "REQUEUE", "TIME=100%", "TIME=90%", "TIME=80%", "TIME=50%", "STAGE_OUT", "ARRAY_TASKS", "INVALID_DEPENDENCY", ] 

# memory_binding_type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["VERBOSE", "NONE", "RANK", "MAP", "MASK", "LOCAL", "SORT", "PREFER", ] 

# open_mode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["APPEND", "TRUNCATE", ] 

# power_flags

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

# kill_warning_flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["BATCH_JOB", "ARRAY_JOB", "FULL_STEPS_ONLY", "FULL_JOB", "FEDERATION_REQUEUE", "HURRY", "OUT_OF_MEMORY", "NO_SIBLING_JOBS", "RESERVATION_JOB", "WARNING_SENT", ] 

# x11

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | flags | must be one of ["FORWARD_ALL_NODES", "BATCH_NODE", "FIRST_NODE", "LAST_NODE", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

