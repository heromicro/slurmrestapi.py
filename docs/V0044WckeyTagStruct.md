# V0044WckeyTagStruct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wckey** | **str** | WCKey name | 
**flags** | **List[str]** | Active flags | 

## Example

```python
from slurmrestapi.models.v0044_wckey_tag_struct import V0044WckeyTagStruct

# TODO update the JSON string below
json = "{}"
# create an instance of V0044WckeyTagStruct from a JSON string
v0044_wckey_tag_struct_instance = V0044WckeyTagStruct.from_json(json)
# print the JSON string representation of the object
print(V0044WckeyTagStruct.to_json())

# convert the object into a dict
v0044_wckey_tag_struct_dict = v0044_wckey_tag_struct_instance.to_dict()
# create an instance of V0044WckeyTagStruct from a dict
v0044_wckey_tag_struct_from_dict = V0044WckeyTagStruct.from_dict(v0044_wckey_tag_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


