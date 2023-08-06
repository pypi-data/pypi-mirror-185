# compute_api_client.RuntimeTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_runtime_type_runtime_types_id_get**](RuntimeTypesApi.md#read_runtime_type_runtime_types_id_get) | **GET** /runtime_types/{id} | Retrieve runtime type
[**read_runtime_types_runtime_types_get**](RuntimeTypesApi.md#read_runtime_types_runtime_types_get) | **GET** /runtime_types/ | List runtime types


# **read_runtime_type_runtime_types_id_get**
> RuntimeType read_runtime_type_runtime_types_id_get(id)

Retrieve runtime type

Get runtime type by ID.

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
    api_instance = compute_api_client.RuntimeTypesApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve runtime type
        api_response = api_instance.read_runtime_type_runtime_types_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RuntimeTypesApi->read_runtime_type_runtime_types_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RuntimeType**](RuntimeType.md)

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

# **read_runtime_types_runtime_types_get**
> list[RuntimeType] read_runtime_types_runtime_types_get()

List runtime types

Read runtime types.

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
    api_instance = compute_api_client.RuntimeTypesApi(api_client)
    
    try:
        # List runtime types
        api_response = api_instance.read_runtime_types_runtime_types_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RuntimeTypesApi->read_runtime_types_runtime_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RuntimeType]**](RuntimeType.md)

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

