# SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **int** | Average RPC processing time in microseconds | [optional] 
**total** | **int** | Total RPC processing time in microseconds | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics_rpcs_inner_time import SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime from a JSON string
slurmdb_v0041_get_diag200_response_statistics_rpcs_inner_time_instance = SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_rpcs_inner_time_dict = slurmdb_v0041_get_diag200_response_statistics_rpcs_inner_time_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime from a dict
slurmdb_v0041_get_diag200_response_statistics_rpcs_inner_time_from_dict = SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime.from_dict(slurmdb_v0041_get_diag200_response_statistics_rpcs_inner_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


