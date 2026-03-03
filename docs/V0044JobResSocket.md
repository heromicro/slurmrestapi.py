# V0044JobResSocket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Core index | 
**cores** | [**List[V0044JobResCore]**](V0044JobResCore.md) |  | 

## Example

```python
from slurmrestapi.models.v0044_job_res_socket import V0044JobResSocket

# TODO update the JSON string below
json = "{}"
# create an instance of V0044JobResSocket from a JSON string
v0044_job_res_socket_instance = V0044JobResSocket.from_json(json)
# print the JSON string representation of the object
print(V0044JobResSocket.to_json())

# convert the object into a dict
v0044_job_res_socket_dict = v0044_job_res_socket_instance.to_dict()
# create an instance of V0044JobResSocket from a dict
v0044_job_res_socket_from_dict = V0044JobResSocket.from_dict(v0044_job_res_socket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


