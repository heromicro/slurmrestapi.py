# V0044UpdateNodeMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**cpu_bind** | **int** | Default method for binding tasks to allocated CPUs | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**features** | **List[str]** |  | [optional] 
**features_act** | **List[str]** |  | [optional] 
**gres** | **str** | Generic resources | [optional] 
**address** | **List[str]** |  | [optional] 
**hostname** | **List[str]** |  | [optional] 
**name** | **List[str]** |  | [optional] 
**state** | **List[str]** | New state to assign to the node | [optional] 
**reason** | **str** | Reason for node being DOWN or DRAINING | [optional] 
**reason_uid** | **str** | User ID to associate with the reason (needed if user root is sending message) | [optional] 
**resume_after** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**topology_str** | **str** | Topology | [optional] 
**weight** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_update_node_msg import V0044UpdateNodeMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0044UpdateNodeMsg from a JSON string
v0044_update_node_msg_instance = V0044UpdateNodeMsg.from_json(json)
# print the JSON string representation of the object
print(V0044UpdateNodeMsg.to_json())

# convert the object into a dict
v0044_update_node_msg_dict = v0044_update_node_msg_instance.to_dict()
# create an instance of V0044UpdateNodeMsg from a dict
v0044_update_node_msg_from_dict = V0044UpdateNodeMsg.from_dict(v0044_update_node_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


