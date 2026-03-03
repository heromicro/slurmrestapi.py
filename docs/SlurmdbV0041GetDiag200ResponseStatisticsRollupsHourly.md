# SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of hourly rollups since last_run | [optional] 
**last_run** | **int** | Last time hourly rollup ran (UNIX timestamp) | [optional] 
**duration** | [**SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourlyDuration**](SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourlyDuration.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics_rollups_hourly import SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly from a JSON string
slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_instance = SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_dict = slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly from a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_from_dict = SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly.from_dict(slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


