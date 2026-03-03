# V0044JobModify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerComment**](V0041OpenapiSlurmdbdJobsRespJobsInnerComment.md) |  | [optional] 
**derived_exit_code** | [**V0044ProcessExitCodeVerbose**](V0044ProcessExitCodeVerbose.md) |  | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**tres** | [**V0044JobModifyTres**](V0044JobModifyTres.md) |  | [optional] 
**wckey** | **str** | Workload characterization key | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_modify import V0044JobModify

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobModify from a JSON string
v0044_job_modify_instance = V0044JobModify.from_json(json)
# print the JSON string representation of the object
print(V0044JobModify.to_json())

# convert the object into a dict
v0044_job_modify_dict = v0044_job_modify_instance.to_dict()
# create an instance of V0044JobModify from a dict
v0044_job_modify_from_dict = V0044JobModify.from_dict(v0044_job_modify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


