# V0044JobTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**requested** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_job_tres import V0044JobTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobTres from a JSON string
v0044_job_tres_instance = V0044JobTres.from_json(json)
# print the JSON string representation of the object
print(V0044JobTres.to_json())

# convert the object into a dict
v0044_job_tres_dict = v0044_job_tres_instance.to_dict()
# create an instance of V0044JobTres from a dict
v0044_job_tres_from_dict = V0044JobTres.from_dict(v0044_job_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


