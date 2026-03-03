# SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourlyDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last** | **int** | Total time spent doing last daily rollup (seconds) | [optional] 
**max** | **int** | Longest hourly rollup time (seconds) | [optional] 
**time** | **int** | Total time spent doing hourly rollups (seconds) | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_duration import SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourlyDuration

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourlyDuration from a JSON string
slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_duration_instance = SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourlyDuration.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourlyDuration.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_duration_dict = slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_duration_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourlyDuration from a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_duration_from_dict = SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourlyDuration.from_dict(slurmdb_v0041_get_diag200_response_statistics_rollups_hourly_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


