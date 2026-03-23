# V0044QosPreempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | **List[str]** |  | [optional] 
**mode** | **List[str]** | PreemptMode - Mechanism used to preempt jobs or enable gang scheduling | [optional] 
**exempt_time** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_qos_preempt import V0044QosPreempt

# TODO update the JSON string below
json = "{}"
# create an instance of V0044QosPreempt from a JSON string
v0044_qos_preempt_instance = V0044QosPreempt.from_json(json)
# print the JSON string representation of the object
print(V0044QosPreempt.to_json())

# convert the object into a dict
v0044_qos_preempt_dict = v0044_qos_preempt_instance.to_dict()
# create an instance of V0044QosPreempt from a dict
v0044_qos_preempt_from_dict = V0044QosPreempt.from_dict(v0044_qos_preempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


