# pc4g.AlphaApi

All URIs are relative to the base URL of pc4g.Configuration(HOST)

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_card**](AlphaApi.md#add_customer_card) | **POST** /alpha/customer/{customer_id}/cards | 
[**add_host_to_server_pool**](AlphaApi.md#add_host_to_server_pool) | **POST** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/server-pools/{serverpool_id}/hosts | 
[**create_cloudspaces_server_pool**](AlphaApi.md#create_cloudspaces_server_pool) | **POST** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/server-pools | 
[**create_load_balancer**](AlphaApi.md#create_load_balancer) | **POST** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/load-balancers | 
[**create_reverse_proxy**](AlphaApi.md#create_reverse_proxy) | **POST** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/reverse-proxies | 
[**delete_customer_card**](AlphaApi.md#delete_customer_card) | **DELETE** /alpha/customer/{customer_id}/cards/{card_id} | 
[**delete_load_balancer**](AlphaApi.md#delete_load_balancer) | **DELETE** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/load-balancers/{loadbalancer_id} | 
[**delete_reverse_proxy**](AlphaApi.md#delete_reverse_proxy) | **DELETE** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/reverse-proxies/{reverseproxy_id} | 
[**delete_server_pool**](AlphaApi.md#delete_server_pool) | **DELETE** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/server-pools/{serverpool_id} | 
[**generate_traefik_config**](AlphaApi.md#generate_traefik_config) | **GET** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/traefik | 
[**get_customer_card**](AlphaApi.md#get_customer_card) | **GET** /alpha/customer/{customer_id}/cards/{card_id} | 
[**get_reverse_proxy_info**](AlphaApi.md#get_reverse_proxy_info) | **GET** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/reverse-proxies/{reverseproxy_id} | 
[**get_server_pool_info**](AlphaApi.md#get_server_pool_info) | **GET** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/server-pools/{serverpool_id} | 
[**list_cloudspaces_reverse_proxies**](AlphaApi.md#list_cloudspaces_reverse_proxies) | **GET** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/reverse-proxies | 
[**list_cloudspaces_server_pools**](AlphaApi.md#list_cloudspaces_server_pools) | **GET** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/server-pools | 
[**list_customer_cards**](AlphaApi.md#list_customer_cards) | **GET** /alpha/customer/{customer_id}/cards | 
[**list_load_balancers**](AlphaApi.md#list_load_balancers) | **GET** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/load-balancers | 
[**list_server_pool_hosts**](AlphaApi.md#list_server_pool_hosts) | **GET** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/server-pools/{serverpool_id}/hosts | 
[**remove_host_from_server_pool**](AlphaApi.md#remove_host_from_server_pool) | **DELETE** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/server-pools/{serverpool_id}/hosts/{host_id} | 
[**renew_certificate**](AlphaApi.md#renew_certificate) | **POST** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/reverse-proxies/{reverseproxy_id}/renew-certificate | 
[**set_customer_card_as_default**](AlphaApi.md#set_customer_card_as_default) | **PUT** /alpha/customer/{customer_id}/cards/{card_id} | 
[**show_load_balancer_info**](AlphaApi.md#show_load_balancer_info) | **GET** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/load-balancers/{loadbalancer_id} | 
[**update_load_balancer_info**](AlphaApi.md#update_load_balancer_info) | **PUT** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/load-balancers/{loadbalancer_id} | 
[**update_reverse_proxy_info**](AlphaApi.md#update_reverse_proxy_info) | **PUT** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/reverse-proxies/{reverseproxy_id} | 
[**update_server_pool_info**](AlphaApi.md#update_server_pool_info) | **PUT** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/server-pools/{serverpool_id} | 
[**update_traefik_config**](AlphaApi.md#update_traefik_config) | **PUT** /alpha/customers/{customer_id}/cloudspaces/{cloudspace_id}/ingress/traefik | 


# **add_customer_card**
> add_customer_card(customer_id)



Add customer Card

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    api_instance.add_customer_card(customer_id)
except ApiException as e:
    print("Exception when calling AlphaApi->add_customer_card: %s\n" % e)
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

# **add_host_to_server_pool**
> ServerPoolHost add_host_to_server_pool(customer_id, cloudspace_id, serverpool_id, address, x_fields=x_fields)



Add host to server pool

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
serverpool_id = 'serverpool_id_example' # str | 
address = 'address_example' # str | IPv4 address, IPv6 address or domain name of the host
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.add_host_to_server_pool(customer_id, cloudspace_id, serverpool_id, address, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->add_host_to_server_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **serverpool_id** | **str**|  | 
 **address** | **str**| IPv4 address, IPv6 address or domain name of the host | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ServerPoolHost**](ServerPoolHost.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloudspaces_server_pool**
> IDModel create_cloudspaces_server_pool(customer_id, cloudspace_id, name, description=description, x_fields=x_fields)



create new server pool

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
name = 'name_example' # str | Name of the server pool
description = 'description_example' # str | Description of the server pool (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_cloudspaces_server_pool(customer_id, cloudspace_id, name, description=description, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->create_cloudspaces_server_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **name** | **str**| Name of the server pool | 
 **description** | **str**| Description of the server pool | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**IDModel**](IDModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_load_balancer**
> IDModel create_load_balancer(customer_id, cloudspace_id, payload, x_fields=x_fields)



create new load balancer

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
payload = pc4g.CreateLoadBalancerFull() # CreateLoadBalancerFull | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_load_balancer(customer_id, cloudspace_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->create_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **payload** | [**CreateLoadBalancerFull**](CreateLoadBalancerFull.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**IDModel**](IDModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reverse_proxy**
> IDModel create_reverse_proxy(customer_id, cloudspace_id, payload, x_fields=x_fields)



create new reverse proxy

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
payload = pc4g.CreateReverseProxyFull() # CreateReverseProxyFull | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.create_reverse_proxy(customer_id, cloudspace_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->create_reverse_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **payload** | [**CreateReverseProxyFull**](CreateReverseProxyFull.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**IDModel**](IDModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_card**
> delete_customer_card(customer_id, card_id)



Delete customer Card

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
card_id = 'card_id_example' # str | 

try:
    api_instance.delete_customer_card(customer_id, card_id)
except ApiException as e:
    print("Exception when calling AlphaApi->delete_customer_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **card_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_balancer**
> SuccessModel delete_load_balancer(customer_id, cloudspace_id, loadbalancer_id, x_fields=x_fields)



Delete load balancer

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
loadbalancer_id = 'loadbalancer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_load_balancer(customer_id, cloudspace_id, loadbalancer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->delete_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **loadbalancer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reverse_proxy**
> SuccessModel delete_reverse_proxy(customer_id, cloudspace_id, reverseproxy_id, x_fields=x_fields)



Delete reverse proxy

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
reverseproxy_id = 'reverseproxy_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_reverse_proxy(customer_id, cloudspace_id, reverseproxy_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->delete_reverse_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **reverseproxy_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server_pool**
> SuccessModel delete_server_pool(customer_id, cloudspace_id, serverpool_id, x_fields=x_fields)



Delete server pool

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
serverpool_id = 'serverpool_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.delete_server_pool(customer_id, cloudspace_id, serverpool_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->delete_server_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **serverpool_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_traefik_config**
> generate_traefik_config(customer_id, cloudspace_id)



Inspect configured traefik config

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 

try:
    api_instance.generate_traefik_config(customer_id, cloudspace_id)
except ApiException as e:
    print("Exception when calling AlphaApi->generate_traefik_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_card**
> get_customer_card(customer_id, card_id)



Get customer Card

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
card_id = 'card_id_example' # str | 

try:
    api_instance.get_customer_card(customer_id, card_id)
except ApiException as e:
    print("Exception when calling AlphaApi->get_customer_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **card_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reverse_proxy_info**
> ShowReverseProxyFull get_reverse_proxy_info(customer_id, cloudspace_id, reverseproxy_id, x_fields=x_fields)



Show reverse proxy information

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
reverseproxy_id = 'reverseproxy_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_reverse_proxy_info(customer_id, cloudspace_id, reverseproxy_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->get_reverse_proxy_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **reverseproxy_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ShowReverseProxyFull**](ShowReverseProxyFull.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_pool_info**
> ServerPool get_server_pool_info(customer_id, cloudspace_id, serverpool_id, x_fields=x_fields)



Show server pool information

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
serverpool_id = 'serverpool_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_server_pool_info(customer_id, cloudspace_id, serverpool_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->get_server_pool_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **serverpool_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ServerPool**](ServerPool.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloudspaces_reverse_proxies**
> ReverseProxyList list_cloudspaces_reverse_proxies(customer_id, cloudspace_id, x_fields=x_fields)



list cloudspace's reverse proxies

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_cloudspaces_reverse_proxies(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->list_cloudspaces_reverse_proxies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ReverseProxyList**](ReverseProxyList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloudspaces_server_pools**
> ServerPoolList list_cloudspaces_server_pools(customer_id, cloudspace_id, x_fields=x_fields)



list cloudspace's server pools

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_cloudspaces_server_pools(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->list_cloudspaces_server_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ServerPoolList**](ServerPoolList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_cards**
> list_customer_cards(customer_id)



List customer Cards

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    api_instance.list_customer_cards(customer_id)
except ApiException as e:
    print("Exception when calling AlphaApi->list_customer_cards: %s\n" % e)
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

# **list_load_balancers**
> LoadBalancerList list_load_balancers(customer_id, cloudspace_id, x_fields=x_fields)



list cloudspace's load balancers

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_load_balancers(customer_id, cloudspace_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->list_load_balancers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**LoadBalancerList**](LoadBalancerList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_server_pool_hosts**
> ServerPoolHosts list_server_pool_hosts(customer_id, cloudspace_id, serverpool_id, x_fields=x_fields)



List hosts inside server pool

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
serverpool_id = 'serverpool_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.list_server_pool_hosts(customer_id, cloudspace_id, serverpool_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->list_server_pool_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **serverpool_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ServerPoolHosts**](ServerPoolHosts.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_host_from_server_pool**
> SuccessModel remove_host_from_server_pool(customer_id, cloudspace_id, serverpool_id, host_id, x_fields=x_fields)



Remove Host from server pool

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
serverpool_id = 'serverpool_id_example' # str | 
host_id = 'host_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.remove_host_from_server_pool(customer_id, cloudspace_id, serverpool_id, host_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->remove_host_from_server_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **serverpool_id** | **str**|  | 
 **host_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_certificate**
> SuccessModel renew_certificate(customer_id, cloudspace_id, reverseproxy_id, x_fields=x_fields)



Renew acme certificate

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
reverseproxy_id = 'reverseproxy_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.renew_certificate(customer_id, cloudspace_id, reverseproxy_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->renew_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **reverseproxy_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_customer_card_as_default**
> set_customer_card_as_default(customer_id, card_id)



Set customer Card as Default

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
card_id = 'card_id_example' # str | 

try:
    api_instance.set_customer_card_as_default(customer_id, card_id)
except ApiException as e:
    print("Exception when calling AlphaApi->set_customer_card_as_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **card_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_load_balancer_info**
> ShowLoadBalancerFull show_load_balancer_info(customer_id, cloudspace_id, loadbalancer_id, x_fields=x_fields)



Show load balancer information

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
loadbalancer_id = 'loadbalancer_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.show_load_balancer_info(customer_id, cloudspace_id, loadbalancer_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->show_load_balancer_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **loadbalancer_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ShowLoadBalancerFull**](ShowLoadBalancerFull.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_load_balancer_info**
> SuccessModel update_load_balancer_info(customer_id, cloudspace_id, loadbalancer_id, payload, x_fields=x_fields)



Update load balancer information

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
loadbalancer_id = 'loadbalancer_id_example' # str | 
payload = pc4g.CreateLoadBalancerFull() # CreateLoadBalancerFull | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_load_balancer_info(customer_id, cloudspace_id, loadbalancer_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->update_load_balancer_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **loadbalancer_id** | **str**|  | 
 **payload** | [**CreateLoadBalancerFull**](CreateLoadBalancerFull.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reverse_proxy_info**
> SuccessModel update_reverse_proxy_info(customer_id, cloudspace_id, reverseproxy_id, payload, x_fields=x_fields)



Update reverse proxy information

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
reverseproxy_id = 'reverseproxy_id_example' # str | 
payload = pc4g.CreateReverseProxyFull() # CreateReverseProxyFull | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_reverse_proxy_info(customer_id, cloudspace_id, reverseproxy_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->update_reverse_proxy_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **reverseproxy_id** | **str**|  | 
 **payload** | [**CreateReverseProxyFull**](CreateReverseProxyFull.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_pool_info**
> SuccessModel update_server_pool_info(customer_id, cloudspace_id, serverpool_id, name=name, description=description, x_fields=x_fields)



Update server pool information

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
serverpool_id = 'serverpool_id_example' # str | 
name = 'name_example' # str | Name of the server pool (optional)
description = 'description_example' # str | Description of the server pool (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.update_server_pool_info(customer_id, cloudspace_id, serverpool_id, name=name, description=description, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlphaApi->update_server_pool_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **serverpool_id** | **str**|  | 
 **name** | **str**| Name of the server pool | [optional] 
 **description** | **str**| Description of the server pool | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SuccessModel**](SuccessModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_traefik_config**
> update_traefik_config(customer_id, cloudspace_id, payload)



Update traefik config

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
api_instance = pc4g.AlphaApi(pc4g.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
cloudspace_id = 'cloudspace_id_example' # str | 
payload = pc4g.IngressConfig() # IngressConfig | 

try:
    api_instance.update_traefik_config(customer_id, cloudspace_id, payload)
except ApiException as e:
    print("Exception when calling AlphaApi->update_traefik_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **cloudspace_id** | **str**|  | 
 **payload** | [**IngressConfig**](IngressConfig.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

