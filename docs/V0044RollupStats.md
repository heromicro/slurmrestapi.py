# V0044RollupStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | [**V0044RollupStatsHourly**](V0044RollupStatsHourly.md) |  | [optional] 
**daily** | [**V0044RollupStatsDaily**](V0044RollupStatsDaily.md) |  | [optional] 
**monthly** | [**V0044RollupStatsMonthly**](V0044RollupStatsMonthly.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_rollup_stats import V0044RollupStats

# TODO update the JSON string below
json = "{}"
# create an instance of V0044RollupStats from a JSON string
v0044_rollup_stats_instance = V0044RollupStats.from_json(json)
# print the JSON string representation of the object
print(V0044RollupStats.to_json())

# convert the object into a dict
v0044_rollup_stats_dict = v0044_rollup_stats_instance.to_dict()
# create an instance of V0044RollupStats from a dict
v0044_rollup_stats_from_dict = V0044RollupStats.from_dict(v0044_rollup_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


