# V0044JobState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **List[str]** | Current state | [optional] 
**reason** | **str** | Reason for previous Pending or Failed state | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_state import V0044JobState

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobState from a JSON string
v0044_job_state_instance = V0044JobState.from_json(json)
# print the JSON string representation of the object
print(V0044JobState.to_json())

# convert the object into a dict
v0044_job_state_dict = v0044_job_state_instance.to_dict()
# create an instance of V0044JobState from a dict
v0044_job_state_from_dict = V0044JobState.from_dict(v0044_job_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


