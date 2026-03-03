# SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of monthly rollups since last_run | [optional] 
**last_run** | **int** | Last time monthly rollup ran (UNIX timestamp) | [optional] 
**duration** | [**SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthlyDuration**](SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthlyDuration.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics_rollups_monthly import SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthly from a JSON string
slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_instance = SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthly.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthly.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_dict = slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthly from a dict
slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_from_dict = SlurmdbV0041GetDiag200ResponseStatisticsRollupsMonthly.from_dict(slurmdb_v0041_get_diag200_response_statistics_rollups_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


