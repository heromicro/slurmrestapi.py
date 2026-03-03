# SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthlyDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last** | **int** | Total time spent doing monthly daily rollup (seconds) | [optional] 
**max** | **int** | Longest monthly rollup time (seconds) | [optional] 
**time** | **int** | Total time spent doing monthly rollups (seconds) | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_duration import SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthlyDuration

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthlyDuration from a JSON string
slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_duration_instance = SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthlyDuration.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthlyDuration.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_duration_dict = slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_duration_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthlyDuration from a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_duration_from_dict = SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthlyDuration.from_dict(slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


