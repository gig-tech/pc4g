# pc4g.UtilitiesApi

All URIs are relative to the base URL of pc4g.Configuration(HOST)

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_csi_driver_examples**](UtilitiesApi.md#download_csi_driver_examples) | **GET** /utilities/csi-driver/examples | 
[**download_kubernetes_configuration_files_example**](UtilitiesApi.md#download_kubernetes_configuration_files_example) | **GET** /utilities/examples/kubernetes-files | 
[**download_terraform_provider_version**](UtilitiesApi.md#download_terraform_provider_version) | **GET** /utilities/terraform-provider/version | 
[**get_cli**](UtilitiesApi.md#get_cli) | **GET** /utilities/cli | 
[**get_latest_cli_version_info**](UtilitiesApi.md#get_latest_cli_version_info) | **GET** /utilities/cli/version | 
[**get_terrafom_provider**](UtilitiesApi.md#get_terrafom_provider) | **GET** /utilities/terraform-provider | 
[**list_cli_platforms**](UtilitiesApi.md#list_cli_platforms) | **GET** /utilities/cli/platforms | 
[**list_terraform_provider_platforms**](UtilitiesApi.md#list_terraform_provider_platforms) | **GET** /utilities/terrafrom-provider/platforms | 


# **download_csi_driver_examples**
> download_csi_driver_examples()



download examples for using the CSI driver

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
api_instance = pc4g.UtilitiesApi(pc4g.ApiClient(configuration))

try:
    api_instance.download_csi_driver_examples()
except ApiException as e:
    print("Exception when calling UtilitiesApi->download_csi_driver_examples: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_kubernetes_configuration_files_example**
> download_kubernetes_configuration_files_example()



download pre-filled examples for kubernetes configuration files

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
api_instance = pc4g.UtilitiesApi(pc4g.ApiClient(configuration))

try:
    api_instance.download_kubernetes_configuration_files_example()
except ApiException as e:
    print("Exception when calling UtilitiesApi->download_kubernetes_configuration_files_example: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_terraform_provider_version**
> VersionInfo download_terraform_provider_version(platform, x_fields=x_fields)



download Terraform provider version

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
api_instance = pc4g.UtilitiesApi(pc4g.ApiClient(configuration))
platform = 'platform_example' # str | platforms available i.e. windows, linux etc.
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.download_terraform_provider_version(platform, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->download_terraform_provider_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| platforms available i.e. windows, linux etc. | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cli**
> str get_cli(platform, version=version)



Get cli

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
api_instance = pc4g.UtilitiesApi(pc4g.ApiClient(configuration))
platform = 'platform_example' # str | specific platform to download binaries for
version = 'version_example' # str | specific version to download (internally used by the cli update mechanism. should not be used otherwise) (optional)

try:
    api_response = api_instance.get_cli(platform, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->get_cli: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| specific platform to download binaries for | 
 **version** | **str**| specific version to download (internally used by the cli update mechanism. should not be used otherwise) | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_cli_version_info**
> VersionInfo get_latest_cli_version_info(platform, x_fields=x_fields)



get latest cli version info

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
api_instance = pc4g.UtilitiesApi(pc4g.ApiClient(configuration))
platform = 'platform_example' # str | platforms available i.e. windows, linux etc.
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_latest_cli_version_info(platform, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->get_latest_cli_version_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| platforms available i.e. windows, linux etc. | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_terrafom_provider**
> str get_terrafom_provider(platform)



Get terraform provider

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
api_instance = pc4g.UtilitiesApi(pc4g.ApiClient(configuration))
platform = 'platform_example' # str | specific platform to download binaries for

try:
    api_response = api_instance.get_terrafom_provider(platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->get_terrafom_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| specific platform to download binaries for | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cli_platforms**
> SupportedPlatforms list_cli_platforms(x_fields=x_fields)



list cli platforms

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
api_instance = pc4g.UtilitiesApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_cli_platforms(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->list_cli_platforms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SupportedPlatforms**](SupportedPlatforms.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_terraform_provider_platforms**
> SupportedPlatforms list_terraform_provider_platforms(x_fields=x_fields)



list terraform provider platforms

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
api_instance = pc4g.UtilitiesApi(pc4g.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_terraform_provider_platforms(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->list_terraform_provider_platforms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SupportedPlatforms**](SupportedPlatforms.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

