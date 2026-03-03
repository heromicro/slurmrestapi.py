# SlurmV0041GetShares200ResponseShares

fairshare info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**List[SlurmV0041GetShares200ResponseSharesSharesInner]**](SlurmV0041GetShares200ResponseSharesSharesInner.md) | Association shares | [optional] 
**total_shares** | **int** | Total number of shares | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_shares import SlurmV0041GetShares200ResponseShares

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseShares from a JSON string
slurm_v0041_get_shares200_response_shares_instance = SlurmV0041GetShares200ResponseShares.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseShares.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_shares_dict = slurm_v0041_get_shares200_response_shares_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseShares from a dict
slurm_v0041_get_shares200_response_shares_from_dict = SlurmV0041GetShares200ResponseShares.from_dict(slurm_v0041_get_shares200_response_shares_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


