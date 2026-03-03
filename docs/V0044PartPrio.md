# V0044PartPrio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | **str** | Partition name | [optional] 
**priority** | **int** | Prospective job priority if it runs in this partition | [optional] 

## Example

```python
from slurmrestapi.models.v0044_part_prio import V0044PartPrio

# TODO update the JSON string below
json = "{}"
# create an instance of V0044PartPrio from a JSON string
v0044_part_prio_instance = V0044PartPrio.from_json(json)
# print the JSON string representation of the object
print(V0044PartPrio.to_json())

# convert the object into a dict
v0044_part_prio_dict = v0044_part_prio_instance.to_dict()
# create an instance of V0044PartPrio from a dict
v0044_part_prio_from_dict = V0044PartPrio.from_dict(v0044_part_prio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


