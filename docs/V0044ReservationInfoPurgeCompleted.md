# V0044ReservationInfoPurgeCompleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_reservation_info_purge_completed import V0044ReservationInfoPurgeCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of V0044ReservationInfoPurgeCompleted from a JSON string
v0044_reservation_info_purge_completed_instance = V0044ReservationInfoPurgeCompleted.from_json(json)
# print the JSON string representation of the object
print(V0044ReservationInfoPurgeCompleted.to_json())

# convert the object into a dict
v0044_reservation_info_purge_completed_dict = v0044_reservation_info_purge_completed_instance.to_dict()
# create an instance of V0044ReservationInfoPurgeCompleted from a dict
v0044_reservation_info_purge_completed_from_dict = V0044ReservationInfoPurgeCompleted.from_dict(v0044_reservation_info_purge_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


