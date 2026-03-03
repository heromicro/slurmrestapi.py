# V0044NodeResourceLayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **str** | Node name | 
**sockets_per_node** | **int** | Sockets per node | [optional] 
**cores_per_socket** | **int** | Cores per socket | [optional] 
**mem_alloc** | **int** | Allocated memory | [optional] 
**core_bitmap** | **str** | Abstract core bitmap | [optional] 
**channel** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**gres** | [**List[V0044NodeGresLayout]**](V0044NodeGresLayout.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_node_resource_layout import V0044NodeResourceLayout

# TODO update the JSON string below
json = "{}"
# create an instance of V0044NodeResourceLayout from a JSON string
v0044_node_resource_layout_instance = V0044NodeResourceLayout.from_json(json)
# print the JSON string representation of the object
print(V0044NodeResourceLayout.to_json())

# convert the object into a dict
v0044_node_resource_layout_dict = v0044_node_resource_layout_instance.to_dict()
# create an instance of V0044NodeResourceLayout from a dict
v0044_node_resource_layout_from_dict = V0044NodeResourceLayout.from_dict(v0044_node_resource_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


