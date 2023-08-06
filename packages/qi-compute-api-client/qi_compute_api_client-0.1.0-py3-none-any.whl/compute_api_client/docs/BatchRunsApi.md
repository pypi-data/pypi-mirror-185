# compute_api_client.BatchRunsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_run_batch_runs_post**](BatchRunsApi.md#create_batch_run_batch_runs_post) | **POST** /batch_runs | Create batch run
[**enqueue_batch_run_batch_runs_id_enqueue_patch**](BatchRunsApi.md#enqueue_batch_run_batch_runs_id_enqueue_patch) | **PATCH** /batch_runs/{id}/enqueue | Enqueue batch run for execution
[**finish_batch_run_batch_runs_id_finish_patch**](BatchRunsApi.md#finish_batch_run_batch_runs_id_finish_patch) | **PATCH** /batch_runs/{id}/finish | Finish batch run
[**peek_batch_run_batch_runs_peek_patch**](BatchRunsApi.md#peek_batch_run_batch_runs_peek_patch) | **PATCH** /batch_runs/peek | Peek batch run
[**pop_batch_run_batch_runs_pop_patch**](BatchRunsApi.md#pop_batch_run_batch_runs_pop_patch) | **PATCH** /batch_runs/pop | Take batch run
[**read_batch_runs_batch_runs_get**](BatchRunsApi.md#read_batch_runs_batch_runs_get) | **GET** /batch_runs | List batch runs


# **create_batch_run_batch_runs_post**
> BatchRun create_batch_run_batch_runs_post(batch_run_in)

Create batch run

Create new batch run.

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
    api_instance = compute_api_client.BatchRunsApi(api_client)
    batch_run_in = compute_api_client.BatchRunIn() # BatchRunIn | 

    try:
        # Create batch run
        api_response = api_instance.create_batch_run_batch_runs_post(batch_run_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchRunsApi->create_batch_run_batch_runs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_run_in** | [**BatchRunIn**](BatchRunIn.md)|  | 

### Return type

[**BatchRun**](BatchRun.md)

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

# **enqueue_batch_run_batch_runs_id_enqueue_patch**
> BatchRun enqueue_batch_run_batch_runs_id_enqueue_patch(id)

Enqueue batch run for execution

Enqueue batch run for execution.

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
    api_instance = compute_api_client.BatchRunsApi(api_client)
    id = 56 # int | 

    try:
        # Enqueue batch run for execution
        api_response = api_instance.enqueue_batch_run_batch_runs_id_enqueue_patch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchRunsApi->enqueue_batch_run_batch_runs_id_enqueue_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BatchRun**](BatchRun.md)

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

# **finish_batch_run_batch_runs_id_finish_patch**
> BatchRun finish_batch_run_batch_runs_id_finish_patch(id)

Finish batch run

Finish batch run.

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
    api_instance = compute_api_client.BatchRunsApi(api_client)
    id = 56 # int | 

    try:
        # Finish batch run
        api_response = api_instance.finish_batch_run_batch_runs_id_finish_patch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchRunsApi->finish_batch_run_batch_runs_id_finish_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BatchRun**](BatchRun.md)

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

# **peek_batch_run_batch_runs_peek_patch**
> BatchRun peek_batch_run_batch_runs_peek_patch(request_body)

Peek batch run

Get batch run that can be taken up, excluding list of IDs.

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
    api_instance = compute_api_client.BatchRunsApi(api_client)
    request_body = [56] # list[int] | 

    try:
        # Peek batch run
        api_response = api_instance.peek_batch_run_batch_runs_peek_patch(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchRunsApi->peek_batch_run_batch_runs_peek_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[int]**](int.md)|  | 

### Return type

[**BatchRun**](BatchRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pop_batch_run_batch_runs_pop_patch**
> BatchRun pop_batch_run_batch_runs_pop_patch()

Take batch run

Claim batch run by ID.

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
    api_instance = compute_api_client.BatchRunsApi(api_client)
    
    try:
        # Take batch run
        api_response = api_instance.pop_batch_run_batch_runs_pop_patch()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchRunsApi->pop_batch_run_batch_runs_pop_patch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BatchRun**](BatchRun.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_batch_runs_batch_runs_get**
> list[BatchRun] read_batch_runs_batch_runs_get()

List batch runs

List batch runs.

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
    api_instance = compute_api_client.BatchRunsApi(api_client)
    
    try:
        # List batch runs
        api_response = api_instance.read_batch_runs_batch_runs_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchRunsApi->read_batch_runs_batch_runs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BatchRun]**](BatchRun.md)

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

