# SlurmV0041GetDiag200ResponseStatisticsJobStatesTs

When the job state counts were gathered (UNIX timestamp)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_diag200_response_statistics_job_states_ts import SlurmV0041GetDiag200ResponseStatisticsJobStatesTs

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetDiag200ResponseStatisticsJobStatesTs from a JSON string
slurm_v0041_get_diag200_response_statistics_job_states_ts_instance = SlurmV0041GetDiag200ResponseStatisticsJobStatesTs.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetDiag200ResponseStatisticsJobStatesTs.to_json())

# convert the object into a dict
slurm_v0041_get_diag200_response_statistics_job_states_ts_dict = slurm_v0041_get_diag200_response_statistics_job_states_ts_instance.to_dict()
# create an instance of SlurmV0041GetDiag200ResponseStatisticsJobStatesTs from a dict
slurm_v0041_get_diag200_response_statistics_job_states_ts_from_dict = SlurmV0041GetDiag200ResponseStatisticsJobStatesTs.from_dict(slurm_v0041_get_diag200_response_statistics_job_states_ts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


