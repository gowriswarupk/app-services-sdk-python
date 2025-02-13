# rhoas-connector-mgmt-sdk
Connector Management API is a REST API to manage connectors.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

The package is hosted on [PyPI](https://pypi.org/project/rhoas-sdks/), you can install directly using:

```sh
pip install rhoas_connector_mgmt_sdk
```

Then import the package:
```python
import rhoas_connector_mgmt_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import rhoas_connector_mgmt_sdk
from pprint import pprint
from rhoas_connector_mgmt_sdk.api import connector_clusters_api
from rhoas_connector_mgmt_sdk.model.addon_parameter_list import AddonParameterList
from rhoas_connector_mgmt_sdk.model.connector_cluster import ConnectorCluster
from rhoas_connector_mgmt_sdk.model.connector_cluster_list import ConnectorClusterList
from rhoas_connector_mgmt_sdk.model.connector_cluster_request import ConnectorClusterRequest
from rhoas_connector_mgmt_sdk.model.connector_namespace_list import ConnectorNamespaceList
from rhoas_connector_mgmt_sdk.model.error import Error
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_connector_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_connector_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with rhoas_connector_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connector_clusters_api.ConnectorClustersApi(api_client)
    _async = True # bool | Perform the action in an asynchronous manner
    connector_cluster_request = ConnectorClusterRequest(None) # ConnectorClusterRequest | Connector cluster data

    try:
        # Create a new connector cluster
        api_response = api_instance.create_connector_cluster(_async, connector_cluster_request)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->create_connector_cluster: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.openshift.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConnectorClustersApi* | [**create_connector_cluster**](docs/ConnectorClustersApi.md#create_connector_cluster) | **POST** /api/connector_mgmt/v1/kafka_connector_clusters | Create a new connector cluster
*ConnectorClustersApi* | [**delete_connector_cluster**](docs/ConnectorClustersApi.md#delete_connector_cluster) | **DELETE** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id} | Delete a connector cluster
*ConnectorClustersApi* | [**get_connector_cluster**](docs/ConnectorClustersApi.md#get_connector_cluster) | **GET** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id} | Get a connector cluster
*ConnectorClustersApi* | [**get_connector_cluster_addon_parameters**](docs/ConnectorClustersApi.md#get_connector_cluster_addon_parameters) | **GET** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id}/addon_parameters | Get a connector cluster&#39;s addon parameters
*ConnectorClustersApi* | [**get_connector_cluster_namespaces**](docs/ConnectorClustersApi.md#get_connector_cluster_namespaces) | **GET** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id}/namespaces | Get a connector cluster&#39;s namespaces
*ConnectorClustersApi* | [**list_connector_clusters**](docs/ConnectorClustersApi.md#list_connector_clusters) | **GET** /api/connector_mgmt/v1/kafka_connector_clusters | Returns a list of connector clusters
*ConnectorClustersApi* | [**update_connector_cluster_by_id**](docs/ConnectorClustersApi.md#update_connector_cluster_by_id) | **PUT** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id} | udpate a connector cluster
*ConnectorNamespacesApi* | [**create_evaluation_namespace**](docs/ConnectorNamespacesApi.md#create_evaluation_namespace) | **POST** /api/connector_mgmt/v1/kafka_connector_namespaces/eval | Create a new short lived evaluation connector namespace
*ConnectorNamespacesApi* | [**get_connector_namespace**](docs/ConnectorNamespacesApi.md#get_connector_namespace) | **GET** /api/connector_mgmt/v1/kafka_connector_namespaces/{connector_namespace_id} | Get a connector namespace
*ConnectorNamespacesApi* | [**list_connector_namespaces**](docs/ConnectorNamespacesApi.md#list_connector_namespaces) | **GET** /api/connector_mgmt/v1/kafka_connector_namespaces | Returns a list of connector namespaces
*ConnectorServiceApi* | [**get_version_metadata**](docs/ConnectorServiceApi.md#get_version_metadata) | **GET** /api/connector_mgmt/v1 | Returns the version metadata
*ConnectorTypesApi* | [**get_connector_type_by_id**](docs/ConnectorTypesApi.md#get_connector_type_by_id) | **GET** /api/connector_mgmt/v1/kafka_connector_types/{connector_type_id} | Get a connector type by id
*ConnectorTypesApi* | [**get_connector_types**](docs/ConnectorTypesApi.md#get_connector_types) | **GET** /api/connector_mgmt/v1/kafka_connector_types | Returns a list of connector types
*ConnectorsApi* | [**create_connector**](docs/ConnectorsApi.md#create_connector) | **POST** /api/connector_mgmt/v1/kafka_connectors | Create a new connector
*ConnectorsApi* | [**delete_connector**](docs/ConnectorsApi.md#delete_connector) | **DELETE** /api/connector_mgmt/v1/kafka_connectors/{id} | Delete a connector
*ConnectorsApi* | [**get_connector**](docs/ConnectorsApi.md#get_connector) | **GET** /api/connector_mgmt/v1/kafka_connectors/{id} | Get a connector
*ConnectorsApi* | [**list_connectors**](docs/ConnectorsApi.md#list_connectors) | **GET** /api/connector_mgmt/v1/kafka_connectors | Returns a list of connector types
*ConnectorsApi* | [**patch_connector**](docs/ConnectorsApi.md#patch_connector) | **PATCH** /api/connector_mgmt/v1/kafka_connectors/{id} | Patch a connector


## Documentation For Models

 - [AddonParameter](docs/AddonParameter.md)
 - [AddonParameterList](docs/AddonParameterList.md)
 - [Channel](docs/Channel.md)
 - [Connector](docs/Connector.md)
 - [ConnectorCluster](docs/ConnectorCluster.md)
 - [ConnectorClusterList](docs/ConnectorClusterList.md)
 - [ConnectorClusterListAllOf](docs/ConnectorClusterListAllOf.md)
 - [ConnectorClusterMeta](docs/ConnectorClusterMeta.md)
 - [ConnectorClusterRequest](docs/ConnectorClusterRequest.md)
 - [ConnectorClusterRequestMeta](docs/ConnectorClusterRequestMeta.md)
 - [ConnectorClusterState](docs/ConnectorClusterState.md)
 - [ConnectorClusterStatus](docs/ConnectorClusterStatus.md)
 - [ConnectorClusterStatusStatus](docs/ConnectorClusterStatusStatus.md)
 - [ConnectorConfiguration](docs/ConnectorConfiguration.md)
 - [ConnectorDesiredState](docs/ConnectorDesiredState.md)
 - [ConnectorList](docs/ConnectorList.md)
 - [ConnectorListAllOf](docs/ConnectorListAllOf.md)
 - [ConnectorMeta](docs/ConnectorMeta.md)
 - [ConnectorMetaAllOf](docs/ConnectorMetaAllOf.md)
 - [ConnectorNamespace](docs/ConnectorNamespace.md)
 - [ConnectorNamespaceAllOf](docs/ConnectorNamespaceAllOf.md)
 - [ConnectorNamespaceEvalRequest](docs/ConnectorNamespaceEvalRequest.md)
 - [ConnectorNamespaceList](docs/ConnectorNamespaceList.md)
 - [ConnectorNamespaceListAllOf](docs/ConnectorNamespaceListAllOf.md)
 - [ConnectorNamespaceMeta](docs/ConnectorNamespaceMeta.md)
 - [ConnectorNamespaceMetaAllOf](docs/ConnectorNamespaceMetaAllOf.md)
 - [ConnectorNamespacePatchRequest](docs/ConnectorNamespacePatchRequest.md)
 - [ConnectorNamespaceQuota](docs/ConnectorNamespaceQuota.md)
 - [ConnectorNamespaceRequest](docs/ConnectorNamespaceRequest.md)
 - [ConnectorNamespaceRequestAllOf](docs/ConnectorNamespaceRequestAllOf.md)
 - [ConnectorNamespaceRequestMeta](docs/ConnectorNamespaceRequestMeta.md)
 - [ConnectorNamespaceState](docs/ConnectorNamespaceState.md)
 - [ConnectorNamespaceStatus](docs/ConnectorNamespaceStatus.md)
 - [ConnectorNamespaceTenant](docs/ConnectorNamespaceTenant.md)
 - [ConnectorNamespaceTenantKind](docs/ConnectorNamespaceTenantKind.md)
 - [ConnectorRequest](docs/ConnectorRequest.md)
 - [ConnectorRequestMeta](docs/ConnectorRequestMeta.md)
 - [ConnectorState](docs/ConnectorState.md)
 - [ConnectorStatus](docs/ConnectorStatus.md)
 - [ConnectorStatusStatus](docs/ConnectorStatusStatus.md)
 - [ConnectorType](docs/ConnectorType.md)
 - [ConnectorTypeAllOf](docs/ConnectorTypeAllOf.md)
 - [ConnectorTypeList](docs/ConnectorTypeList.md)
 - [ConnectorTypeListAllOf](docs/ConnectorTypeListAllOf.md)
 - [CpuQuota](docs/CpuQuota.md)
 - [Error](docs/Error.md)
 - [KafkaConnectionSettings](docs/KafkaConnectionSettings.md)
 - [List](docs/List.md)
 - [MemoryQuota](docs/MemoryQuota.md)
 - [ObjectMeta](docs/ObjectMeta.md)
 - [ObjectReference](docs/ObjectReference.md)
 - [SchemaRegistryConnectionSettings](docs/SchemaRegistryConnectionSettings.md)
 - [ServiceAccount](docs/ServiceAccount.md)
 - [ServiceConnectionSettings](docs/ServiceConnectionSettings.md)
 - [VersionMetadata](docs/VersionMetadata.md)
 - [VersionMetadataAllOf](docs/VersionMetadataAllOf.md)


## Documentation For Authorization


## Bearer

- **Type**: Bearer authentication (JWT)


## Author

rhosak-support@redhat.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in rhoas_connector_mgmt_sdk.apis and rhoas_connector_mgmt_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from rhoas_connector_mgmt_sdk.api.default_api import DefaultApi`
- `from rhoas_connector_mgmt_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.apis import *
from rhoas_connector_mgmt_sdk.models import *
```
