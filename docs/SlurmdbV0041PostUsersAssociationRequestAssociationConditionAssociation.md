# SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation

Association limits and options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**defaultqos** | **str** | Default QOS | [optional] 
**grpjobs** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobs**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobs.md) |  | [optional] 
**grpjobsaccrue** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobsaccrue**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpjobsaccrue.md) |  | [optional] 
**grpsubmitjobs** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpsubmitjobs**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpsubmitjobs.md) |  | [optional] 
**grptres** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES able to be allocated by running jobs in this association and its children | [optional] 
**grptresmins** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Total number of TRES minutes that can possibly be used by past, present and future jobs in this association and its children | [optional] 
**grptresrunmins** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES minutes able to be allocated by running jobs in this association and its children | [optional] 
**grpwall** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpwall**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrpwall.md) |  | [optional] 
**maxjobs** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxjobs**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxjobs.md) |  | [optional] 
**maxjobsaccrue** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxjobsaccrue**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxjobsaccrue.md) |  | [optional] 
**maxsubmitjobs** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxsubmitjobs**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxsubmitjobs.md) |  | [optional] 
**maxtresminsperjob** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES minutes each job is able to use in this association | [optional] 
**maxtresrunmins** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES minutes able to be allocated by running jobs in this association | [optional] 
**maxtresperjob** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES each job is able to use in this association | [optional] 
**maxtrespernode** | [**List[SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner]**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES each node is able to use | [optional] 
**maxwalldurationperjob** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxwalldurationperjob**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMaxwalldurationperjob.md) |  | [optional] 
**minpriothresh** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationMinpriothresh.md) |  | [optional] 
**parent** | **str** | Name of parent account | [optional] 
**priority** | [**SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationPriority**](SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociationPriority.md) |  | [optional] 
**qoslevel** | **List[str]** | List of available QOS names | [optional] 
**fairshare** | **int** | Allocated shares used for fairshare calculation | [optional] 

## Example

```python
from slurmrestapi.models.slurmdb_v0041_post_users_association_request_association_condition_association import SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation from a JSON string
slurmdb_v0041_post_users_association_request_association_condition_association_instance = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation.from_json(json)
# print the JSON string representation of the object
print(SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation.to_json())

# convert the object into a dict
slurmdb_v0041_post_users_association_request_association_condition_association_dict = slurmdb_v0041_post_users_association_request_association_condition_association_instance.to_dict()
# create an instance of SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation from a dict
slurmdb_v0041_post_users_association_request_association_condition_association_from_dict = SlurmdbV0041PostUsersAssociationRequestAssociationConditionAssociation.from_dict(slurmdb_v0041_post_users_association_request_association_condition_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


