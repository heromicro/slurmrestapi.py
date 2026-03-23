# V0044JobResCore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Core index | 
**status** | **List[str]** | Core status | 

## Example

```python
from slurmrestapi.models.v0044_job_res_core import V0044JobResCore

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobResCore from a JSON string
v0044_job_res_core_instance = V0044JobResCore.from_json(json)
# print the JSON string representation of the object
print(V0044JobResCore.to_json())

# convert the object into a dict
v0044_job_res_core_dict = v0044_job_res_core_instance.to_dict()
# create an instance of V0044JobResCore from a dict
v0044_job_res_core_from_dict = V0044JobResCore.from_dict(v0044_job_res_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


