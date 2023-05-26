# slurmrestapi.model.v0038_node.V0038Node

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**architecture** | str,  | str,  | computer architecture | [optional] 
**burstbuffer_network_address** | str,  | str,  | BcastAddr | [optional] 
**boards** | decimal.Decimal, int,  | decimal.Decimal,  | total number of boards per node | [optional] 
**boot_time** | decimal.Decimal, int,  | decimal.Decimal,  | timestamp of node boot | [optional] value must be a 64 bit integer
**cores** | decimal.Decimal, int,  | decimal.Decimal,  | number of cores per socket | [optional] 
**cpu_binding** | decimal.Decimal, int,  | decimal.Decimal,  | Default task binding | [optional] 
**cpu_load** | decimal.Decimal, int,  | decimal.Decimal,  | CPU load * 100 | [optional] value must be a 64 bit integer
**free_memory** | decimal.Decimal, int,  | decimal.Decimal,  | free memory in MiB | [optional] 
**cpus** | decimal.Decimal, int,  | decimal.Decimal,  | configured count of cpus running on the node | [optional] 
**features** | str,  | str,  |  | [optional] 
**active_features** | str,  | str,  | list of a node&#x27;s available features | [optional] 
**gres** | str,  | str,  | list of a node&#x27;s generic resources | [optional] 
**gres_drained** | str,  | str,  | list of drained GRES | [optional] 
**gres_used** | str,  | str,  | list of GRES in current use | [optional] 
**mcs_label** | str,  | str,  | mcs label if mcs plugin in use | [optional] 
**name** | str,  | str,  | node name to slurm | [optional] 
**next_state_after_reboot** | str,  | str,  | state after reboot | [optional] 
**[next_state_after_reboot_flags](#next_state_after_reboot_flags)** | list, tuple,  | tuple,  | node state flags | [optional] 
**address** | str,  | str,  | state after reboot | [optional] 
**hostname** | str,  | str,  | node&#x27;s hostname | [optional] 
**state** | str,  | str,  | current node state | [optional] 
**[state_flags](#state_flags)** | list, tuple,  | tuple,  | node state flags | [optional] 
**operating_system** | str,  | str,  | operating system | [optional] 
**owner** | str,  | str,  | User allowed to use this node | [optional] 
**[partitions](#partitions)** | list, tuple,  | tuple,  | assigned partitions | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | TCP port number of the slurmd | [optional] 
**real_memory** | decimal.Decimal, int,  | decimal.Decimal,  | configured MB of real memory on the node | [optional] 
**reason** | str,  | str,  | reason for node being DOWN or DRAINING | [optional] 
**reason_changed_at** | decimal.Decimal, int,  | decimal.Decimal,  | Time stamp when reason was set | [optional] 
**reason_set_by_user** | str,  | str,  | User that set the reason | [optional] 
**slurmd_start_time** | decimal.Decimal, int,  | decimal.Decimal,  | timestamp of slurmd startup | [optional] value must be a 64 bit integer
**sockets** | decimal.Decimal, int,  | decimal.Decimal,  | total number of sockets per node | [optional] 
**threads** | decimal.Decimal, int,  | decimal.Decimal,  | number of threads per core | [optional] 
**temporary_disk** | decimal.Decimal, int,  | decimal.Decimal,  | configured MB of total disk in TMP_FS | [optional] 
**weight** | decimal.Decimal, int,  | decimal.Decimal,  | arbitrary priority of node for scheduling | [optional] 
**tres** | str,  | str,  | TRES on node | [optional] 
**tres_used** | str,  | str,  | TRES used on node | [optional] 
**tres_weighted** | decimal.Decimal, int, float,  | decimal.Decimal,  | TRES weight used on node | [optional] value must be a 64 bit float
**slurmd_version** | str,  | str,  | Slurmd version | [optional] 
**alloc_cpus** | decimal.Decimal, int,  | decimal.Decimal,  | Allocated CPUs | [optional] value must be a 64 bit integer
**idle_cpus** | decimal.Decimal, int,  | decimal.Decimal,  | Idle CPUs | [optional] value must be a 64 bit integer
**alloc_memory** | decimal.Decimal, int,  | decimal.Decimal,  | Allocated memory (MB) | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# next_state_after_reboot_flags

node state flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | node state flags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# state_flags

node state flags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | node state flags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# partitions

assigned partitions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | assigned partitions | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

