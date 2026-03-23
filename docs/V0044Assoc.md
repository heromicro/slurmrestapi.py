# V0044Assoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting** | [**List[V0044Accounting]**](V0044Accounting.md) |  | [optional] 
**account** | **str** | Account name | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**comment** | **str** | Arbitrary comment | [optional] 
**default** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerDefault**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerDefault.md) |  | [optional] 
**flags** | **List[str]** | Flags on the association | [optional] 
**max** | [**V0044AssocMax**](V0044AssocMax.md) |  | [optional] 
**id** | **int** | Unique ID (Association ID) | [optional] 
**is_default** | **bool** | Is default association for user | [optional] 
**lineage** | **str** | Complete path up the hierarchy to the root association | [optional] 
**min** | [**V0044AssocMin**](V0044AssocMin.md) |  | [optional] 
**parent_account** | **str** | Name of parent account | [optional] 
**partition** | **str** | Partition name | [optional] 
**priority** | [**V0044Uint32NoValStruct**](V0044Uint32NoValStruct.md) |  | [optional] 
**qos** | **List[str]** | List of QOS names | [optional] 
**shares_raw** | **int** | Allocated shares used for fairshare calculation | [optional] 
**user** | **str** | User name | 

## Example

```python
from slurmrestapi.models.v0044_assoc import V0044Assoc

# TODO update the JSON string below
json = "{}"
# create an instance of V0044Assoc from a JSON string
v0044_assoc_instance = V0044Assoc.from_json(json)
# print the JSON string representation of the object
print(V0044Assoc.to_json())

# convert the object into a dict
v0044_assoc_dict = v0044_assoc_instance.to_dict()
# create an instance of V0044Assoc from a dict
v0044_assoc_from_dict = V0044Assoc.from_dict(v0044_assoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


