# V0044UserShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminlevel** | **List[str]** | AdminLevel granted to the user | [optional] 
**defaultqos** | **int** | Default QOS | [optional] 
**defaultaccount** | **str** | Default account | [optional] 
**defaultwckey** | **str** | Default WCKey | [optional] 

## Example

```python
from slurmrestapi.models.v0044_user_short import V0044UserShort

# TODO update the JSON string below
json = "{}"
# create an instance of V0044UserShort from a JSON string
v0044_user_short_instance = V0044UserShort.from_json(json)
# print the JSON string representation of the object
print(V0044UserShort.to_json())

# convert the object into a dict
v0044_user_short_dict = v0044_user_short_instance.to_dict()
# create an instance of V0044UserShort from a dict
v0044_user_short_from_dict = V0044UserShort.from_dict(v0044_user_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


