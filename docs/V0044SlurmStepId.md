# V0044SlurmStepId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sluid** | **str** | SLUID (Slurm Lexicographically-sortable Unique ID) | [optional] 
**job_id** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**step_het_component** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**step_id** | **str** | Job step ID | [optional] 

## Example

```python
from slurmrestapi.models.v0044_slurm_step_id import V0044SlurmStepId

# TODO update the JSON string below
json = "{}"
# create an instance of V0044SlurmStepId from a JSON string
v0044_slurm_step_id_instance = V0044SlurmStepId.from_json(json)
# print the JSON string representation of the object
print(V0044SlurmStepId.to_json())

# convert the object into a dict
v0044_slurm_step_id_dict = v0044_slurm_step_id_instance.to_dict()
# create an instance of V0044SlurmStepId from a dict
v0044_slurm_step_id_from_dict = V0044SlurmStepId.from_dict(v0044_slurm_step_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


