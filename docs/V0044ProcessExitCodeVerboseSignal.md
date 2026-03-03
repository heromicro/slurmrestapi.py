# V0044ProcessExitCodeVerboseSignal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**V0044Uint16NoValStruct**](V0044Uint16NoValStruct.md) |  | [optional] 
**name** | **str** | Signal sent to process (name) | [optional] 

## Example

```python
from slurmrestapi.models.v0044_process_exit_code_verbose_signal import V0044ProcessExitCodeVerboseSignal

# TODO update the JSON string below
json = "{}"
# create an instance of V0044ProcessExitCodeVerboseSignal from a JSON string
v0044_process_exit_code_verbose_signal_instance = V0044ProcessExitCodeVerboseSignal.from_json(json)
# print the JSON string representation of the object
print(V0044ProcessExitCodeVerboseSignal.to_json())

# convert the object into a dict
v0044_process_exit_code_verbose_signal_dict = v0044_process_exit_code_verbose_signal_instance.to_dict()
# create an instance of V0044ProcessExitCodeVerboseSignal from a dict
v0044_process_exit_code_verbose_signal_from_dict = V0044ProcessExitCodeVerboseSignal.from_dict(v0044_process_exit_code_verbose_signal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


