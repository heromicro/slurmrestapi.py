# slurmrestapi.model.v0038_reservation.V0038Reservation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accounts** | str,  | str,  | Allowed accounts | [optional] 
**burst_buffer** | str,  | str,  | Reserved burst buffer | [optional] 
**core_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of reserved cores | [optional] 
**core_spec_cnt** | decimal.Decimal, int,  | decimal.Decimal,  | Number of reserved specialized cores | [optional] 
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  | End time of the reservation | [optional] 
**features** | str,  | str,  | List of features | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  | Reservation options | [optional] 
**groups** | str,  | str,  | List of groups permitted to use the reserved nodes | [optional] 
**licenses** | str,  | str,  | List of licenses | [optional] 
**max_start_delay** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum delay in which jobs outside of the reservation will be permitted to overlap once any jobs are queued for the reservation | [optional] 
**name** | str,  | str,  | Reservationn name | [optional] 
**node_count** | decimal.Decimal, int,  | decimal.Decimal,  | Count of nodes reserved | [optional] 
**node_list** | str,  | str,  | List of reserved nodes | [optional] 
**partition** | str,  | str,  | Partition | [optional] 
**[purge_completed](#purge_completed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | If PURGE_COMP flag is set the amount of seconds this reservation will sit idle until it is revoked | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Start time of reservation | [optional] 
**watts** | decimal.Decimal, int,  | decimal.Decimal,  | amount of power to reserve in watts | [optional] 
**tres** | str,  | str,  | List of TRES | [optional] 
**users** | str,  | str,  | List of users | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

Reservation options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Reservation options | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# purge_completed

If PURGE_COMP flag is set the amount of seconds this reservation will sit idle until it is revoked

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | If PURGE_COMP flag is set the amount of seconds this reservation will sit idle until it is revoked | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**time** | decimal.Decimal, int,  | decimal.Decimal,  | amount of seconds this reservation will sit idle until it is revoked | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

