# V0044QosLimitsMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**active_jobs** | [**V0044QosLimitsMaxJobsActiveJobs**](V0044QosLimitsMaxJobsActiveJobs.md) |  | [optional] 
**per** | [**V0044QosLimitsMaxJobsActiveJobsPer**](V0044QosLimitsMaxJobsActiveJobsPer.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits_max_jobs import V0044QosLimitsMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimitsMaxJobs from a JSON string
v0044_qos_limits_max_jobs_instance = V0044QosLimitsMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimitsMaxJobs.to_json())

# convert the object into a dict
v0044_qos_limits_max_jobs_dict = v0044_qos_limits_max_jobs_instance.to_dict()
# create an instance of V0044QosLimitsMaxJobs from a dict
v0044_qos_limits_max_jobs_from_dict = V0044QosLimitsMaxJobs.from_dict(v0044_qos_limits_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


