# slurmrestapi.model.dbv0037_cluster_info.Dbv0037ClusterInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[controller](#controller)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about controller | [optional] 
**[flags](#flags)** | list, tuple,  | tuple,  | List of properties of cluster | [optional] 
**name** | str,  | str,  | Cluster name | [optional] 
**nodes** | str,  | str,  | Assigned nodes | [optional] 
**select_plugin** | str,  | str,  | Configured select plugin | [optional] 
**[associations](#associations)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about associations | [optional] 
**rpc_version** | decimal.Decimal, int,  | decimal.Decimal,  | Number rpc version | [optional] 
**[tres](#tres)** | list, tuple,  | tuple,  | List of TRES in cluster | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# controller

Information about controller

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about controller | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**host** | str,  | str,  | Hostname | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | Port number | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flags

List of properties of cluster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of properties of cluster | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | String of property name | 

# associations

Information about associations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about associations | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**root** | [**Dbv0037AssociationShortInfo**](Dbv0037AssociationShortInfo.md) | [**Dbv0037AssociationShortInfo**](Dbv0037AssociationShortInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tres

List of TRES in cluster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of TRES in cluster | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dbv0037ResponseTres**](Dbv0037ResponseTres.md) | [**Dbv0037ResponseTres**](Dbv0037ResponseTres.md) | [**Dbv0037ResponseTres**](Dbv0037ResponseTres.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

