# V0041OpenapiReservationResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservations** | [**List[V0041OpenapiReservationRespReservationsInner]**](V0041OpenapiReservationRespReservationsInner.md) | List of reservations | 
**last_update** | [**V0041OpenapiReservationRespLastUpdate**](V0041OpenapiReservationRespLastUpdate.md) |  | 
**meta** | [**SlurmV0041GetShares200ResponseMeta**](SlurmV0041GetShares200ResponseMeta.md) |  | [optional] 
**errors** | [**List[SlurmV0041GetShares200ResponseErrorsInner]**](SlurmV0041GetShares200ResponseErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[SlurmV0041GetShares200ResponseWarningsInner]**](SlurmV0041GetShares200ResponseWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrestapi.models.v0041_openapi_reservation_resp import V0041OpenapiReservationResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiReservationResp from a JSON string
v0041_openapi_reservation_resp_instance = V0041OpenapiReservationResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiReservationResp.to_json())

# convert the object into a dict
v0041_openapi_reservation_resp_dict = v0041_openapi_reservation_resp_instance.to_dict()
# create an instance of V0041OpenapiReservationResp from a dict
v0041_openapi_reservation_resp_from_dict = V0041OpenapiReservationResp.from_dict(v0041_openapi_reservation_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


