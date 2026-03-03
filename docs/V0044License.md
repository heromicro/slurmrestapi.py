# V0044License


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_name** | **str** | Name of the license | [optional] 
**total** | **int** | Total number of licenses present | [optional] 
**used** | **int** | Number of licenses in use | [optional] 
**free** | **int** | Number of licenses currently available | [optional] 
**remote** | **bool** | Indicates whether licenses are served by the database | [optional] 
**reserved** | **int** | Number of licenses reserved | [optional] 
**last_consumed** | **int** | Last known number of licenses that were consumed in the license manager (Remote Only) | [optional] 
**last_deficit** | **int** | Number of \&quot;missing licenses\&quot; from the cluster&#39;s perspective | [optional] 
**last_update** | **int** | When the license information was last updated (UNIX Timestamp) (UNIX timestamp or time string recognized by Slurm (e.g., &#39;[MM/DD[/YY]-]HH:MM[:SS]&#39;)) | [optional] 
**nodes** | **str** | HRes nodes | [optional] 

## Example

```python
from slurmrestapi.models.v0044_license import V0044License

# TODO update the JSON string below
json = "{}"
# create an instance of V0044License from a JSON string
v0044_license_instance = V0044License.from_json(json)
# print the JSON string representation of the object
print(V0044License.to_json())

# convert the object into a dict
v0044_license_dict = v0044_license_instance.to_dict()
# create an instance of V0044License from a dict
v0044_license_from_dict = V0044License.from_dict(v0044_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


