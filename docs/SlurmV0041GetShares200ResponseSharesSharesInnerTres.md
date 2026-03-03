# SlurmV0041GetShares200ResponseSharesSharesInnerTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_seconds** | [**List[SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInner]**](SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInner.md) | Currently running tres-secs &#x3D; grp_used_tres_run_secs | [optional] 
**group_minutes** | [**List[SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInner]**](SlurmV0041GetShares200ResponseSharesSharesInnerTresRunSecondsInner.md) | TRES-minute limit | [optional] 
**usage** | [**List[SlurmV0041GetShares200ResponseSharesSharesInnerTresUsageInner]**](SlurmV0041GetShares200ResponseSharesSharesInnerTresUsageInner.md) | Measure of each TRES usage | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_shares_shares_inner_tres import SlurmV0041GetShares200ResponseSharesSharesInnerTres

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInnerTres from a JSON string
slurm_v0041_get_shares200_response_shares_shares_inner_tres_instance = SlurmV0041GetShares200ResponseSharesSharesInnerTres.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseSharesSharesInnerTres.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_shares_shares_inner_tres_dict = slurm_v0041_get_shares200_response_shares_shares_inner_tres_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInnerTres from a dict
slurm_v0041_get_shares200_response_shares_shares_inner_tres_from_dict = SlurmV0041GetShares200ResponseSharesSharesInnerTres.from_dict(slurm_v0041_get_shares200_response_shares_shares_inner_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


