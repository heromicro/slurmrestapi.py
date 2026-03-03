# V0044JobDescMsgRlimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**fsize** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**data** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**stack** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**core** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**rss** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**nproc** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**nofile** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**memlock** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**var_as** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_desc_msg_rlimits import V0044JobDescMsgRlimits

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobDescMsgRlimits from a JSON string
v0044_job_desc_msg_rlimits_instance = V0044JobDescMsgRlimits.from_json(json)
# print the JSON string representation of the object
print(V0044JobDescMsgRlimits.to_json())

# convert the object into a dict
v0044_job_desc_msg_rlimits_dict = v0044_job_desc_msg_rlimits_instance.to_dict()
# create an instance of V0044JobDescMsgRlimits from a dict
v0044_job_desc_msg_rlimits_from_dict = V0044JobDescMsgRlimits.from_dict(v0044_job_desc_msg_rlimits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


