# SlurmV0041GetShares200ResponseSharesSharesInnerSharesNormalized

Normalized shares

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **float** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_shares_shares_inner_shares_normalized import SlurmV0041GetShares200ResponseSharesSharesInnerSharesNormalized

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInnerSharesNormalized from a JSON string
slurm_v0041_get_shares200_response_shares_shares_inner_shares_normalized_instance = SlurmV0041GetShares200ResponseSharesSharesInnerSharesNormalized.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseSharesSharesInnerSharesNormalized.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_shares_shares_inner_shares_normalized_dict = slurm_v0041_get_shares200_response_shares_shares_inner_shares_normalized_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInnerSharesNormalized from a dict
slurm_v0041_get_shares200_response_shares_shares_inner_shares_normalized_from_dict = SlurmV0041GetShares200ResponseSharesSharesInnerSharesNormalized.from_dict(slurm_v0041_get_shares200_response_shares_shares_inner_shares_normalized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


