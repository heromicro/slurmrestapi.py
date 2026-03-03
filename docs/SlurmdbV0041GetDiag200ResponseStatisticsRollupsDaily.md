# SlurmdbV0041GetDiag200ResponseStatisticsRollupsDaily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of daily rollups since last_run | [optional] 
**last_run** | **int** | Last time daily rollup ran (UNIX timestamp) | [optional] 
**duration** | [**SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration**](SlurmdbV0041GetDiag200ResponseStatisticsRollupsDailyDuration.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics_rollups_daily import SlurmdbV0041GetDiag200ResponseStatisticsRollupsDaily

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsDaily from a JSON string
slurmdb_v0041_get_diag200_response_statistics_rollups_daily_instance = SlurmdbV0041GetDiag200ResponseStatisticsRollupsDaily.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatisticsRollupsDaily.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_daily_dict = slurmdb_v0041_get_diag200_response_statistics_rollups_daily_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsDaily from a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_daily_from_dict = SlurmdbV0041GetDiag200ResponseStatisticsRollupsDaily.from_dict(slurmdb_v0041_get_diag200_response_statistics_rollups_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


