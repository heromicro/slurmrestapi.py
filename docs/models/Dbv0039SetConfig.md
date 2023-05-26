# slurmrestapi.model.dbv0039_set_config.Dbv0039SetConfig

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clusters** | [**V0039ClusterRecList**](V0039ClusterRecList.md) | [**V0039ClusterRecList**](V0039ClusterRecList.md) |  | [optional] 
**[TRES](#TRES)** | list, tuple,  | tuple,  |  | [optional] 
**accounts** | [**V0039AccountList**](V0039AccountList.md) | [**V0039AccountList**](V0039AccountList.md) |  | [optional] 
**users** | [**V0039UserList**](V0039UserList.md) | [**V0039UserList**](V0039UserList.md) |  | [optional] 
**qos** | [**V0039QosList**](V0039QosList.md) | [**V0039QosList**](V0039QosList.md) |  | [optional] 
**wckeys** | [**V0039WckeyList**](V0039WckeyList.md) | [**V0039WckeyList**](V0039WckeyList.md) |  | [optional] 
**associations** | [**V0039AssocList**](V0039AssocList.md) | [**V0039AssocList**](V0039AssocList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TRES

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V0039TresList**](V0039TresList.md) | [**V0039TresList**](V0039TresList.md) | [**V0039TresList**](V0039TresList.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

