# rhoas-service-registry-mgmt-sdk
Service Registry Management API is a REST API for managing Service Registry instances. Service Registry is a datastore for event schemas and API designs, which is based on the open source Apicurio Registry project.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.6
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://console.redhat.com/application-services/service-registry/](https://console.redhat.com/application-services/service-registry/)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

The package is hosted on [PyPI](https://pypi.org/project/rhoas-sdks/), you can install directly using:

```sh
pip install rhoas_service_registry_mgmt_sdk
```

Then import the package:
```python
import rhoas_service_registry_mgmt_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import rhoas_service_registry_mgmt_sdk
from pprint import pprint
from rhoas_service_registry_mgmt_sdk.api import errors_api
from rhoas_service_registry_mgmt_sdk.model.error import Error
from rhoas_service_registry_mgmt_sdk.model.error_list import ErrorList
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_registry_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)



# Enter a context with an instance of the API client
with rhoas_service_registry_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = errors_api.ErrorsApi(api_client)
    id = 1 # int | A unique identifier for an error type.

    try:
        api_response = api_instance.get_error(id)
        pprint(api_response)
    except rhoas_service_registry_mgmt_sdk.ApiException as e:
        print("Exception when calling ErrorsApi->get_error: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.openshift.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ErrorsApi* | [**get_error**](docs/ErrorsApi.md#get_error) | **GET** /api/serviceregistry_mgmt/v1/errors/{id} | 
*ErrorsApi* | [**get_errors**](docs/ErrorsApi.md#get_errors) | **GET** /api/serviceregistry_mgmt/v1/errors | 
*RegistriesApi* | [**create_registry**](docs/RegistriesApi.md#create_registry) | **POST** /api/serviceregistry_mgmt/v1/registries | 
*RegistriesApi* | [**delete_registry**](docs/RegistriesApi.md#delete_registry) | **DELETE** /api/serviceregistry_mgmt/v1/registries/{id} | Delete a Registry instance
*RegistriesApi* | [**get_registries**](docs/RegistriesApi.md#get_registries) | **GET** /api/serviceregistry_mgmt/v1/registries | 
*RegistriesApi* | [**get_registry**](docs/RegistriesApi.md#get_registry) | **GET** /api/serviceregistry_mgmt/v1/registries/{id} | Get a Registry instance
*DefaultApi* | [**get_service_status**](docs/DefaultApi.md#get_service_status) | **GET** /api/serviceregistry_mgmt/v1/status | 


## Documentation For Models

 - [Error](docs/Error.md)
 - [ErrorList](docs/ErrorList.md)
 - [ErrorListAllOf](docs/ErrorListAllOf.md)
 - [List](docs/List.md)
 - [ObjectReference](docs/ObjectReference.md)
 - [Registry](docs/Registry.md)
 - [RegistryCreate](docs/RegistryCreate.md)
 - [RegistryInstanceTypeValue](docs/RegistryInstanceTypeValue.md)
 - [RegistryList](docs/RegistryList.md)
 - [RegistryListAllOf](docs/RegistryListAllOf.md)
 - [RegistryStatusValue](docs/RegistryStatusValue.md)
 - [RootTypeForRegistry](docs/RootTypeForRegistry.md)
 - [ServiceStatus](docs/ServiceStatus.md)


## Documentation For Authorization


## Bearer

- **Type**: Bearer authentication (JWT)


## Author

rhosak-eval-support@redhat.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in rhoas_service_registry_mgmt_sdk.apis and rhoas_service_registry_mgmt_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from rhoas_service_registry_mgmt_sdk.api.default_api import DefaultApi`
- `from rhoas_service_registry_mgmt_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import rhoas_service_registry_mgmt_sdk
from rhoas_service_registry_mgmt_sdk.apis import *
from rhoas_service_registry_mgmt_sdk.models import *
```
