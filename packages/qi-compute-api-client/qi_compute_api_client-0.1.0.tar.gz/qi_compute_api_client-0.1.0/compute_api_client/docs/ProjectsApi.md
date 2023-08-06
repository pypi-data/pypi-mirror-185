# compute_api_client.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_projects_post**](ProjectsApi.md#create_project_projects_post) | **POST** /projects | Create project
[**delete_project_projects_id_delete**](ProjectsApi.md#delete_project_projects_id_delete) | **DELETE** /projects/{id} | Destroy project
[**partial_update_project_projects_id_patch**](ProjectsApi.md#partial_update_project_projects_id_patch) | **PATCH** /projects/{id} | Partially update project
[**read_project_projects_id_get**](ProjectsApi.md#read_project_projects_id_get) | **GET** /projects/{id} | Retrieve project
[**read_projects_projects_get**](ProjectsApi.md#read_projects_projects_get) | **GET** /projects | List projects
[**update_project_projects_id_put**](ProjectsApi.md#update_project_projects_id_put) | **PUT** /projects/{id} | Update project


# **create_project_projects_post**
> Project create_project_projects_post(project_in)

Create project

Create new project.

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
    api_instance = compute_api_client.ProjectsApi(api_client)
    project_in = compute_api_client.ProjectIn() # ProjectIn | 

    try:
        # Create project
        api_response = api_instance.create_project_projects_post(project_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_project_projects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_in** | [**ProjectIn**](ProjectIn.md)|  | 

### Return type

[**Project**](Project.md)

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

# **delete_project_projects_id_delete**
> delete_project_projects_id_delete(id)

Destroy project

Delete a project.

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
    api_instance = compute_api_client.ProjectsApi(api_client)
    id = 56 # int | 

    try:
        # Destroy project
        api_instance.delete_project_projects_id_delete(id)
    except ApiException as e:
        print("Exception when calling ProjectsApi->delete_project_projects_id_delete: %s\n" % e)
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

# **partial_update_project_projects_id_patch**
> Project partial_update_project_projects_id_patch(id, project_patch)

Partially update project

Partially update a project.

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
    api_instance = compute_api_client.ProjectsApi(api_client)
    id = 56 # int | 
project_patch = compute_api_client.ProjectPatch() # ProjectPatch | 

    try:
        # Partially update project
        api_response = api_instance.partial_update_project_projects_id_patch(id, project_patch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->partial_update_project_projects_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **project_patch** | [**ProjectPatch**](ProjectPatch.md)|  | 

### Return type

[**Project**](Project.md)

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

# **read_project_projects_id_get**
> Project read_project_projects_id_get(id)

Retrieve project

Get project by ID.

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
    api_instance = compute_api_client.ProjectsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve project
        api_response = api_instance.read_project_projects_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->read_project_projects_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Project**](Project.md)

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

# **read_projects_projects_get**
> list[Project] read_projects_projects_get()

List projects

List projects.

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
    api_instance = compute_api_client.ProjectsApi(api_client)
    
    try:
        # List projects
        api_response = api_instance.read_projects_projects_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->read_projects_projects_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

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

# **update_project_projects_id_put**
> Project update_project_projects_id_put(id, project_in)

Update project

Update a project.

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
    api_instance = compute_api_client.ProjectsApi(api_client)
    id = 56 # int | 
project_in = compute_api_client.ProjectIn() # ProjectIn | 

    try:
        # Update project
        api_response = api_instance.update_project_projects_id_put(id, project_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_project_projects_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **project_in** | [**ProjectIn**](ProjectIn.md)|  | 

### Return type

[**Project**](Project.md)

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

