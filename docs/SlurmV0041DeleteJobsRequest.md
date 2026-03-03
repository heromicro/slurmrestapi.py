# SlurmV0041DeleteJobsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Filter jobs to a specific account | [optional] 
**flags** | **List[str]** | Filter jobs according to flags | [optional] 
**job_name** | **str** | Filter jobs to a specific name | [optional] 
**jobs** | **List[str]** | List of jobs to signal | [optional] 
**partition** | **str** | Filter jobs to a specific partition | [optional] 
**qos** | **str** | Filter jobs to a specific QOS | [optional] 
**reservation** | **str** | Filter jobs to a specific reservation | [optional] 
**signal** | **str** | Signal to send to jobs | [optional] 
**job_state** | **List[str]** | Filter jobs to a specific state | [optional] 
**user_id** | **str** | Filter jobs to a specific numeric user id | [optional] 
**user_name** | **str** | Filter jobs to a specific user name | [optional] 
**wckey** | **str** | Filter jobs to a specific wckey | [optional] 
**nodes** | **List[str]** | Filter jobs to a set of nodes | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_delete_jobs_request import SlurmV0041DeleteJobsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041DeleteJobsRequest from a JSON string
slurm_v0041_delete_jobs_request_instance = SlurmV0041DeleteJobsRequest.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041DeleteJobsRequest.to_json())

# convert the object into a dict
slurm_v0041_delete_jobs_request_dict = slurm_v0041_delete_jobs_request_instance.to_dict()
# create an instance of SlurmV0041DeleteJobsRequest from a dict
slurm_v0041_delete_jobs_request_from_dict = SlurmV0041DeleteJobsRequest.from_dict(slurm_v0041_delete_jobs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


