# V0044StatsUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User ID | [optional] 
**count** | **int** | Number of RPCs processed | [optional] 
**time** | [**SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime**](SlurmdbV0041GetDiag200ResponseStatisticsRPCsInnerTime.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_stats_user import V0044StatsUser

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StatsUser from a JSON string
v0044_stats_user_instance = V0044StatsUser.from_json(json)
# print the JSON string representation of the object
print(V0044StatsUser.to_json())

# convert the object into a dict
v0044_stats_user_dict = v0044_stats_user_instance.to_dict()
# create an instance of V0044StatsUser from a dict
v0044_stats_user_from_dict = V0044StatsUser.from_dict(v0044_stats_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


