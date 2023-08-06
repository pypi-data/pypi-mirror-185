# compute_api_client.FinalResultsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_final_result_final_results_post**](FinalResultsApi.md#create_final_result_final_results_post) | **POST** /final_results | Create final result
[**read_final_result_by_run_id_final_results_run_run_id_get**](FinalResultsApi.md#read_final_result_by_run_id_final_results_run_run_id_get) | **GET** /final_results/run/{run_id} | Retrieve final result by run ID
[**read_final_result_final_results_id_get**](FinalResultsApi.md#read_final_result_final_results_id_get) | **GET** /final_results/{id} | Retrieve final result


# **create_final_result_final_results_post**
> FinalResult create_final_result_final_results_post(final_result_in)

Create final result

Create new final result.

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
    api_instance = compute_api_client.FinalResultsApi(api_client)
    final_result_in = compute_api_client.FinalResultIn() # FinalResultIn | 

    try:
        # Create final result
        api_response = api_instance.create_final_result_final_results_post(final_result_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinalResultsApi->create_final_result_final_results_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **final_result_in** | [**FinalResultIn**](FinalResultIn.md)|  | 

### Return type

[**FinalResult**](FinalResult.md)

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

# **read_final_result_by_run_id_final_results_run_run_id_get**
> FinalResult read_final_result_by_run_id_final_results_run_run_id_get(run_id)

Retrieve final result by run ID

Get final result by run ID.

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
    api_instance = compute_api_client.FinalResultsApi(api_client)
    run_id = 56 # int | 

    try:
        # Retrieve final result by run ID
        api_response = api_instance.read_final_result_by_run_id_final_results_run_run_id_get(run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinalResultsApi->read_final_result_by_run_id_final_results_run_run_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **int**|  | 

### Return type

[**FinalResult**](FinalResult.md)

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

# **read_final_result_final_results_id_get**
> FinalResult read_final_result_final_results_id_get(id)

Retrieve final result

Get final result by ID.

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
    api_instance = compute_api_client.FinalResultsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve final result
        api_response = api_instance.read_final_result_final_results_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinalResultsApi->read_final_result_final_results_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FinalResult**](FinalResult.md)

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

