# V0044QosLimitsMin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_threshold** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**tres** | [**V0044QosLimitsMinTres**](V0044QosLimitsMinTres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_limits_min import V0044QosLimitsMin

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosLimitsMin from a JSON string
v0044_qos_limits_min_instance = V0044QosLimitsMin.from_json(json)
# print the JSON string representation of the object
print(V0044QosLimitsMin.to_json())

# convert the object into a dict
v0044_qos_limits_min_dict = v0044_qos_limits_min_instance.to_dict()
# create an instance of V0044QosLimitsMin from a dict
v0044_qos_limits_min_from_dict = V0044QosLimitsMin.from_dict(v0044_qos_limits_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


