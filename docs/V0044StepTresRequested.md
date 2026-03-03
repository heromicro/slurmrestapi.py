# V0044StepTresRequested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**min** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**average** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**total** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_step_tres_requested import V0044StepTresRequested

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StepTresRequested from a JSON string
v0044_step_tres_requested_instance = V0044StepTresRequested.from_json(json)
# print the JSON string representation of the object
print(V0044StepTresRequested.to_json())

# convert the object into a dict
v0044_step_tres_requested_dict = v0044_step_tres_requested_instance.to_dict()
# create an instance of V0044StepTresRequested from a dict
v0044_step_tres_requested_from_dict = V0044StepTresRequested.from_dict(v0044_step_tres_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


