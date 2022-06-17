# coding: utf-8

"""
    Python client for GIG based clouds (pc4g)

    RESTful api client to a GIG based cloud.  # noqa: E501

    OpenAPI spec version: v1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pc4g.configuration import Configuration


class VmStatsModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'time': 'list[int]',
        'series': 'VmStatsModelSeries'
    }

    attribute_map = {
        'time': 'time',
        'series': 'series'
    }

    def __init__(self, time=None, series=None, _configuration=None):  # noqa: E501
        """VmStatsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._time = None
        self._series = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if series is not None:
            self.series = series

    @property
    def time(self):
        """Gets the time of this VmStatsModel.  # noqa: E501


        :return: The time of this VmStatsModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this VmStatsModel.


        :param time: The time of this VmStatsModel.  # noqa: E501
        :type: list[int]
        """

        self._time = time

    @property
    def series(self):
        """Gets the series of this VmStatsModel.  # noqa: E501


        :return: The series of this VmStatsModel.  # noqa: E501
        :rtype: VmStatsModelSeries
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this VmStatsModel.


        :param series: The series of this VmStatsModel.  # noqa: E501
        :type: VmStatsModelSeries
        """

        self._series = series

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(VmStatsModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VmStatsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmStatsModel):
            return True

        return self.to_dict() != other.to_dict()
