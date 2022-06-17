# pc4g.MeApi

All URIs are relative to the base URL of pc4g.Configuration(HOST)

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user_info**](MeApi.md#get_current_user_info) | **GET** /me | 
[**get_current_user_jwt**](MeApi.md#get_current_user_jwt) | **GET** /me/jwt | 
[**get_email_subscriptions**](MeApi.md#get_email_subscriptions) | **GET** /me/email-subscriptions | 
[**get_new_email_subscriptions**](MeApi.md#get_new_email_subscriptions) | **GET** /me/new-email-subscriptions | 
[**list_user_notifications**](MeApi.md#list_user_notifications) | **GET** /me/email-notifications | 
[**update_email_subscription**](MeApi.md#update_email_subscription) | **PUT** /me/email-subscriptions | 


# **get_current_user_info**
> User get_current_user_info(x_fields=x_fields)



Gets current user info

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
api_instance = pc4g.MeApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_current_user_info(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_current_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_jwt**
> str get_current_user_jwt()



Gets current user JWT token

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
api_instance = pc4g.MeApi(pc4g.ApiClient(configuration))

try:
    api_response = api_instance.get_current_user_jwt()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_current_user_jwt: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_subscriptions**
> UserEmailSubscriptionConfigEmailPreferences get_email_subscriptions(x_fields=x_fields)



Gets Email Subscriptions

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
api_instance = pc4g.MeApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_email_subscriptions(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_email_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**UserEmailSubscriptionConfigEmailPreferences**](UserEmailSubscriptionConfigEmailPreferences.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_email_subscriptions**
> UserEmailSubscriptionConfigEmailPreferences get_new_email_subscriptions(x_fields=x_fields)



Gets new email subscriptions

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
api_instance = pc4g.MeApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_new_email_subscriptions(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_new_email_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**UserEmailSubscriptionConfigEmailPreferences**](UserEmailSubscriptionConfigEmailPreferences.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_notifications**
> list[NotificationConfig] list_user_notifications(include_past=include_past, notification_type=notification_type, status=status, x_fields=x_fields)



get email notifications

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
api_instance = pc4g.MeApi(pc4g.ApiClient(configuration))
include_past = false # bool | include past maintenance notifications (optional) (default to false)
notification_type = 'notification_type_example' # str | notification type (optional)
status = 'status_example' # str | notification status (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_user_notifications(include_past=include_past, notification_type=notification_type, status=status, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->list_user_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_past** | **bool**| include past maintenance notifications | [optional] [default to false]
 **notification_type** | **str**| notification type | [optional] 
 **status** | **str**| notification status | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[NotificationConfig]**](NotificationConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_subscription**
> update_email_subscription(payload)



update Email Subscription

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
api_instance = pc4g.MeApi(pc4g.ApiClient(configuration))
payload = pc4g.UserEmailSubscriptionConfigEmailPreferences() # UserEmailSubscriptionConfigEmailPreferences | 

try:
    api_instance.update_email_subscription(payload)
except ApiException as e:
    print("Exception when calling MeApi->update_email_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UserEmailSubscriptionConfigEmailPreferences**](UserEmailSubscriptionConfigEmailPreferences.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

