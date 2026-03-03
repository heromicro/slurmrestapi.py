# SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInnerValue

TRES value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_shares_shares_inner_tres_run_seconds_inner_value import SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInnerValue from a JSON string
slurm_v0041_get_shares200_response_shares_shares_inner_tres_run_seconds_inner_value_instance = SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInnerValue.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInnerValue.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_shares_shares_inner_tres_run_seconds_inner_value_dict = slurm_v0041_get_shares200_response_shares_shares_inner_tres_run_seconds_inner_value_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInnerValue from a dict
slurm_v0041_get_shares200_response_shares_shares_inner_tres_run_seconds_inner_value_from_dict = SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInnerValue.from_dict(slurm_v0041_get_shares200_response_shares_shares_inner_tres_run_seconds_inner_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


