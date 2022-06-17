# pc4g.AdminApi

All URIs are relative to the base URL of pc4g.Configuration(HOST)

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_invoice_payment_status**](AdminApi.md#change_invoice_payment_status) | **PUT** /admin/invoices/{invoice_id}/status | 
[**create_vco_notification**](AdminApi.md#create_vco_notification) | **POST** /admin/email-notifications | 
[**delete_invoice**](AdminApi.md#delete_invoice) | **DELETE** /admin/invoices/{invoice_id} | 
[**delete_vco_notification**](AdminApi.md#delete_vco_notification) | **DELETE** /admin/email-notification/{notification_id} | 
[**delete_vco_to_customer_prices**](AdminApi.md#delete_vco_to_customer_prices) | **DELETE** /admin/prices/{customer_id} | 
[**edit_notification_forwarding**](AdminApi.md#edit_notification_forwarding) | **PUT** /admin/email-notification-forwarding | 
[**generate_invoices**](AdminApi.md#generate_invoices) | **POST** /admin/invoices | 
[**get_acceptable_use_policy**](AdminApi.md#get_acceptable_use_policy) | **GET** /admin/legal/acceptable_use_policy | 
[**get_chat_config**](AdminApi.md#get_chat_config) | **GET** /admin/chat | 
[**get_color_scheme**](AdminApi.md#get_color_scheme) | **GET** /admin/branding/color-scheme | 
[**get_cookie_policy**](AdminApi.md#get_cookie_policy) | **GET** /admin/legal/cookie_policy | 
[**get_demo_user**](AdminApi.md#get_demo_user) | **GET** /admin/demo-user | 
[**get_invoice**](AdminApi.md#get_invoice) | **GET** /admin/invoices/{invoice_id} | 
[**get_invoice_legal_terms**](AdminApi.md#get_invoice_legal_terms) | **GET** /admin/invoices/legal-terms | 
[**get_invoice_numbering_format**](AdminApi.md#get_invoice_numbering_format) | **GET** /admin/invoices/numbering-format | 
[**get_invoice_payment_terms**](AdminApi.md#get_invoice_payment_terms) | **GET** /admin/invoices/payment-terms | 
[**get_invoice_pdf**](AdminApi.md#get_invoice_pdf) | **GET** /admin/invoices/{invoice_id}/pdf | 
[**get_latest_sequence_number**](AdminApi.md#get_latest_sequence_number) | **GET** /admin/invoices/{invoice_id}/sequence-number | 
[**get_legal_documents**](AdminApi.md#get_legal_documents) | **GET** /admin/legal | 
[**get_logo**](AdminApi.md#get_logo) | **GET** /admin/branding/logo | 
[**get_naming**](AdminApi.md#get_naming) | **GET** /admin/naming | 
[**get_notification_forwarding**](AdminApi.md#get_notification_forwarding) | **GET** /admin/email-notification-forwarding | 
[**get_payment_config**](AdminApi.md#get_payment_config) | **GET** /admin/payment-config | 
[**get_privacy_policy**](AdminApi.md#get_privacy_policy) | **GET** /admin/legal/privacy_policy | 
[**get_terms_conditions**](AdminApi.md#get_terms_conditions) | **GET** /admin/legal/terms_and_conditions | 
[**get_v_website**](AdminApi.md#get_v_website) | **GET** /admin/branding/vco-website | 
[**get_vco_buying_prices**](AdminApi.md#get_vco_buying_prices) | **GET** /admin/buying-prices | 
[**get_vco_notification**](AdminApi.md#get_vco_notification) | **GET** /admin/email-notification/{notification_id} | 
[**get_vco_settings**](AdminApi.md#get_vco_settings) | **GET** /admin/settings | 
[**get_vco_timezone**](AdminApi.md#get_vco_timezone) | **GET** /admin/timezone | 
[**get_vco_to_customer_prices**](AdminApi.md#get_vco_to_customer_prices) | **GET** /admin/prices/{customer_id} | 
[**get_vco_to_customer_standard_prices**](AdminApi.md#get_vco_to_customer_standard_prices) | **GET** /admin/prices | 
[**list_invoices**](AdminApi.md#list_invoices) | **GET** /admin/invoices | 
[**list_notification_utilities**](AdminApi.md#list_notification_utilities) | **GET** /admin/email-notification/utilities | 
[**list_vco_notifications**](AdminApi.md#list_vco_notifications) | **GET** /admin/email-notifications | 
[**pay_invoice_with_card**](AdminApi.md#pay_invoice_with_card) | **POST** /admin/invoices/{invoice_id}/pay-with-card | 
[**put_vco_settings**](AdminApi.md#put_vco_settings) | **PUT** /admin/settings | 
[**regenerate_invoice**](AdminApi.md#regenerate_invoice) | **POST** /admin/invoices/{invoice_id} | 
[**send_invoice**](AdminApi.md#send_invoice) | **POST** /admin/invoices/{invoice_id}/send | 
[**send_vco_notification**](AdminApi.md#send_vco_notification) | **PUT** /admin/email-notification/{notification_id}/send | 
[**send_vco_test_notification**](AdminApi.md#send_vco_test_notification) | **PUT** /admin/email-notification/{notification_id}/send-test | 
[**set_chat_config**](AdminApi.md#set_chat_config) | **PUT** /admin/chat | 
[**set_color_scheme**](AdminApi.md#set_color_scheme) | **POST** /admin/branding/color-scheme | 
[**set_demo_user**](AdminApi.md#set_demo_user) | **POST** /admin/demo-user | 
[**set_description**](AdminApi.md#set_description) | **POST** /admin/branding/description | 
[**set_invoice**](AdminApi.md#set_invoice) | **PUT** /admin/invoices/{invoice_id} | 
[**set_legal_documents**](AdminApi.md#set_legal_documents) | **POST** /admin/legal | 
[**set_logo**](AdminApi.md#set_logo) | **POST** /admin/branding/logo | 
[**set_payment_config**](AdminApi.md#set_payment_config) | **PUT** /admin/payment-config | 
[**set_vco_to_customer_prices**](AdminApi.md#set_vco_to_customer_prices) | **PUT** /admin/prices/{customer_id} | 
[**set_vco_to_customer_standard_prices**](AdminApi.md#set_vco_to_customer_standard_prices) | **PUT** /admin/prices | 
[**set_website**](AdminApi.md#set_website) | **PUT** /admin/branding/vco-website | 
[**unset_demo_user**](AdminApi.md#unset_demo_user) | **DELETE** /admin/demo-user | 
[**update_invoice_legal_terms**](AdminApi.md#update_invoice_legal_terms) | **PUT** /admin/invoices/legal-terms | 
[**update_invoice_numbering_format**](AdminApi.md#update_invoice_numbering_format) | **PUT** /admin/invoices/numbering-format | 
[**update_invoice_payment_terms**](AdminApi.md#update_invoice_payment_terms) | **PUT** /admin/invoices/payment-terms | 
[**update_naming**](AdminApi.md#update_naming) | **PUT** /admin/naming | 
[**update_vco_notification**](AdminApi.md#update_vco_notification) | **PUT** /admin/email-notification/{notification_id} | 


# **change_invoice_payment_status**
> change_invoice_payment_status(invoice_id, payment_status)



Change Invoice Payment Status

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
payment_status = 'payment_status_example' # str | Invoice payment status

try:
    api_instance.change_invoice_payment_status(invoice_id, payment_status)
except ApiException as e:
    print("Exception when calling AdminApi->change_invoice_payment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **payment_status** | **str**| Invoice payment status | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vco_notification**
> create_vco_notification(payload)



Create a new email notification

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
payload = pc4g.NotificationConfig() # NotificationConfig | 

try:
    api_instance.create_vco_notification(payload)
except ApiException as e:
    print("Exception when calling AdminApi->create_vco_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**NotificationConfig**](NotificationConfig.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice**
> delete_invoice(invoice_id)



Delete Invoice

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 

try:
    api_instance.delete_invoice(invoice_id)
except ApiException as e:
    print("Exception when calling AdminApi->delete_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vco_notification**
> delete_vco_notification(notification_id)



Delete email notification

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
notification_id = 'notification_id_example' # str | 

try:
    api_instance.delete_vco_notification(notification_id)
except ApiException as e:
    print("Exception when calling AdminApi->delete_vco_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vco_to_customer_prices**
> delete_vco_to_customer_prices(customer_id)



Unset prices set by VCO for a specific customer, fall back to standard prices

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    api_instance.delete_vco_to_customer_prices(customer_id)
except ApiException as e:
    print("Exception when calling AdminApi->delete_vco_to_customer_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_notification_forwarding**
> edit_notification_forwarding(enabled)



Edit email notification forwarding

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
enabled = true # bool | Notifications forwarding status

try:
    api_instance.edit_notification_forwarding(enabled)
except ApiException as e:
    print("Exception when calling AdminApi->edit_notification_forwarding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**| Notifications forwarding status | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_invoices**
> generate_invoices(month)



(Re)generate Invoices

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
month = 56 # int | Month to generate Invoices for in timestamp format UTC epoch of YYYY-MM-01 00:00:00

try:
    api_instance.generate_invoices(month)
except ApiException as e:
    print("Exception when calling AdminApi->generate_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **int**| Month to generate Invoices for in timestamp format UTC epoch of YYYY-MM-01 00:00:00 | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acceptable_use_policy**
> get_acceptable_use_policy()



Get Acceptable Use text file

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))

try:
    api_instance.get_acceptable_use_policy()
except ApiException as e:
    print("Exception when calling AdminApi->get_acceptable_use_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_config**
> ChatConfig get_chat_config(x_fields=x_fields)



Get Chat Configuration

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_chat_config(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_chat_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ChatConfig**](ChatConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_color_scheme**
> ColorScheme get_color_scheme(x_fields=x_fields)



Get the color scheme

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_color_scheme(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_color_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ColorScheme**](ColorScheme.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cookie_policy**
> get_cookie_policy()



Get Cookie Policy text file

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))

try:
    api_instance.get_cookie_policy()
except ApiException as e:
    print("Exception when calling AdminApi->get_cookie_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demo_user**
> MenejaStructsVcoDataclassesDemoUserDemoUserStruct get_demo_user(x_fields=x_fields)



Get Demo User info

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_demo_user(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_demo_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**MenejaStructsVcoDataclassesDemoUserDemoUserStruct**](MenejaStructsVcoDataclassesDemoUserDemoUserStruct.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> InvoiceModel get_invoice(invoice_id, x_fields=x_fields)



Get Invoice

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_invoice(invoice_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**InvoiceModel**](InvoiceModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_legal_terms**
> InvoiceLegalTerms get_invoice_legal_terms(x_fields=x_fields)



Get Legal Terms

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_invoice_legal_terms(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_invoice_legal_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**InvoiceLegalTerms**](InvoiceLegalTerms.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_numbering_format**
> InvoiceNumberingFormat get_invoice_numbering_format(x_fields=x_fields)



Get Numbering Format

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_invoice_numbering_format(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_invoice_numbering_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**InvoiceNumberingFormat**](InvoiceNumberingFormat.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_payment_terms**
> InvoicePaymentTerms get_invoice_payment_terms(x_fields=x_fields)



Get Payment Terms

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_invoice_payment_terms(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_invoice_payment_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**InvoicePaymentTerms**](InvoicePaymentTerms.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_pdf**
> get_invoice_pdf(invoice_id)



Get Invoice PDF

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 

try:
    api_instance.get_invoice_pdf(invoice_id)
except ApiException as e:
    print("Exception when calling AdminApi->get_invoice_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_sequence_number**
> ExpectedSequenceNumber get_latest_sequence_number(invoice_id, x_fields=x_fields)



Get Sequence Number

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_latest_sequence_number(invoice_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_latest_sequence_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ExpectedSequenceNumber**](ExpectedSequenceNumber.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_documents**
> LegalDocumentVersions get_legal_documents(x_fields=x_fields)



Get Legal Documents

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_legal_documents(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_legal_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**LegalDocumentVersions**](LegalDocumentVersions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logo**
> str get_logo()



Get logo

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))

try:
    api_response = api_instance.get_logo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_logo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_naming**
> NamingInfo get_naming(x_fields=x_fields)



Get Naming

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_naming(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_naming: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**NamingInfo**](NamingInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_forwarding**
> MenejaStructsNotificationSubscriptionDataclassesNotificationsForwardingStruct get_notification_forwarding(x_fields=x_fields)



Gets email notification forwarding

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_notification_forwarding(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_notification_forwarding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**MenejaStructsNotificationSubscriptionDataclassesNotificationsForwardingStruct**](MenejaStructsNotificationSubscriptionDataclassesNotificationsForwardingStruct.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_config**
> get_payment_config()



Get Payment Config

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))

try:
    api_instance.get_payment_config()
except ApiException as e:
    print("Exception when calling AdminApi->get_payment_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privacy_policy**
> get_privacy_policy()



Get Privacy Policy text file

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))

try:
    api_instance.get_privacy_policy()
except ApiException as e:
    print("Exception when calling AdminApi->get_privacy_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_terms_conditions**
> get_terms_conditions()



Get Terms and Conditions text file

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))

try:
    api_instance.get_terms_conditions()
except ApiException as e:
    print("Exception when calling AdminApi->get_terms_conditions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v_website**
> str get_v_website()



Get Website

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))

try:
    api_response = api_instance.get_v_website()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_v_website: %s\n" % e)
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

# **get_vco_buying_prices**
> VcoPricing get_vco_buying_prices(x_fields=x_fields)



List VCO buying prices for all locations

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_vco_buying_prices(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_vco_buying_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VcoPricing**](VcoPricing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vco_notification**
> NotificationConfig get_vco_notification(notification_id, x_fields=x_fields)



Get email notification

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
notification_id = 'notification_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_vco_notification(notification_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_vco_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**NotificationConfig**](NotificationConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vco_settings**
> VCOSettings get_vco_settings(x_fields=x_fields)



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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_vco_settings(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_vco_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VCOSettings**](VCOSettings.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vco_timezone**
> MenejaStructsNotificationSubscriptionDataclassesTimezoneStruct get_vco_timezone(x_fields=x_fields)



Get VCO timezone

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_vco_timezone(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_vco_timezone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**MenejaStructsNotificationSubscriptionDataclassesTimezoneStruct**](MenejaStructsNotificationSubscriptionDataclassesTimezoneStruct.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vco_to_customer_prices**
> VcoPricingFlagged get_vco_to_customer_prices(customer_id, x_fields=x_fields)



Get prices set by VCO for a specific customer

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_vco_to_customer_prices(customer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_vco_to_customer_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VcoPricingFlagged**](VcoPricingFlagged.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vco_to_customer_standard_prices**
> VcoPricing get_vco_to_customer_standard_prices(x_fields=x_fields)



Get standard prices set by VCO for the customers

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_vco_to_customer_standard_prices(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_vco_to_customer_standard_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VcoPricing**](VcoPricing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> InvoicesModel list_invoices(customer_id=customer_id, month=month, x_fields=x_fields)



List Invoices

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | Customer ID to filter Invoices on (optional)
month = 56 # int | Month to filter Invoices on in timestamp format UTC epoch of YYYY-MM-01 00:00:00 (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_invoices(customer_id=customer_id, month=month, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer ID to filter Invoices on | [optional] 
 **month** | **int**| Month to filter Invoices on in timestamp format UTC epoch of YYYY-MM-01 00:00:00 | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**InvoicesModel**](InvoicesModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_utilities**
> MenejaStructsNotificationSubscriptionDataclassesNotificationUtilitiesStruct list_notification_utilities(x_fields=x_fields)



List notification utilities

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_notification_utilities(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_notification_utilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**MenejaStructsNotificationSubscriptionDataclassesNotificationUtilitiesStruct**](MenejaStructsNotificationSubscriptionDataclassesNotificationUtilitiesStruct.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vco_notifications**
> list[NotificationConfig] list_vco_notifications(include_past=include_past, notification_type=notification_type, x_fields=x_fields)



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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
include_past = false # bool | include past maintenance notifications (optional) (default to false)
notification_type = 'notification_type_example' # str | notification type (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_vco_notifications(include_past=include_past, notification_type=notification_type, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_vco_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_past** | **bool**| include past maintenance notifications | [optional] [default to false]
 **notification_type** | **str**| notification type | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[NotificationConfig]**](NotificationConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_invoice_with_card**
> pay_invoice_with_card(invoice_id)



Pay Invoice with Card

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 

try:
    api_instance.pay_invoice_with_card(invoice_id)
except ApiException as e:
    print("Exception when calling AdminApi->pay_invoice_with_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_vco_settings**
> put_vco_settings(payload)



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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
payload = pc4g.VCOSettings() # VCOSettings | 

try:
    api_instance.put_vco_settings(payload)
except ApiException as e:
    print("Exception when calling AdminApi->put_vco_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**VCOSettings**](VCOSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_invoice**
> regenerate_invoice(invoice_id)



Regenerate Invoice

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 

try:
    api_instance.regenerate_invoice(invoice_id)
except ApiException as e:
    print("Exception when calling AdminApi->regenerate_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_invoice**
> send_invoice(invoice_id, sequence_number=sequence_number)



(Re)Send VCO Invoice

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
sequence_number = 56 # int | Invoice sequence number (optional)

try:
    api_instance.send_invoice(invoice_id, sequence_number=sequence_number)
except ApiException as e:
    print("Exception when calling AdminApi->send_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **sequence_number** | **int**| Invoice sequence number | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_vco_notification**
> send_vco_notification(notification_id)



Send email notification

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
notification_id = 'notification_id_example' # str | 

try:
    api_instance.send_vco_notification(notification_id)
except ApiException as e:
    print("Exception when calling AdminApi->send_vco_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_vco_test_notification**
> send_vco_test_notification(notification_id, payload)



Send test email notification

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
notification_id = 'notification_id_example' # str | 
payload = pc4g.MenejaStructsNotificationSubscriptionDataclassesTestEmailsStruct() # MenejaStructsNotificationSubscriptionDataclassesTestEmailsStruct | 

try:
    api_instance.send_vco_test_notification(notification_id, payload)
except ApiException as e:
    print("Exception when calling AdminApi->send_vco_test_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
 **payload** | [**MenejaStructsNotificationSubscriptionDataclassesTestEmailsStruct**](MenejaStructsNotificationSubscriptionDataclassesTestEmailsStruct.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_chat_config**
> set_chat_config(enabled)



Set Chat Configuration

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
enabled = true # bool | Enable chat

try:
    api_instance.set_chat_config(enabled)
except ApiException as e:
    print("Exception when calling AdminApi->set_chat_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**| Enable chat | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_color_scheme**
> set_color_scheme(primary=primary, secondary=secondary, accent=accent, error=error, info=info, success=success, warning=warning)



Set color scheme

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
primary = '#1976D2' # str | Primary color (optional) (default to #1976D2)
secondary = '#424242' # str | Secondary color (optional) (default to #424242)
accent = '#82B1FF' # str | Accent color (optional) (default to #82B1FF)
error = '#FF5252' # str | Error color (optional) (default to #FF5252)
info = '#2196F3' # str | Info color (optional) (default to #2196F3)
success = '#4CAF50' # str | Success color (optional) (default to #4CAF50)
warning = '#FFC107' # str | Warning color (optional) (default to #FFC107)

try:
    api_instance.set_color_scheme(primary=primary, secondary=secondary, accent=accent, error=error, info=info, success=success, warning=warning)
except ApiException as e:
    print("Exception when calling AdminApi->set_color_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary** | **str**| Primary color | [optional] [default to #1976D2]
 **secondary** | **str**| Secondary color | [optional] [default to #424242]
 **accent** | **str**| Accent color | [optional] [default to #82B1FF]
 **error** | **str**| Error color | [optional] [default to #FF5252]
 **info** | **str**| Info color | [optional] [default to #2196F3]
 **success** | **str**| Success color | [optional] [default to #4CAF50]
 **warning** | **str**| Warning color | [optional] [default to #FFC107]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_demo_user**
> set_demo_user(payload)



Set Demo User info

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
payload = pc4g.MenejaStructsVcoDataclassesDemoUserDemoUserStruct() # MenejaStructsVcoDataclassesDemoUserDemoUserStruct | 

try:
    api_instance.set_demo_user(payload)
except ApiException as e:
    print("Exception when calling AdminApi->set_demo_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**MenejaStructsVcoDataclassesDemoUserDemoUserStruct**](MenejaStructsVcoDataclassesDemoUserDemoUserStruct.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_description**
> set_description(description)



Set landing portal description

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
description = 'description_example' # str | Intro text in the portal landing page

try:
    api_instance.set_description(description)
except ApiException as e:
    print("Exception when calling AdminApi->set_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| Intro text in the portal landing page | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_invoice**
> set_invoice(invoice_id, pdf, sequence_number, number)



Set custom Invoice

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
pdf = '/path/to/file.txt' # file | PDF to send for this invoice
sequence_number = 56 # int | Invoice sequence number
number = 'number_example' # str | formatted invoice number

try:
    api_instance.set_invoice(invoice_id, pdf, sequence_number, number)
except ApiException as e:
    print("Exception when calling AdminApi->set_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **pdf** | **file**| PDF to send for this invoice | 
 **sequence_number** | **int**| Invoice sequence number | 
 **number** | **str**| formatted invoice number | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_legal_documents**
> set_legal_documents()



Set Legal Documents

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))

try:
    api_instance.set_legal_documents()
except ApiException as e:
    print("Exception when calling AdminApi->set_legal_documents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_logo**
> set_logo(logo)



Set logo

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
logo = 'logo_example' # str | Base64 of the branding logo

try:
    api_instance.set_logo(logo)
except ApiException as e:
    print("Exception when calling AdminApi->set_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logo** | **str**| Base64 of the branding logo | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_payment_config**
> set_payment_config(payment_gateway)



Set Payment Config

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
payment_gateway = 'payment_gateway_example' # str | 

try:
    api_instance.set_payment_config(payment_gateway)
except ApiException as e:
    print("Exception when calling AdminApi->set_payment_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_gateway** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_vco_to_customer_prices**
> set_vco_to_customer_prices(customer_id, payload)



Set prices set by VCO for a specific customer

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
payload = pc4g.VcoPricing() # VcoPricing | 

try:
    api_instance.set_vco_to_customer_prices(customer_id, payload)
except ApiException as e:
    print("Exception when calling AdminApi->set_vco_to_customer_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **payload** | [**VcoPricing**](VcoPricing.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_vco_to_customer_standard_prices**
> set_vco_to_customer_standard_prices(payload)



Set standard prices set by VCO to the customers

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
payload = pc4g.VcoPricing() # VcoPricing | 

try:
    api_instance.set_vco_to_customer_standard_prices(payload)
except ApiException as e:
    print("Exception when calling AdminApi->set_vco_to_customer_standard_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**VcoPricing**](VcoPricing.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_website**
> set_website(vco_website)



Set Website

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
vco_website = 'vco_website_example' # str | Website

try:
    api_instance.set_website(vco_website)
except ApiException as e:
    print("Exception when calling AdminApi->set_website: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vco_website** | **str**| Website | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_demo_user**
> unset_demo_user()



Unset Demo user

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))

try:
    api_instance.unset_demo_user()
except ApiException as e:
    print("Exception when calling AdminApi->unset_demo_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_legal_terms**
> update_invoice_legal_terms(payload)



Update Legal Terms

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
payload = pc4g.InvoiceLegalTerms() # InvoiceLegalTerms | 

try:
    api_instance.update_invoice_legal_terms(payload)
except ApiException as e:
    print("Exception when calling AdminApi->update_invoice_legal_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**InvoiceLegalTerms**](InvoiceLegalTerms.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_numbering_format**
> update_invoice_numbering_format(numbering_format)



Update Numbering Format

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
numbering_format = 'numbering_format_example' # str | Invoice numbering format

try:
    api_instance.update_invoice_numbering_format(numbering_format)
except ApiException as e:
    print("Exception when calling AdminApi->update_invoice_numbering_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numbering_format** | **str**| Invoice numbering format | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_payment_terms**
> update_invoice_payment_terms(payload)



Update Payment Terms

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
payload = pc4g.InvoicePaymentTerms() # InvoicePaymentTerms | 

try:
    api_instance.update_invoice_payment_terms(payload)
except ApiException as e:
    print("Exception when calling AdminApi->update_invoice_payment_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**InvoicePaymentTerms**](InvoicePaymentTerms.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_naming**
> update_naming(name=name, utility_name=utility_name)



Update Naming

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
name = 'name_example' # str | name (optional)
utility_name = 'utility_name_example' # str | utility name (optional)

try:
    api_instance.update_naming(name=name, utility_name=utility_name)
except ApiException as e:
    print("Exception when calling AdminApi->update_naming: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | [optional] 
 **utility_name** | **str**| utility name | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vco_notification**
> update_vco_notification(notification_id, payload)



Update email notification

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
api_instance = pc4g.AdminApi(pc4g.ApiClient(configuration))
notification_id = 'notification_id_example' # str | 
payload = pc4g.NotificationConfig() # NotificationConfig | 

try:
    api_instance.update_vco_notification(notification_id, payload)
except ApiException as e:
    print("Exception when calling AdminApi->update_vco_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
 **payload** | [**NotificationConfig**](NotificationConfig.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

