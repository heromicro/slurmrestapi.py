# V0044OpenapiSlurmdbdQosResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos** | [**List[V0044Qos]**](V0044Qos.md) |  | 
**meta** | [**V0044OpenapiMeta**](V0044OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0044OpenapiError]**](V0044OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0044OpenapiWarning]**](V0044OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_openapi_slurmdbd_qos_resp import V0044OpenapiSlurmdbdQosResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0044OpenapiSlurmdbdQosResp from a JSON string
v0044_openapi_slurmdbd_qos_resp_instance = V0044OpenapiSlurmdbdQosResp.from_json(json)
# print the JSON string representation of the object
print(V0044OpenapiSlurmdbdQosResp.to_json())

# convert the object into a dict
v0044_openapi_slurmdbd_qos_resp_dict = v0044_openapi_slurmdbd_qos_resp_instance.to_dict()
# create an instance of V0044OpenapiSlurmdbdQosResp from a dict
v0044_openapi_slurmdbd_qos_resp_from_dict = V0044OpenapiSlurmdbdQosResp.from_dict(v0044_openapi_slurmdbd_qos_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


