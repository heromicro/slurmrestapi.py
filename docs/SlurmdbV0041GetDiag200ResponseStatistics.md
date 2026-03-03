# SlurmdbV0041GetDiag200ResponseStatistics

statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_start** | **int** | When data collection started (UNIX timestamp) | [optional] 
**rollups** | [**SlurmdbV0041GetDiag200ResponseStatisticsRollups**](SlurmdbV0041GetDiag200ResponseStatisticsRollups.md) |  | [optional] 
**rpcs** | [**List[SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner]**](SlurmdbV0041GetDiag200ResponseStatisticsRPCsInner.md) | List of RPCs sent to the slurmdbd | [optional] 
**users** | [**List[SlurmdbV0041GetDiag200ResponseStatisticsUsersInner]**](SlurmdbV0041GetDiag200ResponseStatisticsUsersInner.md) | List of users that issued RPCs | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics import SlurmdbV0041GetDiag200ResponseStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatistics from a JSON string
slurmdb_v0041_get_diag200_response_statistics_instance = SlurmdbV0041GetDiag200ResponseStatistics.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatistics.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_dict = slurmdb_v0041_get_diag200_response_statistics_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatistics from a dict
slurmdb_v0041_get_diag200_response_statistics_from_dict = SlurmdbV0041GetDiag200ResponseStatistics.from_dict(slurmdb_v0041_get_diag200_response_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


