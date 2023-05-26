# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import slurmrestapi
from slurmrestapi.paths.openapi_v3 import get  # noqa: E501
from slurmrestapi import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOpenapiV3(ApiTestMixin, unittest.TestCase):
    """
    OpenapiV3 unit test stubs
        Retrieve OpenAPI Specification  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
