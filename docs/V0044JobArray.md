# V0044JobArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Job ID of job array, or 0 if N/A | [optional] 
**limits** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayLimits**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayLimits.md) |  | [optional] 
**task_id** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**task** | **str** | String expression of task IDs in this record | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_array import V0044JobArray

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobArray from a JSON string
v0044_job_array_instance = V0044JobArray.from_json(json)
# print the JSON string representation of the object
print(V0044JobArray.to_json())

# convert the object into a dict
v0044_job_array_dict = v0044_job_array_instance.to_dict()
# create an instance of V0044JobArray from a dict
v0044_job_array_from_dict = V0044JobArray.from_dict(v0044_job_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


