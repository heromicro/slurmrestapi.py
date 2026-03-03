# V0044JobRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_type** | **List[str]** | Scheduler consumable resource selection type | 
**nodes** | [**V0044JobResNodes**](V0044JobResNodes.md) |  | [optional] 
**cpus** | **int** | Number of allocated CPUs | 
**threads_per_core** | [**V0044Uint16NoValStruct**](V0044Uint16NoValStruct.md) |  | 

## Example

```python
from slurmrestapi.models.v0044_job_res import V0044JobRes

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobRes from a JSON string
v0044_job_res_instance = V0044JobRes.from_json(json)
# print the JSON string representation of the object
print(V0044JobRes.to_json())

# convert the object into a dict
v0044_job_res_dict = v0044_job_res_instance.to_dict()
# create an instance of V0044JobRes from a dict
v0044_job_res_from_dict = V0044JobRes.from_dict(v0044_job_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


