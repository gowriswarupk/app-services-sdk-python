"""
    Kafka Instance API

    API for interacting with Kafka Instance. Includes Produce, Consume and Admin APIs  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.model.topic_settings import TopicSettings
globals()['TopicSettings'] = TopicSettings
from rhoas_kafka_instance_sdk.model.new_topic_input import NewTopicInput


class TestNewTopicInput(unittest.TestCase):
    """NewTopicInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNewTopicInput(self):
        """Test NewTopicInput"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NewTopicInput()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
