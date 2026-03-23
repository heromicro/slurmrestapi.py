# V0044OpenapiJobPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[V0044JobArrayResponseMsgEntry]**](V0044JobArrayResponseMsgEntry.md) |  | [optional] 
**meta** | [**V0044OpenapiMeta**](V0044OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0044OpenapiError]**](V0044OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0044OpenapiWarning]**](V0044OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_job_post_response import V0044OpenapiJobPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiJobPostResponse from a JSON string
v0044_openapi_job_post_response_instance = V0044OpenapiJobPostResponse.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiJobPostResponse.to_json())

# convert the object into a dict
v0044_openapi_job_post_response_dict = v0044_openapi_job_post_response_instance.to_dict()
# create an instance of V0044OpenapiJobPostResponse from a dict
v0044_openapi_job_post_response_from_dict = V0044OpenapiJobPostResponse.from_dict(v0044_openapi_job_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


