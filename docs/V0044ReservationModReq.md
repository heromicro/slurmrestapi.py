# V0044ReservationModReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservations** | [**List[V0044ReservationDescMsg]**](V0044ReservationDescMsg.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_reservation_mod_req import V0044ReservationModReq

# TODO update the JSON string below
json = "{}"
# create an instance of V0044ReservationModReq from a JSON string
v0044_reservation_mod_req_instance = V0044ReservationModReq.from_json(json)
# print the JSON string representation of the object
print(V0044ReservationModReq.to_json())

# convert the object into a dict
v0044_reservation_mod_req_dict = v0044_reservation_mod_req_instance.to_dict()
# create an instance of V0044ReservationModReq from a dict
v0044_reservation_mod_req_from_dict = V0044ReservationModReq.from_dict(v0044_reservation_mod_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


