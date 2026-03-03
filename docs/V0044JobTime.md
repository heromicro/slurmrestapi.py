# V0044JobTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | Elapsed time in seconds | [optional] 
**eligible** | **int** | Time when the job became eligible to run (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**end** | **int** | End time (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**planned** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**start** | **int** | Time execution began (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**submission** | **int** | Time when the job was submitted (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**suspended** | **int** | Total time in suspended state in seconds | [optional] 
**system** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerTimeSystem**](V0041OpenapiSlurmdbdJobsRespJobsInnerTimeSystem.md) |  | [optional] 
**limit** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**total** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerTimeTotal**](V0041OpenapiSlurmdbdJobsRespJobsInnerTimeTotal.md) |  | [optional] 
**user** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerTimeUser**](V0041OpenapiSlurmdbdJobsRespJobsInnerTimeUser.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_time import V0044JobTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobTime from a JSON string
v0044_job_time_instance = V0044JobTime.from_json(json)
# print the JSON string representation of the object
print(V0044JobTime.to_json())

# convert the object into a dict
v0044_job_time_dict = v0044_job_time_instance.to_dict()
# create an instance of V0044JobTime from a dict
v0044_job_time_from_dict = V0044JobTime.from_dict(v0044_job_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


