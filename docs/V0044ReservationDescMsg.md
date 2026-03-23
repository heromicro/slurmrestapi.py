# V0044ReservationDescMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **List[str]** |  | [optional] 
**burst_buffer** | **str** | BurstBuffer | [optional] 
**comment** | **str** | Arbitrary string | [optional] 
**core_count** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**duration** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**end_time** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**features** | **str** | Requested node features. Multiple values may be \&quot;&amp;\&quot; separated if all features are required (AND operation) or separated by \&quot;|\&quot; if any of the specified features are required (OR operation). Parenthesis are also supported for features to be ANDed together with counts of nodes having the specified features. | [optional] 
**flags** | **List[str]** | Flags associated with this reservation. Note, to remove flags use \&quot;NO_\&quot; prefixed flag excluding NO_HOLD_JOBS_AFTER_END | [optional] 
**groups** | **List[str]** |  | [optional] 
**licenses** | **List[str]** |  | [optional] 
**max_start_delay** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**name** | **str** | ReservationName | [optional] 
**node_count** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**node_list** | **List[str]** |  | [optional] 
**partition** | **str** | Partition used to reserve nodes from. This will attempt to allocate all nodes in the specified partition unless you request fewer resources than are available with core_cnt, node_cnt or tres. | [optional] 
**purge_completed** | [**V0044ReservationInfoPurgeCompleted**](V0044ReservationInfoPurgeCompleted.md) |  | [optional] 
**start_time** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 
**tres** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**users** | **List[str]** |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_reservation_desc_msg import V0044ReservationDescMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0044ReservationDescMsg from a JSON string
v0044_reservation_desc_msg_instance = V0044ReservationDescMsg.from_json(json)
# print the JSON string representation of the object
print(V0044ReservationDescMsg.to_json())

# convert the object into a dict
v0044_reservation_desc_msg_dict = v0044_reservation_desc_msg_instance.to_dict()
# create an instance of V0044ReservationDescMsg from a dict
v0044_reservation_desc_msg_from_dict = V0044ReservationDescMsg.from_dict(v0044_reservation_desc_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


