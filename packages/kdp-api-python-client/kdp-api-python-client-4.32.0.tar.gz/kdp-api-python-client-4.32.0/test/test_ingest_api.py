"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces  # noqa: E501

    The version of the OpenAPI document: 4.32.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import kdp_api
from kdp_api.api.ingest_api import IngestApi  # noqa: E501


class TestIngestApi(unittest.TestCase):
    """IngestApi unit test stubs"""

    def setUp(self):
        self.api = IngestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_ingest(self):
        """Test case for post_ingest

        Create an Ingest Job  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
