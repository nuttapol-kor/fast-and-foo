# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TrafficReport(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, date=None, time=None, traffic_status=None):  # noqa: E501
        """TrafficReport - a model defined in OpenAPI

        :param date: The date of this TrafficReport.  # noqa: E501
        :type date: str
        :param time: The time of this TrafficReport.  # noqa: E501
        :type time: str
        :param traffic_status: The traffic_status of this TrafficReport.  # noqa: E501
        :type traffic_status: str
        """
        self.openapi_types = {
            'date': str,
            'time': str,
            'traffic_status': str
        }

        self.attribute_map = {
            'date': 'date',
            'time': 'time',
            'traffic_status': 'trafficStatus'
        }

        self._date = date
        self._time = time
        self._traffic_status = traffic_status

    @classmethod
    def from_dict(cls, dikt) -> 'TrafficReport':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TrafficReport of this TrafficReport.  # noqa: E501
        :rtype: TrafficReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def date(self):
        """Gets the date of this TrafficReport.


        :return: The date of this TrafficReport.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TrafficReport.


        :param date: The date of this TrafficReport.
        :type date: str
        """

        self._date = date

    @property
    def time(self):
        """Gets the time of this TrafficReport.


        :return: The time of this TrafficReport.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TrafficReport.


        :param time: The time of this TrafficReport.
        :type time: str
        """

        self._time = time

    @property
    def traffic_status(self):
        """Gets the traffic_status of this TrafficReport.


        :return: The traffic_status of this TrafficReport.
        :rtype: str
        """
        return self._traffic_status

    @traffic_status.setter
    def traffic_status(self, traffic_status):
        """Sets the traffic_status of this TrafficReport.


        :param traffic_status: The traffic_status of this TrafficReport.
        :type traffic_status: str
        """

        self._traffic_status = traffic_status
