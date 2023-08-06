# compute_api_client.RuntimeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_runtime_runtimes_id_get**](RuntimeApi.md#read_runtime_runtimes_id_get) | **GET** /runtimes/{id} | Retrieve runtime
[**read_runtimes_runtimes_get**](RuntimeApi.md#read_runtimes_runtimes_get) | **GET** /runtimes | List runtimes


# **read_runtime_runtimes_id_get**
> Runtime read_runtime_runtimes_id_get(id)

Retrieve runtime

Get runtime by ID.

### Example

```python
from __future__ import print_function
import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with compute_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.RuntimeApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve runtime
        api_response = api_instance.read_runtime_runtimes_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RuntimeApi->read_runtime_runtimes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Runtime**](Runtime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_runtimes_runtimes_get**
> list[Runtime] read_runtimes_runtimes_get()

List runtimes

Read runtimes.

### Example

```python
from __future__ import print_function
import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with compute_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.RuntimeApi(api_client)
    
    try:
        # List runtimes
        api_response = api_instance.read_runtimes_runtimes_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RuntimeApi->read_runtimes_runtimes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Runtime]**](Runtime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

