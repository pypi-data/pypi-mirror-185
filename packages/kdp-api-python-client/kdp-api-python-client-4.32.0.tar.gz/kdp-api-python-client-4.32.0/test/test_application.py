"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces  # noqa: E501

    The version of the OpenAPI document: 4.32.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kdp_api
from kdp_api.model.application_required_dataset_access import ApplicationRequiredDatasetAccess
globals()['ApplicationRequiredDatasetAccess'] = ApplicationRequiredDatasetAccess
from kdp_api.model.application import Application


class TestApplication(unittest.TestCase):
    """Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplication(self):
        """Test Application"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Application()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
