"""
    Apicurio Registry API [v2]

    Apicurio Registry is a datastore for standard event schemas and API designs. Apicurio Registry enables developers to manage and share the structure of their data using a REST interface. For example, client applications can dynamically push or pull the latest updates to or from the registry without needing to redeploy. Apicurio Registry also enables developers to create rules that govern how registry content can evolve over time. For example, this includes rules for content validation and version compatibility.  The Apicurio Registry REST API enables client applications to manage the artifacts in the registry. This API provides create, read, update, and delete operations for schema and API artifacts, rules, versions, and metadata.   The supported artifact types include: - Apache Avro schema - AsyncAPI specification - Google protocol buffers - GraphQL schema - JSON Schema - Kafka Connect schema - OpenAPI specification - Web Services Description Language - XML Schema Definition   **Important**: The Apicurio Registry REST API is available from `https://MY-REGISTRY-URL/apis/registry/v2` by default. Therefore you must prefix all API operation paths with `../apis/registry/v2` in this case. For example: `../apis/registry/v2/ids/globalIds/{globalId}`.   # noqa: E501

    The version of the OpenAPI document: 2.2.5.Final
    Contact: apicurio@lists.jboss.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import rhoas_registry_instance_sdk
from rhoas_registry_instance_sdk.api.artifacts_api import ArtifactsApi  # noqa: E501


class TestArtifactsApi(unittest.TestCase):
    """ArtifactsApi unit test stubs"""

    def setUp(self):
        self.api = ArtifactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_artifact(self):
        """Test case for create_artifact

        Create artifact  # noqa: E501
        """
        pass

    def test_delete_artifact(self):
        """Test case for delete_artifact

        Delete artifact  # noqa: E501
        """
        pass

    def test_delete_artifacts_in_group(self):
        """Test case for delete_artifacts_in_group

        Deletes all artifacts in a group  # noqa: E501
        """
        pass

    def test_get_content_by_global_id(self):
        """Test case for get_content_by_global_id

        Get artifact by global ID  # noqa: E501
        """
        pass

    def test_get_content_by_hash(self):
        """Test case for get_content_by_hash

        Get artifact content by SHA-256 hash  # noqa: E501
        """
        pass

    def test_get_content_by_id(self):
        """Test case for get_content_by_id

        Get artifact content by ID  # noqa: E501
        """
        pass

    def test_get_latest_artifact(self):
        """Test case for get_latest_artifact

        Get latest artifact  # noqa: E501
        """
        pass

    def test_list_artifacts_in_group(self):
        """Test case for list_artifacts_in_group

        List artifacts in group  # noqa: E501
        """
        pass

    def test_references_by_content_hash(self):
        """Test case for references_by_content_hash

        Returns a list with all the references for the artifact with the given hash  # noqa: E501
        """
        pass

    def test_references_by_content_id(self):
        """Test case for references_by_content_id

        Returns a list with all the references for the artifact with the given content id.  # noqa: E501
        """
        pass

    def test_references_by_global_id(self):
        """Test case for references_by_global_id

        Returns a list with all the references for the artifact with the given global id.  # noqa: E501
        """
        pass

    def test_update_artifact(self):
        """Test case for update_artifact

        Update artifact  # noqa: E501
        """
        pass

    def test_update_artifact_state(self):
        """Test case for update_artifact_state

        Update artifact state  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
