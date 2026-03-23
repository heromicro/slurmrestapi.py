# V0044StatsRpc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rpc** | **str** | RPC type | [optional] 
**count** | **int** | Number of RPCs processed | [optional] 
**time** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInnerTime**](V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInnerTime.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_stats_rpc import V0044StatsRpc

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StatsRpc from a JSON string
v0044_stats_rpc_instance = V0044StatsRpc.from_json(json)
# print the JSON string representation of the object
print(V0044StatsRpc.to_json())

# convert the object into a dict
v0044_stats_rpc_dict = v0044_stats_rpc_instance.to_dict()
# create an instance of V0044StatsRpc from a dict
v0044_stats_rpc_from_dict = V0044StatsRpc.from_dict(v0044_stats_rpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


