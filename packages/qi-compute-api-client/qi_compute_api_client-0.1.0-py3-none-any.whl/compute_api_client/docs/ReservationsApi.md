# compute_api_client.ReservationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reservation_reservations_post**](ReservationsApi.md#create_reservation_reservations_post) | **POST** /reservations | Create reservation
[**read_reservation_reservations_id_get**](ReservationsApi.md#read_reservation_reservations_id_get) | **GET** /reservations/{id} | Retrieve reservation
[**read_reservations_reservations_get**](ReservationsApi.md#read_reservations_reservations_get) | **GET** /reservations | List reservations
[**terminate_reservation_reservations_id_terminate_patch**](ReservationsApi.md#terminate_reservation_reservations_id_terminate_patch) | **PATCH** /reservations/{id}/terminate | Terminate reservation


# **create_reservation_reservations_post**
> Reservation create_reservation_reservations_post(reservation_in)

Create reservation

Create new reservation.

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
    api_instance = compute_api_client.ReservationsApi(api_client)
    reservation_in = compute_api_client.ReservationIn() # ReservationIn | 

    try:
        # Create reservation
        api_response = api_instance.create_reservation_reservations_post(reservation_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReservationsApi->create_reservation_reservations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_in** | [**ReservationIn**](ReservationIn.md)|  | 

### Return type

[**Reservation**](Reservation.md)

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

# **read_reservation_reservations_id_get**
> Reservation read_reservation_reservations_id_get(id)

Retrieve reservation

Get reservation by ID.

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
    api_instance = compute_api_client.ReservationsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve reservation
        api_response = api_instance.read_reservation_reservations_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReservationsApi->read_reservation_reservations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Reservation**](Reservation.md)

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

# **read_reservations_reservations_get**
> list[Reservation] read_reservations_reservations_get()

List reservations

Read reservations.

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
    api_instance = compute_api_client.ReservationsApi(api_client)
    
    try:
        # List reservations
        api_response = api_instance.read_reservations_reservations_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReservationsApi->read_reservations_reservations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Reservation]**](Reservation.md)

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

# **terminate_reservation_reservations_id_terminate_patch**
> Reservation terminate_reservation_reservations_id_terminate_patch(id)

Terminate reservation

Terminate reservation by ID.

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
    api_instance = compute_api_client.ReservationsApi(api_client)
    id = 56 # int | 

    try:
        # Terminate reservation
        api_response = api_instance.terminate_reservation_reservations_id_terminate_patch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReservationsApi->terminate_reservation_reservations_id_terminate_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Reservation**](Reservation.md)

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

