"""
    Kafka Instance API

    API for interacting with Kafka Instance. Includes Produce, Consume and Admin APIs  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.model.acl_binding import AclBinding
from rhoas_kafka_instance_sdk.model.acl_binding_list_page_all_of import AclBindingListPageAllOf
from rhoas_kafka_instance_sdk.model.list import List
globals()['AclBinding'] = AclBinding
globals()['AclBindingListPageAllOf'] = AclBindingListPageAllOf
globals()['List'] = List
from rhoas_kafka_instance_sdk.model.acl_binding_list_page import AclBindingListPage


class TestAclBindingListPage(unittest.TestCase):
    """AclBindingListPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAclBindingListPage(self):
        """Test AclBindingListPage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AclBindingListPage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
