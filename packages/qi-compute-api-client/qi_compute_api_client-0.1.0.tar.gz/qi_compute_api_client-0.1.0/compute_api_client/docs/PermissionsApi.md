# compute_api_client.PermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_permission_group_permission_groups_id_get**](PermissionsApi.md#read_permission_group_permission_groups_id_get) | **GET** /permission_groups/{id} | Retrieve permission groups
[**read_permission_groups_permission_groups_get**](PermissionsApi.md#read_permission_groups_permission_groups_get) | **GET** /permission_groups/ | List permission groups
[**read_permission_permissions_id_get**](PermissionsApi.md#read_permission_permissions_id_get) | **GET** /permissions/{id} | Retrieve permissions
[**read_permissions_permissions_get**](PermissionsApi.md#read_permissions_permissions_get) | **GET** /permissions/ | List permissions


# **read_permission_group_permission_groups_id_get**
> PermissionGroup read_permission_group_permission_groups_id_get(id)

Retrieve permission groups

Get permission group by ID.

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
    api_instance = compute_api_client.PermissionsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve permission groups
        api_response = api_instance.read_permission_group_permission_groups_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->read_permission_group_permission_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PermissionGroup**](PermissionGroup.md)

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

# **read_permission_groups_permission_groups_get**
> list[PermissionGroup] read_permission_groups_permission_groups_get()

List permission groups

Read permissions groups.

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
    api_instance = compute_api_client.PermissionsApi(api_client)
    
    try:
        # List permission groups
        api_response = api_instance.read_permission_groups_permission_groups_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->read_permission_groups_permission_groups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PermissionGroup]**](PermissionGroup.md)

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

# **read_permission_permissions_id_get**
> Permission read_permission_permissions_id_get(id)

Retrieve permissions

Get permission by ID.

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
    api_instance = compute_api_client.PermissionsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve permissions
        api_response = api_instance.read_permission_permissions_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->read_permission_permissions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Permission**](Permission.md)

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

# **read_permissions_permissions_get**
> list[Permission] read_permissions_permissions_get()

List permissions

Read permissions.

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
    api_instance = compute_api_client.PermissionsApi(api_client)
    
    try:
        # List permissions
        api_response = api_instance.read_permissions_permissions_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->read_permissions_permissions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Permission]**](Permission.md)

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

