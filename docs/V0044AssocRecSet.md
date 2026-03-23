# V0044AssocRecSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**defaultqos** | **str** | Default QOS | [optional] 
**grpjobs** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**grpjobsaccrue** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**grpsubmitjobs** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**grptres** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**grptresmins** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**grptresrunmins** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**grpwall** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**maxjobs** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**maxjobsaccrue** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**maxsubmitjobs** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**maxtresminsperjob** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**maxtresrunmins** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**maxtresperjob** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**maxtrespernode** | [**List[V0044Tres]**](V0044Tres.md) |  | [optional] 
**maxwalldurationperjob** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**minpriothresh** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**parent** | **str** | Name of parent account | [optional] 
**priority** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**qoslevel** | **List[str]** | List of QOS names | [optional] 
**fairshare** | **int** | Allocated shares used for fairshare calculation | [optional] 

## Example

```python
from slurmrestapi.models.v0044_assoc_rec_set import V0044AssocRecSet

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AssocRecSet from a JSON string
v0044_assoc_rec_set_instance = V0044AssocRecSet.from_json(json)
# print the JSON string representation of the object
print(V0044AssocRecSet.to_json())

# convert the object into a dict
v0044_assoc_rec_set_dict = v0044_assoc_rec_set_instance.to_dict()
# create an instance of V0044AssocRecSet from a dict
v0044_assoc_rec_set_from_dict = V0044AssocRecSet.from_dict(v0044_assoc_rec_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


