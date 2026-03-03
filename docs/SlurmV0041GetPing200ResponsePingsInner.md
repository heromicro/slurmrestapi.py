# SlurmV0041GetPing200ResponsePingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Target for ping | [optional] 
**pinged** | **str** | Ping result | [optional] 
**latency** | **int** | Number of microseconds it took to successfully ping or timeout | [optional] 
**mode** | **str** | The operating mode of the responding slurmctld | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_ping200_response_pings_inner import SlurmV0041GetPing200ResponsePingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetPing200ResponsePingsInner from a JSON string
slurm_v0041_get_ping200_response_pings_inner_instance = SlurmV0041GetPing200ResponsePingsInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetPing200ResponsePingsInner.to_json())

# convert the object into a dict
slurm_v0041_get_ping200_response_pings_inner_dict = slurm_v0041_get_ping200_response_pings_inner_instance.to_dict()
# create an instance of SlurmV0041GetPing200ResponsePingsInner from a dict
slurm_v0041_get_ping200_response_pings_inner_from_dict = SlurmV0041GetPing200ResponsePingsInner.from_dict(slurm_v0041_get_ping200_response_pings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


