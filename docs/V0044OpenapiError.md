# V0044OpenapiError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Long form error description | [optional] 
**error_number** | **int** | Slurm numeric error identifier | [optional] 
**error** | **str** | Short form error description | [optional] 
**source** | **str** | Source of error or where error was first detected | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_error import V0044OpenapiError

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiError from a JSON string
v0044_openapi_error_instance = V0044OpenapiError.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiError.to_json())

# convert the object into a dict
v0044_openapi_error_dict = v0044_openapi_error_instance.to_dict()
# create an instance of V0044OpenapiError from a dict
v0044_openapi_error_from_dict = V0044OpenapiError.from_dict(v0044_openapi_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


