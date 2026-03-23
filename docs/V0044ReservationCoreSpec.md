# V0044ReservationCoreSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **str** | Name of reserved node | [optional] 
**core** | **str** | IDs of reserved cores | [optional] 

## Example

```python
from slurmrestapi.models.v0044_reservation_core_spec import V0044ReservationCoreSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V0044ReservationCoreSpec from a JSON string
v0044_reservation_core_spec_instance = V0044ReservationCoreSpec.from_json(json)
# print the JSON string representation of the object
print(V0044ReservationCoreSpec.to_json())

# convert the object into a dict
v0044_reservation_core_spec_dict = v0044_reservation_core_spec_instance.to_dict()
# create an instance of V0044ReservationCoreSpec from a dict
v0044_reservation_core_spec_from_dict = V0044ReservationCoreSpec.from_dict(v0044_reservation_core_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


