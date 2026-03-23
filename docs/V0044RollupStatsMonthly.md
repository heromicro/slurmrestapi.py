# V0044RollupStatsMonthly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of monthly rollups since last_run | [optional] 
**last_run** | **int** | Last time monthly rollup ran (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**duration** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthlyDuration**](V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthlyDuration.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_rollup_stats_monthly import V0044RollupStatsMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of V0044RollupStatsMonthly from a JSON string
v0044_rollup_stats_monthly_instance = V0044RollupStatsMonthly.from_json(json)
# print the JSON string representation of the object
print(V0044RollupStatsMonthly.to_json())

# convert the object into a dict
v0044_rollup_stats_monthly_dict = v0044_rollup_stats_monthly_instance.to_dict()
# create an instance of V0044RollupStatsMonthly from a dict
v0044_rollup_stats_monthly_from_dict = V0044RollupStatsMonthly.from_dict(v0044_rollup_stats_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


