# SlurmdbV0041GetDiag200ResponseStatisticsUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User ID | [optional] 
**count** | **int** | Number of RPCs processed | [optional] 
**time** | [**SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime**](SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_get_diag200_response_statistics_users_inner import SlurmdbV0041GetDiag200ResponseStatisticsUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsUsersInner from a JSON string
slurmdb_v0041_get_diag200_response_statistics_users_inner_instance = SlurmdbV0041GetDiag200ResponseStatisticsUsersInner.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041GetDiag200ResponseStatisticsUsersInner.to_json())

# convert the object into a dict
slurmdb_v0041_get_diag200_response_statistics_users_inner_dict = slurmdb_v0041_get_diag200_response_statistics_users_inner_instance.to_dict()
# create an instance of SlurmdbV0041GetDiag200ResponseStatisticsUsersInner from a dict
slurmdb_v0041_get_diag200_response_statistics_users_inner_from_dict = SlurmdbV0041GetDiag200ResponseStatisticsUsersInner.from_dict(slurmdb_v0041_get_diag200_response_statistics_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


