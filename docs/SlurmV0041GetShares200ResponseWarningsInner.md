# SlurmV0041GetShares200ResponseWarningsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Long form warning description | [optional] 
**source** | **str** | Source of warning or where warning was first detected | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_warnings_inner import SlurmV0041GetShares200ResponseWarningsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseWarningsInner from a JSON string
slurm_v0041_get_shares200_response_warnings_inner_instance = SlurmV0041GetShares200ResponseWarningsInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseWarningsInner.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_warnings_inner_dict = slurm_v0041_get_shares200_response_warnings_inner_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseWarningsInner from a dict
slurm_v0041_get_shares200_response_warnings_inner_from_dict = SlurmV0041GetShares200ResponseWarningsInner.from_dict(slurm_v0041_get_shares200_response_warnings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


