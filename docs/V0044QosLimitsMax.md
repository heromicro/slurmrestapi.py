# V0044QosLimitsMax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_jobs** | [**V0044QosLimitsMaxActiveJobs**](V0044QosLimitsMaxActiveJobs.md) |  | [optional] 
**jobs** | [**V0044QosLimitsMaxJobs**](V0044QosLimitsMaxJobs.md) |  | [optional] 
**tres** | [**V0044QosLimitsMaxTres**](V0044QosLimitsMaxTres.md) |  | [optional] 
**wall_clock** | [**V0044QosLimitsMaxWallClock**](V0044QosLimitsMaxWallClock.md) |  | [optional] 
**accruing** | [**V0044QosLimitsMaxJobsActiveJobs**](V0044QosLimitsMaxJobsActiveJobs.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits_max import V0044QosLimitsMax

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimitsMax from a JSON string
v0044_qos_limits_max_instance = V0044QosLimitsMax.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimitsMax.to_json())

# convert the object into a dict
v0044_qos_limits_max_dict = v0044_qos_limits_max_instance.to_dict()
# create an instance of V0044QosLimitsMax from a dict
v0044_qos_limits_max_from_dict = V0044QosLimitsMax.from_dict(v0044_qos_limits_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


