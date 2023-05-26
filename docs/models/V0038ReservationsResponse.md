# slurmrestapi.model.v0038_reservations_response.V0038ReservationsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**meta** | [**V0038Meta**](V0038Meta.md) | [**V0038Meta**](V0038Meta.md) |  | [optional] 
**[errors](#errors)** | list, tuple,  | tuple,  | slurm errors | [optional] 
**[reservations](#reservations)** | list, tuple,  | tuple,  | reservation info | [optional] 
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
[**V0038Error**](V0038Error.md) | [**V0038Error**](V0038Error.md) | [**V0038Error**](V0038Error.md) |  | 

# reservations

reservation info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | reservation info | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V0038Reservation**](V0038Reservation.md) | [**V0038Reservation**](V0038Reservation.md) | [**V0038Reservation**](V0038Reservation.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

