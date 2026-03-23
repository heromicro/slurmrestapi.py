# V0044AssocMax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**V0044AssocMaxJobs**](V0044AssocMaxJobs.md) |  | [optional] 
**tres** | [**V0044AssocMaxTres**](V0044AssocMaxTres.md) |  | [optional] 
**per** | [**V0044AssocMaxPer**](V0044AssocMaxPer.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_assoc_max import V0044AssocMax

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AssocMax from a JSON string
v0044_assoc_max_instance = V0044AssocMax.from_json(json)
# print the JSON string representation of the object
print(V0044AssocMax.to_json())

# convert the object into a dict
v0044_assoc_max_dict = v0044_assoc_max_instance.to_dict()
# create an instance of V0044AssocMax from a dict
v0044_assoc_max_from_dict = V0044AssocMax.from_dict(v0044_assoc_max_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


