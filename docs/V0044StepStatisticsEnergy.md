# V0044StepStatisticsEnergy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumed** | [**V0044Uint64NoValStruct**](V0044Uint64NoValStruct.md) |  | [optional] 

## Example

```python
from slurmrestapi.models.v0044_step_statistics_energy import V0044StepStatisticsEnergy

# TODO update the JSON string below
json = "{}"
# create an instance of V0044StepStatisticsEnergy from a JSON string
v0044_step_statistics_energy_instance = V0044StepStatisticsEnergy.from_json(json)
# print the JSON string representation of the object
print(V0044StepStatisticsEnergy.to_json())

# convert the object into a dict
v0044_step_statistics_energy_dict = v0044_step_statistics_energy_instance.to_dict()
# create an instance of V0044StepStatisticsEnergy from a dict
v0044_step_statistics_energy_from_dict = V0044StepStatisticsEnergy.from_dict(v0044_step_statistics_energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


