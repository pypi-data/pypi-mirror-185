# compute_api_client.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_transaction_transactions_id_get**](TransactionsApi.md#read_transaction_transactions_id_get) | **GET** /transactions/{id} | Retrieve transactions
[**read_transactions_transactions_get**](TransactionsApi.md#read_transactions_transactions_get) | **GET** /transactions/ | List transactions


# **read_transaction_transactions_id_get**
> Transaction read_transaction_transactions_id_get(id)

Retrieve transactions

Get transaction by ID.

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
    api_instance = compute_api_client.TransactionsApi(api_client)
    id = 56 # int | 

    try:
        # Retrieve transactions
        api_response = api_instance.read_transaction_transactions_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->read_transaction_transactions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Transaction**](Transaction.md)

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

# **read_transactions_transactions_get**
> list[Transaction] read_transactions_transactions_get()

List transactions

Read transactions.

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
    api_instance = compute_api_client.TransactionsApi(api_client)
    
    try:
        # List transactions
        api_response = api_instance.read_transactions_transactions_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->read_transactions_transactions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Transaction]**](Transaction.md)

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

