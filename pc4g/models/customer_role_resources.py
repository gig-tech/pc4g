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


class CustomerRoleResources(object):
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
        'locations': 'list[LocationStatus]',
        'result': 'list[CustomerRoleResource]'
    }

    attribute_map = {
        'locations': 'locations',
        'result': 'result'
    }

    def __init__(self, locations=None, result=None, _configuration=None):  # noqa: E501
        """CustomerRoleResources - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._locations = None
        self._result = None
        self.discriminator = None

        if locations is not None:
            self.locations = locations
        if result is not None:
            self.result = result

    @property
    def locations(self):
        """Gets the locations of this CustomerRoleResources.  # noqa: E501


        :return: The locations of this CustomerRoleResources.  # noqa: E501
        :rtype: list[LocationStatus]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this CustomerRoleResources.


        :param locations: The locations of this CustomerRoleResources.  # noqa: E501
        :type: list[LocationStatus]
        """

        self._locations = locations

    @property
    def result(self):
        """Gets the result of this CustomerRoleResources.  # noqa: E501


        :return: The result of this CustomerRoleResources.  # noqa: E501
        :rtype: list[CustomerRoleResource]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CustomerRoleResources.


        :param result: The result of this CustomerRoleResources.  # noqa: E501
        :type: list[CustomerRoleResource]
        """

        self._result = result

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
        if issubclass(CustomerRoleResources, dict):
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
        if not isinstance(other, CustomerRoleResources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerRoleResources):
            return True

        return self.to_dict() != other.to_dict()
