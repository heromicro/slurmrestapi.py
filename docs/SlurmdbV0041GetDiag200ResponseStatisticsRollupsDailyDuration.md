# SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last** | **int** | Total time spent doing daily daily rollup (seconds) | [optional] 
**max** | **int** | Longest daily rollup time (seconds) | [optional] 
**time** | **int** | Total time spent doing daily rollups (seconds) | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics_rollups_daily_duration import SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration from a JSON string
slurmdb_v0041_get_diag200_response_statistics_rollups_daily_duration_instance = SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_daily_duration_dict = slurmdb_v0041_get_diag200_response_statistics_rollups_daily_duration_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration from a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_daily_duration_from_dict = SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration.from_dict(slurmdb_v0041_get_diag200_response_statistics_rollups_daily_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


