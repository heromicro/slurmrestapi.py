# SlurmV0041PostJobSubmitRequestJobsInnerRlimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsCpu**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsCpu.md) |  | [optional] 
**fsize** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsFsize**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsFsize.md) |  | [optional] 
**data** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsData**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsData.md) |  | [optional] 
**stack** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsStack**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsStack.md) |  | [optional] 
**core** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsCore**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsCore.md) |  | [optional] 
**rss** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsRss**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsRss.md) |  | [optional] 
**nproc** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsNproc**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsNproc.md) |  | [optional] 
**nofile** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsNofile**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsNofile.md) |  | [optional] 
**memlock** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsMemlock**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsMemlock.md) |  | [optional] 
**var_as** | [**SlurmV0041PostJobSubmitRequestJobsInnerRlimitsAs**](SlurmV0041PostJobSubmitRequestJobsInnerRlimitsAs.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.slurm_v0041_post_job_submit_request_jobs_inner_rlimits import SlurmV0041PostJobSubmitRequestJobsInnerRlimits

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerRlimits from a JSON string
slurm_v0041_post_job_submit_request_jobs_inner_rlimits_instance = SlurmV0041PostJobSubmitRequestJobsInnerRlimits.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostJobSubmitRequestJobsInnerRlimits.to_json())

# convert the object into a dict
slurm_v0041_post_job_submit_request_jobs_inner_rlimits_dict = slurm_v0041_post_job_submit_request_jobs_inner_rlimits_instance.to_dict()
# create an instance of SlurmV0041PostJobSubmitRequestJobsInnerRlimits from a dict
slurm_v0041_post_job_submit_request_jobs_inner_rlimits_from_dict = SlurmV0041PostJobSubmitRequestJobsInnerRlimits.from_dict(slurm_v0041_post_job_submit_request_jobs_inner_rlimits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


