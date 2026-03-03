# V0044QosLimitsMaxActiveJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accruing** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**count** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits_max_active_jobs import V0044QosLimitsMaxActiveJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimitsMaxActiveJobs from a JSON string
v0044_qos_limits_max_active_jobs_instance = V0044QosLimitsMaxActiveJobs.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimitsMaxActiveJobs.to_json())

# convert the object into a dict
v0044_qos_limits_max_active_jobs_dict = v0044_qos_limits_max_active_jobs_instance.to_dict()
# create an instance of V0044QosLimitsMaxActiveJobs from a dict
v0044_qos_limits_max_active_jobs_from_dict = V0044QosLimitsMaxActiveJobs.from_dict(v0044_qos_limits_max_active_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


