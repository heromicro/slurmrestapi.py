# V0044RollupStatsHourly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of hourly rollups since last_run | [optional] 
**last_run** | **int** | Last time hourly rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**duration** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration**](V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_rollup_stats_hourly import V0044RollupStatsHourly

# TODO update the JSON string below
json = "{}"
# create an instance of V0044RollupStatsHourly from a JSON string
v0044_rollup_stats_hourly_instance = V0044RollupStatsHourly.from_json(json)
# print the JSON string representation of the object
print(V0044RollupStatsHourly.to_json())

# convert the object into a dict
v0044_rollup_stats_hourly_dict = v0044_rollup_stats_hourly_instance.to_dict()
# create an instance of V0044RollupStatsHourly from a dict
v0044_rollup_stats_hourly_from_dict = V0044RollupStatsHourly.from_dict(v0044_rollup_stats_hourly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


