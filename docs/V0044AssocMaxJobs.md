# V0044AssocMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per** | [**V0044AssocMaxJobsPer**](V0044AssocMaxJobsPer.md) |  | [optional] 
**active** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**accruing** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**total** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_assoc_max_jobs import V0044AssocMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AssocMaxJobs from a JSON string
v0044_assoc_max_jobs_instance = V0044AssocMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0044AssocMaxJobs.to_json())

# convert the object into a dict
v0044_assoc_max_jobs_dict = v0044_assoc_max_jobs_instance.to_dict()
# create an instance of V0044AssocMaxJobs from a dict
v0044_assoc_max_jobs_from_dict = V0044AssocMaxJobs.from_dict(v0044_assoc_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


