# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.speed import Speed  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_specific_humidity(self):
        """Test case for controller_get_specific_humidity

        JeeJee
        """
        headers = { 
        }
        response = self.client.open(
            '/speed/v1/tmd/{speed_id}/humidity'.format(speed_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_specific_pm25(self):
        """Test case for controller_get_specific_pm25

        JeeJee
        """
        headers = { 
        }
        response = self.client.open(
            '/speed/v1/pm25/{speed_id}'.format(speed_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_specific_rainfall(self):
        """Test case for controller_get_specific_rainfall

        JeeJee
        """
        headers = { 
        }
        response = self.client.open(
            '/speed/v1/tmd/{speed_id}/rainfall'.format(speed_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_specific_speed(self):
        """Test case for controller_get_specific_speed

        JeeJee
        """
        headers = { 
        }
        response = self.client.open(
            '/speed/v1/speeds/{speed_id}'.format(speed_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_specific_temperature(self):
        """Test case for controller_get_specific_temperature

        JeeJee
        """
        headers = { 
        }
        response = self.client.open(
            '/speed/v1/tmd/{speed_id}/temperature'.format(speed_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_speeds(self):
        """Test case for controller_get_speeds

        Returns a list speed data
        """
        headers = { 
        }
        response = self.client.open(
            '/speed/v1/speeds',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
