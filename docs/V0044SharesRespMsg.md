# V0044SharesRespMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**List[V0044AssocSharesObjWrap]**](V0044AssocSharesObjWrap.md) |  | [optional] 
**total_shares** | **int** | Total number of shares | [optional] 

## Example

```python
from slurmrestapi.models.v0044_shares_resp_msg import V0044SharesRespMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0044SharesRespMsg from a JSON string
v0044_shares_resp_msg_instance = V0044SharesRespMsg.from_json(json)
# print the JSON string representation of the object
print(V0044SharesRespMsg.to_json())

# convert the object into a dict
v0044_shares_resp_msg_dict = v0044_shares_resp_msg_instance.to_dict()
# create an instance of V0044SharesRespMsg from a dict
v0044_shares_resp_msg_from_dict = V0044SharesRespMsg.from_dict(v0044_shares_resp_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


