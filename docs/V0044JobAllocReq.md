# V0044JobAllocReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hetjob** | [**List[V0044JobDescMsg]**](V0044JobDescMsg.md) |  | [optional] 
**job** | [**V0044JobDescMsg**](V0044JobDescMsg.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_alloc_req import V0044JobAllocReq

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobAllocReq from a JSON string
v0044_job_alloc_req_instance = V0044JobAllocReq.from_json(json)
# print the JSON string representation of the object
print(V0044JobAllocReq.to_json())

# convert the object into a dict
v0044_job_alloc_req_dict = v0044_job_alloc_req_instance.to_dict()
# create an instance of V0044JobAllocReq from a dict
v0044_job_alloc_req_from_dict = V0044JobAllocReq.from_dict(v0044_job_alloc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


