# SlurmV0041GetDiag200ResponseStatisticsRpcsByUserInner

RPCs by user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID (numeric) | 
**user** | **str** | User name | 
**count** | **int** | Number of RPCs received | 
**total_time** | **int** | Total time spent processing RPC in seconds | 
**average_time** | [**SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInnerAverageTime**](SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInnerAverageTime.md) |  | 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_diag200_response_statistics_rpcs_by_user_inner import SlurmV0041GetDiag200ResponseStatisticsRpcsByUserInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetDiag200ResponseStatisticsRpcsByUserInner from a JSON string
slurm_v0041_get_diag200_response_statistics_rpcs_by_user_inner_instance = SlurmV0041GetDiag200ResponseStatisticsRpcsByUserInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetDiag200ResponseStatisticsRpcsByUserInner.to_json())

# convert the object into a dict
slurm_v0041_get_diag200_response_statistics_rpcs_by_user_inner_dict = slurm_v0041_get_diag200_response_statistics_rpcs_by_user_inner_instance.to_dict()
# create an instance of SlurmV0041GetDiag200ResponseStatisticsRpcsByUserInner from a dict
slurm_v0041_get_diag200_response_statistics_rpcs_by_user_inner_from_dict = SlurmV0041GetDiag200ResponseStatisticsRpcsByUserInner.from_dict(slurm_v0041_get_diag200_response_statistics_rpcs_by_user_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


