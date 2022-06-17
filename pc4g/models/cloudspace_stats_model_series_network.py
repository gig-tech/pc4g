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


class CloudspaceStatsModelSeriesNetwork(object):
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
        'vms': 'CloudspaceStatsModelSeriesNetworkVms',
        'gateways': 'CloudspaceStatsModelSeriesNetworkGateways'
    }

    attribute_map = {
        'vms': 'vms',
        'gateways': 'gateways'
    }

    def __init__(self, vms=None, gateways=None, _configuration=None):  # noqa: E501
        """CloudspaceStatsModelSeriesNetwork - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vms = None
        self._gateways = None
        self.discriminator = None

        if vms is not None:
            self.vms = vms
        if gateways is not None:
            self.gateways = gateways

    @property
    def vms(self):
        """Gets the vms of this CloudspaceStatsModelSeriesNetwork.  # noqa: E501


        :return: The vms of this CloudspaceStatsModelSeriesNetwork.  # noqa: E501
        :rtype: CloudspaceStatsModelSeriesNetworkVms
        """
        return self._vms

    @vms.setter
    def vms(self, vms):
        """Sets the vms of this CloudspaceStatsModelSeriesNetwork.


        :param vms: The vms of this CloudspaceStatsModelSeriesNetwork.  # noqa: E501
        :type: CloudspaceStatsModelSeriesNetworkVms
        """

        self._vms = vms

    @property
    def gateways(self):
        """Gets the gateways of this CloudspaceStatsModelSeriesNetwork.  # noqa: E501


        :return: The gateways of this CloudspaceStatsModelSeriesNetwork.  # noqa: E501
        :rtype: CloudspaceStatsModelSeriesNetworkGateways
        """
        return self._gateways

    @gateways.setter
    def gateways(self, gateways):
        """Sets the gateways of this CloudspaceStatsModelSeriesNetwork.


        :param gateways: The gateways of this CloudspaceStatsModelSeriesNetwork.  # noqa: E501
        :type: CloudspaceStatsModelSeriesNetworkGateways
        """

        self._gateways = gateways

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
        if issubclass(CloudspaceStatsModelSeriesNetwork, dict):
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
        if not isinstance(other, CloudspaceStatsModelSeriesNetwork):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudspaceStatsModelSeriesNetwork):
            return True

        return self.to_dict() != other.to_dict()