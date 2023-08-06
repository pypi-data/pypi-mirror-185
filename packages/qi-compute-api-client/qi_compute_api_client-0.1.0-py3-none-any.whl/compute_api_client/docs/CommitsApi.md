# compute_api_client.CommitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_commit_commits_post**](CommitsApi.md#create_commit_commits_post) | **POST** /commits | Create commit
[**delete_commit_commits_id_delete**](CommitsApi.md#delete_commit_commits_id_delete) | **DELETE** /commits/{id} | Destroy commit
[**read_commit_commits_id_get**](CommitsApi.md#read_commit_commits_id_get) | **GET** /commits/{id} | Get commit by ID
[**read_commits_commits_get**](CommitsApi.md#read_commits_commits_get) | **GET** /commits | List commits


# **create_commit_commits_post**
> Commit create_commit_commits_post(commit_in)

Create commit

Create new commit.

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
    api_instance = compute_api_client.CommitsApi(api_client)
    commit_in = compute_api_client.CommitIn() # CommitIn | 

    try:
        # Create commit
        api_response = api_instance.create_commit_commits_post(commit_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommitsApi->create_commit_commits_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commit_in** | [**CommitIn**](CommitIn.md)|  | 

### Return type

[**Commit**](Commit.md)

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

# **delete_commit_commits_id_delete**
> delete_commit_commits_id_delete(id)

Destroy commit

Delete a commit.

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
    api_instance = compute_api_client.CommitsApi(api_client)
    id = 56 # int | 

    try:
        # Destroy commit
        api_instance.delete_commit_commits_id_delete(id)
    except ApiException as e:
        print("Exception when calling CommitsApi->delete_commit_commits_id_delete: %s\n" % e)
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

# **read_commit_commits_id_get**
> Commit read_commit_commits_id_get(id)

Get commit by ID

Get commit by ID.

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
    api_instance = compute_api_client.CommitsApi(api_client)
    id = 56 # int | 

    try:
        # Get commit by ID
        api_response = api_instance.read_commit_commits_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommitsApi->read_commit_commits_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Commit**](Commit.md)

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

# **read_commits_commits_get**
> list[Commit] read_commits_commits_get()

List commits

List commits.

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
    api_instance = compute_api_client.CommitsApi(api_client)
    
    try:
        # List commits
        api_response = api_instance.read_commits_commits_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommitsApi->read_commits_commits_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Commit]**](Commit.md)

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

