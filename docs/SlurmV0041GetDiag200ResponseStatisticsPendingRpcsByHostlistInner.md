# SlurmV0041GetDiag200ResponseStatisticsPendingRpcsByHostlistInner

Pending RPCs by hostlist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Message type as integer | 
**message_type** | **str** | Message type as string | 
**count** | **List[str]** | Number of RPCs received | 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_diag200_response_statistics_pending_rpcs_by_hostlist_inner import SlurmV0041GetDiag200ResponseStatisticsPendingRpcsByHostlistInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetDiag200ResponseStatisticsPendingRpcsByHostlistInner from a JSON string
slurm_v0041_get_diag200_response_statistics_pending_rpcs_by_hostlist_inner_instance = SlurmV0041GetDiag200ResponseStatisticsPendingRpcsByHostlistInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetDiag200ResponseStatisticsPendingRpcsByHostlistInner.to_json())

# convert the object into a dict
slurm_v0041_get_diag200_response_statistics_pending_rpcs_by_hostlist_inner_dict = slurm_v0041_get_diag200_response_statistics_pending_rpcs_by_hostlist_inner_instance.to_dict()
# create an instance of SlurmV0041GetDiag200ResponseStatisticsPendingRpcsByHostlistInner from a dict
slurm_v0041_get_diag200_response_statistics_pending_rpcs_by_hostlist_inner_from_dict = SlurmV0041GetDiag200ResponseStatisticsPendingRpcsByHostlistInner.from_dict(slurm_v0041_get_diag200_response_statistics_pending_rpcs_by_hostlist_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


