# SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | TRES type (CPU, MEM, etc) | 
**name** | **str** | TRES name (if applicable) | [optional] 
**id** | **int** | ID used in database | [optional] 
**count** | **int** | TRES count (0 if listed generically) | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner import SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner from a JSON string
slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner_instance = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.to_json())

# convert the object into a dict
slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner_dict = slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner_instance.to_dict()
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner from a dict
slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner_from_dict = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.from_dict(slurmdb_v0041_post_users_association_request_association_condition_association_grptres_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


