"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces  # noqa: E501

    The version of the OpenAPI document: 4.32.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kdp_api
from kdp_api.model.stripe_latest_charge import StripeLatestCharge
globals()['StripeLatestCharge'] = StripeLatestCharge
from kdp_api.model.user_patch_request import UserPatchRequest


class TestUserPatchRequest(unittest.TestCase):
    """UserPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserPatchRequest(self):
        """Test UserPatchRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserPatchRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
