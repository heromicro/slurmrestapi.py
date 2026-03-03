# V0044UserDefault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos** | **int** | Default QOS | [optional] 
**account** | **str** | Default account | [optional] 
**wckey** | **str** | Default WCKey | [optional] 

## Example

```python
from slurmrestapi.models.v0044_user_default import V0044UserDefault

# TODO update the JSON string below
json = "{}"
# create an instance of V0044UserDefault from a JSON string
v0044_user_default_instance = V0044UserDefault.from_json(json)
# print the JSON string representation of the object
print(V0044UserDefault.to_json())

# convert the object into a dict
v0044_user_default_dict = v0044_user_default_instance.to_dict()
# create an instance of V0044UserDefault from a dict
v0044_user_default_from_dict = V0044UserDefault.from_dict(v0044_user_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


