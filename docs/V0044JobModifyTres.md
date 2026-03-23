# V0044JobModifyTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_modify_tres import V0044JobModifyTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobModifyTres from a JSON string
v0044_job_modify_tres_instance = V0044JobModifyTres.from_json(json)
# print the JSON string representation of the object
print(V0044JobModifyTres.to_json())

# convert the object into a dict
v0044_job_modify_tres_dict = v0044_job_modify_tres_instance.to_dict()
# create an instance of V0044JobModifyTres from a dict
v0044_job_modify_tres_from_dict = V0044JobModifyTres.from_dict(v0044_job_modify_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


