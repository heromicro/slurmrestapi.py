# SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInner

RPCs by type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string | 
**count** | **int** | Number of RPCs received | 
**queued** | **int** | Number of RPCs queued | 
**dropped** | **int** | Number of RPCs dropped | 
**cycle_last** | **int** | Number of RPCs processed within the last RPC queue cycle | 
**cycle_max** | **int** | Maximum number of RPCs processed within a RPC queue cycle since start | 
**total_time** | **int** | Total time spent processing RPC in seconds | 
**average_time** | [**SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInnerAverageTime**](SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInnerAverageTime.md) |  | 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_diag200_response_statistics_rpcs_by_message_type_inner import SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInner from a JSON string
slurm_v0041_get_diag200_response_statistics_rpcs_by_message_type_inner_instance = SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInner.to_json())

# convert the object into a dict
slurm_v0041_get_diag200_response_statistics_rpcs_by_message_type_inner_dict = slurm_v0041_get_diag200_response_statistics_rpcs_by_message_type_inner_instance.to_dict()
# create an instance of SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInner from a dict
slurm_v0041_get_diag200_response_statistics_rpcs_by_message_type_inner_from_dict = SlurmV0041GetDiag200ResponseStatisticsRpcsByMessageTypeInner.from_dict(slurm_v0041_get_diag200_response_statistics_rpcs_by_message_type_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


