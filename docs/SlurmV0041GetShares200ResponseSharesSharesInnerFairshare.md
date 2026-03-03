# SlurmV0041GetShares200ResponseSharesSharesInnerFairshare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor** | **float** | Fairshare factor | [optional] 
**level** | **float** | Fairshare factor at this level; stored on an assoc as a long double, but that is not needed for display in sshare | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_shares_shares_inner_fairshare import SlurmV0041GetShares200ResponseSharesSharesInnerFairshare

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInnerFairshare from a JSON string
slurm_v0041_get_shares200_response_shares_shares_inner_fairshare_instance = SlurmV0041GetShares200ResponseSharesSharesInnerFairshare.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseSharesSharesInnerFairshare.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_shares_shares_inner_fairshare_dict = slurm_v0041_get_shares200_response_shares_shares_inner_fairshare_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInnerFairshare from a dict
slurm_v0041_get_shares200_response_shares_shares_inner_fairshare_from_dict = SlurmV0041GetShares200ResponseSharesSharesInnerFairshare.from_dict(slurm_v0041_get_shares200_response_shares_shares_inner_fairshare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


