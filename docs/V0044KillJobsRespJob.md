# V0044KillJobsRespJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**V0041OpenapiKillJobsRespStatusInnerError**](V0041OpenapiKillJobsRespStatusInnerError.md) |  | [optional] 
**step_id** | **str** | Job or Step ID that signaling failed | 
**job_id** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | 
**federation** | [**V0041OpenapiKillJobsRespStatusInnerFederation**](V0041OpenapiKillJobsRespStatusInnerFederation.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_kill_jobs_resp_job import V0044KillJobsRespJob

# TODO update the JSON string below
json = "{}"
# create an instance of V0044KillJobsRespJob from a JSON string
v0044_kill_jobs_resp_job_instance = V0044KillJobsRespJob.from_json(json)
# print the JSON string representation of the object
print(V0044KillJobsRespJob.to_json())

# convert the object into a dict
v0044_kill_jobs_resp_job_dict = v0044_kill_jobs_resp_job_instance.to_dict()
# create an instance of V0044KillJobsRespJob from a dict
v0044_kill_jobs_resp_job_from_dict = V0044KillJobsRespJob.from_dict(v0044_kill_jobs_resp_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


