# compute_api_client.AlgorithmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_algorithm_algorithms_post**](AlgorithmsApi.md#create_algorithm_algorithms_post) | **POST** /algorithms | Create algorithm
[**delete_algorithm_algorithms_id_delete**](AlgorithmsApi.md#delete_algorithm_algorithms_id_delete) | **DELETE** /algorithms/{id} | Destroy algorithm
[**read_algorithm_algorithms_id_get**](AlgorithmsApi.md#read_algorithm_algorithms_id_get) | **GET** /algorithms/{id} | Retrieve algorithm
[**read_algorithms_algorithms_get**](AlgorithmsApi.md#read_algorithms_algorithms_get) | **GET** /algorithms | List algorithms
[**update_algorithm_algorithms_id_put**](AlgorithmsApi.md#update_algorithm_algorithms_id_put) | **PUT** /algorithms/{id} | Update algorithm


# **create_algorithm_algorithms_post**
> Algorithm create_algorithm_algorithms_post(algorithm_in)

Create algorithm

Create new algorithm.

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
    api_instance = compute_api_client.AlgorithmsApi(api_client)
    algorithm_in = compute_api_client.AlgorithmIn() # AlgorithmIn | 

    try:
        # Create algorithm
        api_response = api_instance.create_algorithm_algorithms_post(algorithm_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlgorithmsApi->create_algorithm_algorithms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algorithm_in** | [**AlgorithmIn**](AlgorithmIn.md)|  | 

### Return type

[**Algorithm**](Algorithm.md)

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

# **delete_algorithm_algorithms_id_delete**
> delete_algorithm_algorithms_id_delete(id)

Destroy algorithm

Delete an algorithm.

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
    api_instance = compute_api_client.AlgorithmsApi(api_client)
    id = 56 # int | 

    try:
        # Destroy algorithm
        api_instance.delete_algorithm_algorithms_id_delete(id)
    except ApiException as e:
        print("Exception when calling AlgorithmsApi->delete_algorithm_algorithms_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_algorithm_algorithms_id_get**
> Algorithm read_algorithm_algorithms_id_get(id)

Retrieve algorithm

Get algorithm by ID.

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
    api_instance = compute_api_client.AlgorithmsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve algorithm
        api_response = api_instance.read_algorithm_algorithms_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlgorithmsApi->read_algorithm_algorithms_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Algorithm**](Algorithm.md)

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

# **read_algorithms_algorithms_get**
> list[Algorithm] read_algorithms_algorithms_get()

List algorithms

List algorithms.

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
    api_instance = compute_api_client.AlgorithmsApi(api_client)
    
    try:
        # List algorithms
        api_response = api_instance.read_algorithms_algorithms_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlgorithmsApi->read_algorithms_algorithms_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Algorithm]**](Algorithm.md)

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

# **update_algorithm_algorithms_id_put**
> Algorithm update_algorithm_algorithms_id_put(id, algorithm_in)

Update algorithm

Update an algorithm.

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
    api_instance = compute_api_client.AlgorithmsApi(api_client)
    id = 56 # int | 
algorithm_in = compute_api_client.AlgorithmIn() # AlgorithmIn | 

    try:
        # Update algorithm
        api_response = api_instance.update_algorithm_algorithms_id_put(id, algorithm_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlgorithmsApi->update_algorithm_algorithms_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **algorithm_in** | [**AlgorithmIn**](AlgorithmIn.md)|  | 

### Return type

[**Algorithm**](Algorithm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

