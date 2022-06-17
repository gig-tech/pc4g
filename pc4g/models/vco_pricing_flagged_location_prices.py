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


class VcoPricingFlaggedLocationPrices(object):
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
        'location': 'str',
        'resources': 'object'
    }

    attribute_map = {
        'location': 'location',
        'resources': 'resources'
    }

    def __init__(self, location=None, resources=None, _configuration=None):  # noqa: E501
        """VcoPricingFlaggedLocationPrices - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._location = None
        self._resources = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if resources is not None:
            self.resources = resources

    @property
    def location(self):
        """Gets the location of this VcoPricingFlaggedLocationPrices.  # noqa: E501

        Location name (G8 Name)  # noqa: E501

        :return: The location of this VcoPricingFlaggedLocationPrices.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this VcoPricingFlaggedLocationPrices.

        Location name (G8 Name)  # noqa: E501

        :param location: The location of this VcoPricingFlaggedLocationPrices.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def resources(self):
        """Gets the resources of this VcoPricingFlaggedLocationPrices.  # noqa: E501

        Cost of each resource  # noqa: E501

        :return: The resources of this VcoPricingFlaggedLocationPrices.  # noqa: E501
        :rtype: object
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this VcoPricingFlaggedLocationPrices.

        Cost of each resource  # noqa: E501

        :param resources: The resources of this VcoPricingFlaggedLocationPrices.  # noqa: E501
        :type: object
        """

        self._resources = resources

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
        if issubclass(VcoPricingFlaggedLocationPrices, dict):
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
        if not isinstance(other, VcoPricingFlaggedLocationPrices):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VcoPricingFlaggedLocationPrices):
            return True

        return self.to_dict() != other.to_dict()
