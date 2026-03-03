# SlurmdbV0041GetDiag200ResponseStatisticsRollups

Rollup statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | [**SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly**](SlurmdbV0041GetDiag200ResponseStatisticsRollupsHourly.md) |  | [optional] 
**daily** | [**SlurmdbV0041GetDiag200ResponseStatisticsRollupsDaily**](SlurmdbV0041GetDiag200ResponseStatisticsRollupsDaily.md) |  | [optional] 
**monthly** | [**SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthly**](SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthly.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics_rollups import SlurmdbV0041GetDiag200ResponseStatisticsRollups

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollups from a JSON string
slurmdb_v0041_get_diag200_response_statistics_rollups_instance = SlurmdbV0041GetDiag200ResponseStatisticsRollups.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatisticsRollups.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_dict = slurmdb_v0041_get_diag200_response_statistics_rollups_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollups from a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_from_dict = SlurmdbV0041GetDiag200ResponseStatisticsRollups.from_dict(slurmdb_v0041_get_diag200_response_statistics_rollups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


