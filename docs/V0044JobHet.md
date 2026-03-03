# V0044JobHet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Heterogeneous job ID, if applicable | [optional] 
**job_offset** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_het import V0044JobHet

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobHet from a JSON string
v0044_job_het_instance = V0044JobHet.from_json(json)
# print the JSON string representation of the object
print(V0044JobHet.to_json())

# convert the object into a dict
v0044_job_het_dict = v0044_job_het_instance.to_dict()
# create an instance of V0044JobHet from a dict
v0044_job_het_from_dict = V0044JobHet.from_dict(v0044_job_het_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


