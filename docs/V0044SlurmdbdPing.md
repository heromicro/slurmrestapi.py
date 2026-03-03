# V0044SlurmdbdPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Target for ping | 
**responding** | **bool** | If ping RPC responded with pong from slurmdbd | 
**latency** | **int** | Number of microseconds it took to successfully ping or timeout | 
**primary** | **bool** | Is responding slurmdbd the primary controller (Is responding slurmctld the primary controller) | 

## Example

```python
from slurmrestapi.models.v0044_slurmdbd_ping import V0044SlurmdbdPing

# TODO update the JSON string below
json = "{}"
# create an instance of V0044SlurmdbdPing from a JSON string
v0044_slurmdbd_ping_instance = V0044SlurmdbdPing.from_json(json)
# print the JSON string representation of the object
print(V0044SlurmdbdPing.to_json())

# convert the object into a dict
v0044_slurmdbd_ping_dict = v0044_slurmdbd_ping_instance.to_dict()
# create an instance of V0044SlurmdbdPing from a dict
v0044_slurmdbd_ping_from_dict = V0044SlurmdbdPing.from_dict(v0044_slurmdbd_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


