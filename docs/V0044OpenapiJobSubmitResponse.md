# V0044OpenapiJobSubmitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | submitted Job ID | [optional] 
**step_id** | **str** | submitted Step ID | [optional] 
**job_submit_user_msg** | **str** | Job submission user message | [optional] 
**meta** | [**V0044OpenapiMeta**](V0044OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0044OpenapiError]**](V0044OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0044OpenapiWarning]**](V0044OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_job_submit_response import V0044OpenapiJobSubmitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiJobSubmitResponse from a JSON string
v0044_openapi_job_submit_response_instance = V0044OpenapiJobSubmitResponse.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiJobSubmitResponse.to_json())

# convert the object into a dict
v0044_openapi_job_submit_response_dict = v0044_openapi_job_submit_response_instance.to_dict()
# create an instance of V0044OpenapiJobSubmitResponse from a dict
v0044_openapi_job_submit_response_from_dict = V0044OpenapiJobSubmitResponse.from_dict(v0044_openapi_job_submit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


