# SlurmV0041GetDiag200ResponseStatisticsPendingRpcsInner

Pending RPCs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string | 
**count** | **int** | Number of pending RPCs queued | 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_diag200_response_statistics_pending_rpcs_inner import SlurmV0041GetDiag200ResponseStatisticsPendingRpcsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetDiag200ResponseStatisticsPendingRpcsInner from a JSON string
slurm_v0041_get_diag200_response_statistics_pending_rpcs_inner_instance = SlurmV0041GetDiag200ResponseStatisticsPendingRpcsInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetDiag200ResponseStatisticsPendingRpcsInner.to_json())

# convert the object into a dict
slurm_v0041_get_diag200_response_statistics_pending_rpcs_inner_dict = slurm_v0041_get_diag200_response_statistics_pending_rpcs_inner_instance.to_dict()
# create an instance of SlurmV0041GetDiag200ResponseStatisticsPendingRpcsInner from a dict
slurm_v0041_get_diag200_response_statistics_pending_rpcs_inner_from_dict = SlurmV0041GetDiag200ResponseStatisticsPendingRpcsInner.from_dict(slurm_v0041_get_diag200_response_statistics_pending_rpcs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


