# V0044StatsRec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_start** | **int** | When data collection started (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**rollups** | [**V0044RollupStats**](V0044RollupStats.md) |  | [optional] 
**rpcs** | [**List[V0044StatsRpc]**](V0044StatsRpc.md) |  | [optional] 
**users** | [**List[V0044StatsUser]**](V0044StatsUser.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_stats_rec import V0044StatsRec

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StatsRec from a JSON string
v0044_stats_rec_instance = V0044StatsRec.from_json(json)
# print the JSON string representation of the object
print(V0044StatsRec.to_json())

# convert the object into a dict
v0044_stats_rec_dict = v0044_stats_rec_instance.to_dict()
# create an instance of V0044StatsRec from a dict
v0044_stats_rec_from_dict = V0044StatsRec.from_dict(v0044_stats_rec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


