"""
    Kafka Management API

    Kafka Management API is a REST API to manage Kafka instances  # noqa: E501

    The version of the OpenAPI document: 1.11.0
    Contact: rhosak-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api.errors_api import ErrorsApi  # noqa: E501


class TestErrorsApi(unittest.TestCase):
    """ErrorsApi unit test stubs"""

    def setUp(self):
        self.api = ErrorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_error_by_id(self):
        """Test case for get_error_by_id

        """
        pass

    def test_get_errors(self):
        """Test case for get_errors

        """
        pass


if __name__ == '__main__':
    unittest.main()
