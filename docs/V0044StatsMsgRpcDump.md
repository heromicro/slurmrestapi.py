# V0044StatsMsgRpcDump


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string (Slurm RPC message type) | 
**count** | **List[str]** |  | 

## Example

```python
from slurmrestapi.models.v0044_stats_msg_rpc_dump import V0044StatsMsgRpcDump

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StatsMsgRpcDump from a JSON string
v0044_stats_msg_rpc_dump_instance = V0044StatsMsgRpcDump.from_json(json)
# print the JSON string representation of the object
print(V0044StatsMsgRpcDump.to_json())

# convert the object into a dict
v0044_stats_msg_rpc_dump_dict = v0044_stats_msg_rpc_dump_instance.to_dict()
# create an instance of V0044StatsMsgRpcDump from a dict
v0044_stats_msg_rpc_dump_from_dict = V0044StatsMsgRpcDump.from_dict(v0044_stats_msg_rpc_dump_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


