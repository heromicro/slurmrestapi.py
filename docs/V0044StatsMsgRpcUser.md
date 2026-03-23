# V0044StatsMsgRpcUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID (numeric) | 
**user** | **str** | User name | 
**count** | **int** | Number of RPCs received | 
**total_time** | **int** | Total time spent processing RPC in seconds | 
**average_time** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | 

## Example

```python
from slurmrestapi.models.v0044_stats_msg_rpc_user import V0044StatsMsgRpcUser

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StatsMsgRpcUser from a JSON string
v0044_stats_msg_rpc_user_instance = V0044StatsMsgRpcUser.from_json(json)
# print the JSON string representation of the object
print(V0044StatsMsgRpcUser.to_json())

# convert the object into a dict
v0044_stats_msg_rpc_user_dict = v0044_stats_msg_rpc_user_instance.to_dict()
# create an instance of V0044StatsMsgRpcUser from a dict
v0044_stats_msg_rpc_user_from_dict = V0044StatsMsgRpcUser.from_dict(v0044_stats_msg_rpc_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


