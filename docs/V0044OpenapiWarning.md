# V0044OpenapiWarning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Long form warning description | [optional] 
**source** | **str** | Source of warning or where warning was first detected | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_warning import V0044OpenapiWarning

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiWarning from a JSON string
v0044_openapi_warning_instance = V0044OpenapiWarning.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiWarning.to_json())

# convert the object into a dict
v0044_openapi_warning_dict = v0044_openapi_warning_instance.to_dict()
# create an instance of V0044OpenapiWarning from a dict
v0044_openapi_warning_from_dict = V0044OpenapiWarning.from_dict(v0044_openapi_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


