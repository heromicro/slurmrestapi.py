# V0044Accounting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**V0044AccountingAllocated**](V0044AccountingAllocated.md) |  | [optional] 
**id** | **int** | Association ID or Workload characterization key ID | [optional] 
**id_alt** | **int** | Alternate ID (not currently used) | [optional] 
**start** | **int** | When the record was started (UNIX timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**tres** | [**V0044Tres**](V0044Tres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_accounting import V0044Accounting

# TODO update the JSON string below
json = "{}"
# create an instance of V0044Accounting from a JSON string
v0044_accounting_instance = V0044Accounting.from_json(json)
# print the JSON string representation of the object
print(V0044Accounting.to_json())

# convert the object into a dict
v0044_accounting_dict = v0044_accounting_instance.to_dict()
# create an instance of V0044Accounting from a dict
v0044_accounting_from_dict = V0044Accounting.from_dict(v0044_accounting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


