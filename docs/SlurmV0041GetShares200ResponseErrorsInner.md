# SlurmV0041GetShares200ResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Long form error description | [optional] 
**error_number** | **int** | Slurm numeric error identifier | [optional] 
**error** | **str** | Short form error description | [optional] 
**source** | **str** | Source of error or where error was first detected | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_errors_inner import SlurmV0041GetShares200ResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseErrorsInner from a JSON string
slurm_v0041_get_shares200_response_errors_inner_instance = SlurmV0041GetShares200ResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseErrorsInner.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_errors_inner_dict = slurm_v0041_get_shares200_response_errors_inner_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseErrorsInner from a dict
slurm_v0041_get_shares200_response_errors_inner_from_dict = SlurmV0041GetShares200ResponseErrorsInner.from_dict(slurm_v0041_get_shares200_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


