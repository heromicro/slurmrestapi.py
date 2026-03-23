# V0044NodeGresLayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | GRES name | 
**type** | **str** | GRES type (optional) | [optional] 
**count** | **int** | Count | [optional] 
**index** | **str** | Index | [optional] 

## Example

```python
from slurmrestapi.models.v0044_node_gres_layout import V0044NodeGresLayout

# TODO update the JSON string below
json = "{}"
# create an instance of V0044NodeGresLayout from a JSON string
v0044_node_gres_layout_instance = V0044NodeGresLayout.from_json(json)
# print the JSON string representation of the object
print(V0044NodeGresLayout.to_json())

# convert the object into a dict
v0044_node_gres_layout_dict = v0044_node_gres_layout_instance.to_dict()
# create an instance of V0044NodeGresLayout from a dict
v0044_node_gres_layout_from_dict = V0044NodeGresLayout.from_dict(v0044_node_gres_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


