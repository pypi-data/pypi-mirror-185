# compute_api_client.RunsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_run_runs_post**](RunsApi.md#create_run_runs_post) | **POST** /runs | Create run
[**delete_run_runs_id_delete**](RunsApi.md#delete_run_runs_id_delete) | **DELETE** /runs/{id} | Destroy run
[**read_run_runs_id_get**](RunsApi.md#read_run_runs_id_get) | **GET** /runs/{id} | Retrieve run
[**read_runs_runs_get**](RunsApi.md#read_runs_runs_get) | **GET** /runs | List runs
[**start_run_runs_id_start_patch**](RunsApi.md#start_run_runs_id_start_patch) | **PATCH** /runs/{id}/start | Start run


# **create_run_runs_post**
> Run create_run_runs_post(run_in)

Create run

Create new run.

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
    api_instance = compute_api_client.RunsApi(api_client)
    run_in = compute_api_client.RunIn() # RunIn | 

    try:
        # Create run
        api_response = api_instance.create_run_runs_post(run_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->create_run_runs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_in** | [**RunIn**](RunIn.md)|  | 

### Return type

[**Run**](Run.md)

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

# **delete_run_runs_id_delete**
> delete_run_runs_id_delete(id)

Destroy run

Delete a run.

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
    api_instance = compute_api_client.RunsApi(api_client)
    id = 56 # int | 

    try:
        # Destroy run
        api_instance.delete_run_runs_id_delete(id)
    except ApiException as e:
        print("Exception when calling RunsApi->delete_run_runs_id_delete: %s\n" % e)
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

# **read_run_runs_id_get**
> Run read_run_runs_id_get(id)

Retrieve run

Get run by ID.

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
    api_instance = compute_api_client.RunsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve run
        api_response = api_instance.read_run_runs_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->read_run_runs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Run**](Run.md)

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

# **read_runs_runs_get**
> list[Run] read_runs_runs_get()

List runs

List runs.

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
    api_instance = compute_api_client.RunsApi(api_client)
    
    try:
        # List runs
        api_response = api_instance.read_runs_runs_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->read_runs_runs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Run]**](Run.md)

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

# **start_run_runs_id_start_patch**
> Run start_run_runs_id_start_patch(id)

Start run

Start a run.

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
    api_instance = compute_api_client.RunsApi(api_client)
    id = 56 # int | 

    try:
        # Start run
        api_response = api_instance.start_run_runs_id_start_patch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->start_run_runs_id_start_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Run**](Run.md)

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

