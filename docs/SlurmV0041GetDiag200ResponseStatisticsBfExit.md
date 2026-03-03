# SlurmV0041GetDiag200ResponseStatisticsBfExit

Reasons for which the backfill scheduling cycle exited since last reset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_job_queue** | **int** | Reached end of queue | [optional] 
**bf_max_job_start** | **int** | Reached number of jobs allowed to start | [optional] 
**bf_max_job_test** | **int** | Reached number of jobs allowed to be tested | [optional] 
**bf_max_time** | **int** | Reached maximum allowed scheduler time | [optional] 
**bf_node_space_size** | **int** | Reached table size limit | [optional] 
**state_changed** | **int** | System state changed | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_diag200_response_statistics_bf_exit import SlurmV0041GetDiag200ResponseStatisticsBfExit

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetDiag200ResponseStatisticsBfExit from a JSON string
slurm_v0041_get_diag200_response_statistics_bf_exit_instance = SlurmV0041GetDiag200ResponseStatisticsBfExit.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetDiag200ResponseStatisticsBfExit.to_json())

# convert the object into a dict
slurm_v0041_get_diag200_response_statistics_bf_exit_dict = slurm_v0041_get_diag200_response_statistics_bf_exit_instance.to_dict()
# create an instance of SlurmV0041GetDiag200ResponseStatisticsBfExit from a dict
slurm_v0041_get_diag200_response_statistics_bf_exit_from_dict = SlurmV0041GetDiag200ResponseStatisticsBfExit.from_dict(slurm_v0041_get_diag200_response_statistics_bf_exit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


