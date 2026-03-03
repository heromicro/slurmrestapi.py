# SlurmV0041GetShares200ResponseSharesSharesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association ID | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**name** | **str** | Share name | [optional] 
**parent** | **str** | Parent name | [optional] 
**partition** | **str** | Partition name | [optional] 
**shares_normalized** | [**SlurmV0041GetShares200ResponseSharesSharesInnerSharesNormalized**](SlurmV0041GetShares200ResponseSharesSharesInnerSharesNormalized.md) |  | [optional] 
**shares** | [**SlurmV0041GetShares200ResponseSharesSharesInnerShares**](SlurmV0041GetShares200ResponseSharesSharesInnerShares.md) |  | [optional] 
**tres** | [**SlurmV0041GetShares200ResponseSharesSharesInnerTres**](SlurmV0041GetShares200ResponseSharesSharesInnerTres.md) |  | [optional] 
**effective_usage** | **float** | Effective, normalized usage | [optional] 
**usage_normalized** | [**SlurmV0041GetShares200ResponseSharesSharesInnerUsageNormalized**](SlurmV0041GetShares200ResponseSharesSharesInnerUsageNormalized.md) |  | [optional] 
**usage** | **int** | Measure of tresbillableunits usage | [optional] 
**fairshare** | [**SlurmV0041GetShares200ResponseSharesSharesInnerFairshare**](SlurmV0041GetShares200ResponseSharesSharesInnerFairshare.md) |  | [optional] 
**type** | **List[str]** | User or account association | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_get_shares200_response_shares_shares_inner import SlurmV0041GetShares200ResponseSharesSharesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInner from a JSON string
slurm_v0041_get_shares200_response_shares_shares_inner_instance = SlurmV0041GetShares200ResponseSharesSharesInner.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041GetShares200ResponseSharesSharesInner.to_json())

# convert the object into a dict
slurm_v0041_get_shares200_response_shares_shares_inner_dict = slurm_v0041_get_shares200_response_shares_shares_inner_instance.to_dict()
# create an instance of SlurmV0041GetShares200ResponseSharesSharesInner from a dict
slurm_v0041_get_shares200_response_shares_shares_inner_from_dict = SlurmV0041GetShares200ResponseSharesSharesInner.from_dict(slurm_v0041_get_shares200_response_shares_shares_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


