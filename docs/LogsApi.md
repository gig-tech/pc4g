# pc4g.LogsApi

All URIs are relative to the base URL of pc4g.Configuration(HOST)

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_ui_error**](LogsApi.md#log_ui_error) | **POST** /logs | 


# **log_ui_error**
> log_ui_error(payload)



Log UI Error

### Example
```python
from __future__ import print_function
import time
import pc4g
from pc4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = pc4g.Configuration("https://example.portal.cloud/api/1")
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pc4g.LogsApi(pc4g.ApiClient(configuration))
payload = pc4g.UIErrorLog() # UIErrorLog | 

try:
    api_instance.log_ui_error(payload)
except ApiException as e:
    print("Exception when calling LogsApi->log_ui_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UIErrorLog**](UIErrorLog.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

