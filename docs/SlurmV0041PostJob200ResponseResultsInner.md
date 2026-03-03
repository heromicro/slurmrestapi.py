# SlurmV0041PostJob200ResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Job ID for updated job | [optional] 
**step_id** | **str** | Step ID for updated job | [optional] 
**error** | **str** | Verbose update status or error | [optional] 
**error_code** | **int** | Verbose update status or error | [optional] 
**why** | **str** | Update response message | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job200_response_results_inner import SlurmV0041PostJob200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJob200ResponseResultsInner from a JSON string
slurm_v0041_post_job200_response_results_inner_instance = SlurmV0041PostJob200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJob200ResponseResultsInner.to_json())

# convert the object into a dict
slurm_v0041_post_job200_response_results_inner_dict = slurm_v0041_post_job200_response_results_inner_instance.to_dict()
# create an instance of SlurmV0041PostJob200ResponseResultsInner from a dict
slurm_v0041_post_job200_response_results_inner_from_dict = SlurmV0041PostJob200ResponseResultsInner.from_dict(slurm_v0041_post_job200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


