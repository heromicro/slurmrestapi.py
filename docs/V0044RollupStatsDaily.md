# V0044RollupStatsDaily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of daily rollups since last_run | [optional] 
**last_run** | **int** | Last time daily rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**duration** | [**SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration**](SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_rollup_stats_daily import V0044RollupStatsDaily

# TODO update the JSON string below
json = "{}"
# create an instance of V0044RollupStatsDaily from a JSON string
v0044_rollup_stats_daily_instance = V0044RollupStatsDaily.from_json(json)
# print the JSON string representation of the object
print(V0044RollupStatsDaily.to_json())

# convert the object into a dict
v0044_rollup_stats_daily_dict = v0044_rollup_stats_daily_instance.to_dict()
# create an instance of V0044RollupStatsDaily from a dict
v0044_rollup_stats_daily_from_dict = V0044RollupStatsDaily.from_dict(v0044_rollup_stats_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


