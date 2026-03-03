# V0044OpenapiJobModifyReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id_list** | **List[str]** |  | [optional] 
**job_rec** | [**V0044JobModify**](V0044JobModify.md) |  | [optional] 
**meta** | [**V0044OpenapiMeta**](V0044OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0044OpenapiError]**](V0044OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0044OpenapiWarning]**](V0044OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_job_modify_req import V0044OpenapiJobModifyReq

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiJobModifyReq from a JSON string
v0044_openapi_job_modify_req_instance = V0044OpenapiJobModifyReq.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiJobModifyReq.to_json())

# convert the object into a dict
v0044_openapi_job_modify_req_dict = v0044_openapi_job_modify_req_instance.to_dict()
# create an instance of V0044OpenapiJobModifyReq from a dict
v0044_openapi_job_modify_req_from_dict = V0044OpenapiJobModifyReq.from_dict(v0044_openapi_job_modify_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


