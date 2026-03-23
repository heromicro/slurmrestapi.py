# V0041OpenapiSlurmdbdConfigRespInstancesInnerTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_end** | **int** | When the instance will end (UNIX timestamp) | [optional] 
**time_start** | **int** | When the instance will start (UNIX timestamp) | [optional] 

## Example

```python
from slurmrestapi.models.v0041_openapi_slurmdbd_config_resp_instances_inner_time import V0041OpenapiSlurmdbdConfigRespInstancesInnerTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespInstancesInnerTime from a JSON string
v0041_openapi_slurmdbd_config_resp_instances_inner_time_instance = V0041OpenapiSlurmdbdConfigRespInstancesInnerTime.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespInstancesInnerTime.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_instances_inner_time_dict = v0041_openapi_slurmdbd_config_resp_instances_inner_time_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespInstancesInnerTime from a dict
v0041_openapi_slurmdbd_config_resp_instances_inner_time_from_dict = V0041OpenapiSlurmdbdConfigRespInstancesInnerTime.from_dict(v0041_openapi_slurmdbd_config_resp_instances_inner_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


