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


class CloudspaceConsumptionModelCloudspace(object):
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
        'consumption': 'CloudspaceConsumptionModelCloudspaceConsumption',
        'vms': 'list[CloudspaceConsumptionModelCloudspaceVms]'
    }

    attribute_map = {
        'consumption': 'consumption',
        'vms': 'vms'
    }

    def __init__(self, consumption=None, vms=None, _configuration=None):  # noqa: E501
        """CloudspaceConsumptionModelCloudspace - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._consumption = None
        self._vms = None
        self.discriminator = None

        if consumption is not None:
            self.consumption = consumption
        if vms is not None:
            self.vms = vms

    @property
    def consumption(self):
        """Gets the consumption of this CloudspaceConsumptionModelCloudspace.  # noqa: E501


        :return: The consumption of this CloudspaceConsumptionModelCloudspace.  # noqa: E501
        :rtype: CloudspaceConsumptionModelCloudspaceConsumption
        """
        return self._consumption

    @consumption.setter
    def consumption(self, consumption):
        """Sets the consumption of this CloudspaceConsumptionModelCloudspace.


        :param consumption: The consumption of this CloudspaceConsumptionModelCloudspace.  # noqa: E501
        :type: CloudspaceConsumptionModelCloudspaceConsumption
        """

        self._consumption = consumption

    @property
    def vms(self):
        """Gets the vms of this CloudspaceConsumptionModelCloudspace.  # noqa: E501


        :return: The vms of this CloudspaceConsumptionModelCloudspace.  # noqa: E501
        :rtype: list[CloudspaceConsumptionModelCloudspaceVms]
        """
        return self._vms

    @vms.setter
    def vms(self, vms):
        """Sets the vms of this CloudspaceConsumptionModelCloudspace.


        :param vms: The vms of this CloudspaceConsumptionModelCloudspace.  # noqa: E501
        :type: list[CloudspaceConsumptionModelCloudspaceVms]
        """

        self._vms = vms

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
        if issubclass(CloudspaceConsumptionModelCloudspace, dict):
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
        if not isinstance(other, CloudspaceConsumptionModelCloudspace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudspaceConsumptionModelCloudspace):
            return True

        return self.to_dict() != other.to_dict()
