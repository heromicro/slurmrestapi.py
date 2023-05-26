# slurmrestapi.model.v0039_stats_msg.V0039StatsMsg

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**parts_packed** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**req_time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**req_time_start** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**server_thread_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**agent_queue_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**agent_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**agent_thread_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**dbd_agent_queue_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**gettimeofday_latency** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**schedule_cycle_max** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**schedule_cycle_last** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**schedule_cycle_total** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**schedule_cycle_mean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**schedule_cycle_mean_depth** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**schedule_cycle_per_minute** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**schedule_queue_length** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**jobs_submitted** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**jobs_started** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**jobs_completed** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**jobs_canceled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**jobs_failed** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**jobs_pending** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**jobs_running** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**job_states_ts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**bf_backfilled_jobs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_last_backfilled_jobs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_backfilled_het_jobs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_cycle_counter** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_cycle_mean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**bf_depth_mean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**bf_depth_mean_try** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**bf_cycle_sum** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**bf_cycle_last** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_last_depth** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_last_depth_try** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_depth_sum** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_depth_try_sum** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_queue_len** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_queue_len_mean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**bf_queue_len_sum** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_table_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**bf_table_size_mean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**bf_when_last_cycle** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**bf_active** | bool,  | BoolClass,  |  | [optional] 
**rpcs_by_message_type** | [**V0039StatsMsgRpcsByType**](V0039StatsMsgRpcsByType.md) | [**V0039StatsMsgRpcsByType**](V0039StatsMsgRpcsByType.md) |  | [optional] 
**rpcs_by_user** | [**V0039StatsMsgRpcsByUser**](V0039StatsMsgRpcsByUser.md) | [**V0039StatsMsgRpcsByUser**](V0039StatsMsgRpcsByUser.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

