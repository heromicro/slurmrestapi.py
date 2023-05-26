# slurmrestapi.model.v0037_diag.V0037Diag

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | list, tuple,  | tuple,  | slurm errors | [optional] 
**[statistics](#statistics)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Slurm statistics | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

slurm errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | slurm errors | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V0037Error**](V0037Error.md) | [**V0037Error**](V0037Error.md) | [**V0037Error**](V0037Error.md) |  | 

# statistics

Slurm statistics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Slurm statistics | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**parts_packed** | decimal.Decimal, int,  | decimal.Decimal,  | partition records packed | [optional] 
**req_time** | decimal.Decimal, int,  | decimal.Decimal,  | generation time | [optional] 
**req_time_start** | decimal.Decimal, int,  | decimal.Decimal,  | data since | [optional] 
**server_thread_count** | decimal.Decimal, int,  | decimal.Decimal,  | Server thread count | [optional] 
**agent_queue_size** | decimal.Decimal, int,  | decimal.Decimal,  | Agent queue size | [optional] 
**agent_count** | decimal.Decimal, int,  | decimal.Decimal,  | Agent count | [optional] 
**agent_thread_count** | decimal.Decimal, int,  | decimal.Decimal,  | Agent thread count | [optional] 
**dbd_agent_queue_size** | decimal.Decimal, int,  | decimal.Decimal,  | DBD Agent queue size | [optional] 
**gettimeofday_latency** | decimal.Decimal, int,  | decimal.Decimal,  | Latency for 1000 calls to gettimeofday() | [optional] 
**schedule_cycle_max** | decimal.Decimal, int,  | decimal.Decimal,  | Main Schedule max cycle | [optional] 
**schedule_cycle_last** | decimal.Decimal, int,  | decimal.Decimal,  | Main Schedule last cycle | [optional] 
**schedule_cycle_total** | decimal.Decimal, int,  | decimal.Decimal,  | Main Schedule cycle iterations | [optional] 
**schedule_cycle_mean** | decimal.Decimal, int,  | decimal.Decimal,  | Average time for Schedule Max cycle | [optional] 
**schedule_cycle_mean_depth** | decimal.Decimal, int,  | decimal.Decimal,  | Average depth for Schedule Max cycle | [optional] 
**schedule_cycle_per_minute** | decimal.Decimal, int,  | decimal.Decimal,  | Main Schedule Cycles per minute | [optional] 
**schedule_queue_length** | decimal.Decimal, int,  | decimal.Decimal,  | Main Schedule Last queue length | [optional] 
**jobs_submitted** | decimal.Decimal, int,  | decimal.Decimal,  | Job submitted | [optional] 
**jobs_started** | decimal.Decimal, int,  | decimal.Decimal,  | Job started | [optional] 
**jobs_completed** | decimal.Decimal, int,  | decimal.Decimal,  | Job completed | [optional] 
**jobs_canceled** | decimal.Decimal, int,  | decimal.Decimal,  | Job cancelled | [optional] 
**jobs_failed** | decimal.Decimal, int,  | decimal.Decimal,  | Job failed | [optional] 
**jobs_pending** | decimal.Decimal, int,  | decimal.Decimal,  | Job pending | [optional] 
**jobs_running** | decimal.Decimal, int,  | decimal.Decimal,  | Job running | [optional] 
**job_states_ts** | decimal.Decimal, int,  | decimal.Decimal,  | Job states timestamp | [optional] 
**bf_backfilled_jobs** | decimal.Decimal, int,  | decimal.Decimal,  | Total backfilled jobs (since last slurm start) | [optional] 
**bf_last_backfilled_jobs** | decimal.Decimal, int,  | decimal.Decimal,  | Total backfilled jobs (since last stats cycle start) | [optional] 
**bf_backfilled_het_jobs** | decimal.Decimal, int,  | decimal.Decimal,  | Total backfilled heterogeneous job components | [optional] 
**bf_cycle_counter** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Total cycles | [optional] 
**bf_cycle_mean** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Mean cycle | [optional] 
**bf_cycle_max** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Max cycle time | [optional] 
**bf_last_depth** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Last depth cycle | [optional] 
**bf_last_depth_try** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Mean cycle (try sched) | [optional] 
**bf_depth_mean** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Depth Mean | [optional] 
**bf_depth_mean_try** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Depth Mean (try sched) | [optional] 
**bf_cycle_last** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Last cycle time | [optional] 
**bf_queue_len** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Last queue length | [optional] 
**bf_queue_len_mean** | decimal.Decimal, int,  | decimal.Decimal,  | Backfill Schedule Mean queue length | [optional] 
**bf_when_last_cycle** | decimal.Decimal, int,  | decimal.Decimal,  | Last cycle timestamp | [optional] 
**bf_active** | bool,  | BoolClass,  | Backfill Schedule currently active | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

