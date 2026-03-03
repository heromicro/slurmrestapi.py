# V0044StatsMsgRpcQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string (Slurm RPC message type) | 
**count** | **int** | Number of pending RPCs queued | 

## Example

```python
from slurmrestapi.models.v0044_stats_msg_rpc_queue import V0044StatsMsgRpcQueue

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StatsMsgRpcQueue from a JSON string
v0044_stats_msg_rpc_queue_instance = V0044StatsMsgRpcQueue.from_json(json)
# print the JSON string representation of the object
print(V0044StatsMsgRpcQueue.to_json())

# convert the object into a dict
v0044_stats_msg_rpc_queue_dict = v0044_stats_msg_rpc_queue_instance.to_dict()
# create an instance of V0044StatsMsgRpcQueue from a dict
v0044_stats_msg_rpc_queue_from_dict = V0044StatsMsgRpcQueue.from_dict(v0044_stats_msg_rpc_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


