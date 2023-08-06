# compute_api_client.MetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata_metadata_post**](MetadataApi.md#create_metadata_metadata_post) | **POST** /metadata | Create metadata
[**read_metadata_by_runtime_id_metadata_runtime_runtime_id_get**](MetadataApi.md#read_metadata_by_runtime_id_metadata_runtime_runtime_id_get) | **GET** /metadata/runtime/{runtime_id} | Retrieve metadata by runtime ID
[**read_metadata_metadata_id_get**](MetadataApi.md#read_metadata_metadata_id_get) | **GET** /metadata/{id} | Get metadata by ID


# **create_metadata_metadata_post**
> Metadata create_metadata_metadata_post(metadata_in)

Create metadata

Create new metadata.

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
    api_instance = compute_api_client.MetadataApi(api_client)
    metadata_in = compute_api_client.MetadataIn() # MetadataIn | 

    try:
        # Create metadata
        api_response = api_instance.create_metadata_metadata_post(metadata_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataApi->create_metadata_metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_in** | [**MetadataIn**](MetadataIn.md)|  | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_metadata_by_runtime_id_metadata_runtime_runtime_id_get**
> list[Metadata] read_metadata_by_runtime_id_metadata_runtime_runtime_id_get(runtime_id)

Retrieve metadata by runtime ID

Get metadata by run ID.

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
    api_instance = compute_api_client.MetadataApi(api_client)
    runtime_id = 56 # int | 

    try:
        # Retrieve metadata by runtime ID
        api_response = api_instance.read_metadata_by_runtime_id_metadata_runtime_runtime_id_get(runtime_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataApi->read_metadata_by_runtime_id_metadata_runtime_runtime_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime_id** | **int**|  | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_metadata_metadata_id_get**
> Metadata read_metadata_metadata_id_get(id)

Get metadata by ID

Get metadata by ID.

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
    api_instance = compute_api_client.MetadataApi(api_client)
    id = 56 # int | 

    try:
        # Get metadata by ID
        api_response = api_instance.read_metadata_metadata_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataApi->read_metadata_metadata_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Metadata**](Metadata.md)

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

