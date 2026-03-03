# V0042PartitionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**V0041OpenapiPartitionRespPartitionsInnerNodes**](V0041OpenapiPartitionRespPartitionsInnerNodes.md) |  | [optional] 
**accounts** | [**V0041OpenapiPartitionRespPartitionsInnerAccounts**](V0041OpenapiPartitionRespPartitionsInnerAccounts.md) |  | [optional] 
**groups** | [**V0041OpenapiPartitionRespPartitionsInnerGroups**](V0041OpenapiPartitionRespPartitionsInnerGroups.md) |  | [optional] 
**qos** | [**V0041OpenapiPartitionRespPartitionsInnerQos**](V0041OpenapiPartitionRespPartitionsInnerQos.md) |  | [optional] 
**alternate** | **str** | Alternate | [optional] 
**tres** | [**V0041OpenapiPartitionRespPartitionsInnerTres**](V0041OpenapiPartitionRespPartitionsInnerTres.md) |  | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**select_type** | **List[str]** |  | [optional] 
**cpus** | [**V0041OpenapiPartitionRespPartitionsInnerCpus**](V0041OpenapiPartitionRespPartitionsInnerCpus.md) |  | [optional] 
**defaults** | [**V0042PartitionInfoDefaults**](V0042PartitionInfoDefaults.md) |  | [optional] 
**grace_time** | **int** | GraceTime | [optional] 
**maximums** | [**V0042PartitionInfoMaximums**](V0042PartitionInfoMaximums.md) |  | [optional] 
**minimums** | [**V0041OpenapiPartitionRespPartitionsInnerMinimums**](V0041OpenapiPartitionRespPartitionsInnerMinimums.md) |  | [optional] 
**name** | **str** | PartitionName | [optional] 
**node_sets** | **str** | NodeSets | [optional] 
**priority** | [**V0041OpenapiPartitionRespPartitionsInnerPriority**](V0041OpenapiPartitionRespPartitionsInnerPriority.md) |  | [optional] 
**timeouts** | [**V0042PartitionInfoTimeouts**](V0042PartitionInfoTimeouts.md) |  | [optional] 
**partition** | [**V0042PartitionInfoPartition**](V0042PartitionInfoPartition.md) |  | [optional] 
**suspend_time** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0042_partition_info import V0042PartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0042PartitionInfo from a JSON string
v0042_partition_info_instance = V0042PartitionInfo.from_json(json)
# print the JSON string representation of the object
print(V0042PartitionInfo.to_json())

# convert the object into a dict
v0042_partition_info_dict = v0042_partition_info_instance.to_dict()
# create an instance of V0042PartitionInfo from a dict
v0042_partition_info_from_dict = V0042PartitionInfo.from_dict(v0042_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


