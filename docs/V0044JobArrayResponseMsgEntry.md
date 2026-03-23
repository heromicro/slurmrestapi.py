# V0044JobArrayResponseMsgEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Job ID for updated job | [optional] 
**step_id** | **str** | Step ID for updated job | [optional] 
**error** | **str** | Verbose update status or error | [optional] 
**error_code** | **int** | Verbose update status or error | [optional] 
**why** | **str** | Update response message | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_array_response_msg_entry import V0044JobArrayResponseMsgEntry

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobArrayResponseMsgEntry from a JSON string
v0044_job_array_response_msg_entry_instance = V0044JobArrayResponseMsgEntry.from_json(json)
# print the JSON string representation of the object
print(V0044JobArrayResponseMsgEntry.to_json())

# convert the object into a dict
v0044_job_array_response_msg_entry_dict = v0044_job_array_response_msg_entry_instance.to_dict()
# create an instance of V0044JobArrayResponseMsgEntry from a dict
v0044_job_array_response_msg_entry_from_dict = V0044JobArrayResponseMsgEntry.from_dict(v0044_job_array_response_msg_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


