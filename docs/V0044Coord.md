# V0044Coord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User name | 
**direct** | **bool** | Indicates whether the coordinator was directly assigned to this account | [optional] 

## Example

```python
from slurmrestapi.models.v0044_coord import V0044Coord

# TODO update the JSON string below
json = "{}"
# create an instance of V0044Coord from a JSON string
v0044_coord_instance = V0044Coord.from_json(json)
# print the JSON string representation of the object
print(V0044Coord.to_json())

# convert the object into a dict
v0044_coord_dict = v0044_coord_instance.to_dict()
# create an instance of V0044Coord from a dict
v0044_coord_from_dict = V0044Coord.from_dict(v0044_coord_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


