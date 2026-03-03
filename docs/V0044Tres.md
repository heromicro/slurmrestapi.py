# V0044Tres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | TRES type (CPU, MEM, etc) | 
**name** | **str** | TRES name (if applicable) | [optional] 
**id** | **int** | ID used in the database | [optional] 
**count** | **int** | TRES count (0 if listed generically) | [optional] 

## Example

```python
from slurmrestapi.models.v0044_tres import V0044Tres

# TODO update the JSON string below
json = "{}"
# create an instance of V0044Tres from a JSON string
v0044_tres_instance = V0044Tres.from_json(json)
# print the JSON string representation of the object
print(V0044Tres.to_json())

# convert the object into a dict
v0044_tres_dict = v0044_tres_instance.to_dict()
# create an instance of V0044Tres from a dict
v0044_tres_from_dict = V0044Tres.from_dict(v0044_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


