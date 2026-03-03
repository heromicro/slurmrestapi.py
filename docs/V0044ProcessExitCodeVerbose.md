# V0044ProcessExitCodeVerbose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **List[str]** | Status given by return code | [optional] 
**return_code** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**signal** | [**V0044ProcessExitCodeVerboseSignal**](V0044ProcessExitCodeVerboseSignal.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_process_exit_code_verbose import V0044ProcessExitCodeVerbose

# TODO update the JSON string below
json = "{}"
# create an instance of V0044ProcessExitCodeVerbose from a JSON string
v0044_process_exit_code_verbose_instance = V0044ProcessExitCodeVerbose.from_json(json)
# print the JSON string representation of the object
print(V0044ProcessExitCodeVerbose.to_json())

# convert the object into a dict
v0044_process_exit_code_verbose_dict = v0044_process_exit_code_verbose_instance.to_dict()
# create an instance of V0044ProcessExitCodeVerbose from a dict
v0044_process_exit_code_verbose_from_dict = V0044ProcessExitCodeVerbose.from_dict(v0044_process_exit_code_verbose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


