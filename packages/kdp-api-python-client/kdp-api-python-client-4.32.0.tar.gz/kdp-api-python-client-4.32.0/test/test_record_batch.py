"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces  # noqa: E501

    The version of the OpenAPI document: 4.32.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kdp_api
from kdp_api.model.json_record import JsonRecord
globals()['JsonRecord'] = JsonRecord
from kdp_api.model.record_batch import RecordBatch


class TestRecordBatch(unittest.TestCase):
    """RecordBatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRecordBatch(self):
        """Test RecordBatch"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RecordBatch()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
