# V0044AssocSharesObjWrap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Association ID | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**name** | **str** | Share name | [optional] 
**parent** | **str** | Parent name | [optional] 
**partition** | **str** | Partition name | [optional] 
**shares_normalized** | [**V0044Float64NoValStruct**](V0044Float64NoValStruct.md) |  | [optional] 
**shares** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**tres** | [**V0044AssocSharesObjWrapTres**](V0044AssocSharesObjWrapTres.md) |  | [optional] 
**effective_usage** | [**V0044Float64NoValStruct**](V0044Float64NoValStruct.md) |  | [optional] 
**usage_normalized** | [**V0044Float64NoValStruct**](V0044Float64NoValStruct.md) |  | [optional] 
**usage** | **int** | Measure of tresbillableunits usage | [optional] 
**fairshare** | [**V0044AssocSharesObjWrapFairshare**](V0044AssocSharesObjWrapFairshare.md) |  | [optional] 
**type** | **List[str]** | User or account association | [optional] 

## Example

```python
from slurmrestapi.models.v0044_assoc_shares_obj_wrap import V0044AssocSharesObjWrap

# TODO update the JSON string below
json = "{}"
# create an instance of V0044AssocSharesObjWrap from a JSON string
v0044_assoc_shares_obj_wrap_instance = V0044AssocSharesObjWrap.from_json(json)
# print the JSON string representation of the object
print(V0044AssocSharesObjWrap.to_json())

# convert the object into a dict
v0044_assoc_shares_obj_wrap_dict = v0044_assoc_shares_obj_wrap_instance.to_dict()
# create an instance of V0044AssocSharesObjWrap from a dict
v0044_assoc_shares_obj_wrap_from_dict = V0044AssocSharesObjWrap.from_dict(v0044_assoc_shares_obj_wrap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


