"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces  # noqa: E501

    The version of the OpenAPI document: 4.32.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kdp_api
from kdp_api.model.job_list import JobList
globals()['JobList'] = JobList
from kdp_api.model.job_paginator import JobPaginator


class TestJobPaginator(unittest.TestCase):
    """JobPaginator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobPaginator(self):
        """Test JobPaginator"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobPaginator()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
