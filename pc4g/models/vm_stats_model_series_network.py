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


class VmStatsModelSeriesNetwork(object):
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
        'nic_mac': 'str',
        'usage': 'VmStatsModelSeriesNetworkUsage'
    }

    attribute_map = {
        'nic_mac': 'nic_mac',
        'usage': 'usage'
    }

    def __init__(self, nic_mac=None, usage=None, _configuration=None):  # noqa: E501
        """VmStatsModelSeriesNetwork - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._nic_mac = None
        self._usage = None
        self.discriminator = None

        if nic_mac is not None:
            self.nic_mac = nic_mac
        if usage is not None:
            self.usage = usage

    @property
    def nic_mac(self):
        """Gets the nic_mac of this VmStatsModelSeriesNetwork.  # noqa: E501


        :return: The nic_mac of this VmStatsModelSeriesNetwork.  # noqa: E501
        :rtype: str
        """
        return self._nic_mac

    @nic_mac.setter
    def nic_mac(self, nic_mac):
        """Sets the nic_mac of this VmStatsModelSeriesNetwork.


        :param nic_mac: The nic_mac of this VmStatsModelSeriesNetwork.  # noqa: E501
        :type: str
        """

        self._nic_mac = nic_mac

    @property
    def usage(self):
        """Gets the usage of this VmStatsModelSeriesNetwork.  # noqa: E501


        :return: The usage of this VmStatsModelSeriesNetwork.  # noqa: E501
        :rtype: VmStatsModelSeriesNetworkUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this VmStatsModelSeriesNetwork.


        :param usage: The usage of this VmStatsModelSeriesNetwork.  # noqa: E501
        :type: VmStatsModelSeriesNetworkUsage
        """

        self._usage = usage

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
        if issubclass(VmStatsModelSeriesNetwork, dict):
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
        if not isinstance(other, VmStatsModelSeriesNetwork):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmStatsModelSeriesNetwork):
            return True

        return self.to_dict() != other.to_dict()