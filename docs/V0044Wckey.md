# V0044Wckey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0044Accounting]**](V0044Accounting.md) |  | [optional] 
**cluster** | **str** | Cluster name | 
**id** | **int** | Unique ID for this user-cluster-wckey combination | [optional] 
**name** | **str** | WCKey name | 
**user** | **str** | User name | 
**flags** | **List[str]** | Flags associated with this WCKey | [optional] 

## Example

```python
from slurmrestapi.models.v0044_wckey import V0044Wckey

# TODO update the JSON string below
json = "{}"
# create an instance of V0044Wckey from a JSON string
v0044_wckey_instance = V0044Wckey.from_json(json)
# print the JSON string representation of the object
print(V0044Wckey.to_json())

# convert the object into a dict
v0044_wckey_dict = v0044_wckey_instance.to_dict()
# create an instance of V0044Wckey from a dict
v0044_wckey_from_dict = V0044Wckey.from_dict(v0044_wckey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


