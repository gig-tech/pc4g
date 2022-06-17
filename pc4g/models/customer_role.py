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


class CustomerRole(object):
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
        'name': 'str',
        'permissions': 'object',
        'role_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'permissions': 'permissions',
        'role_id': 'role_id'
    }

    def __init__(self, name=None, permissions=None, role_id=None, _configuration=None):  # noqa: E501
        """CustomerRole - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._permissions = None
        self._role_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions
        if role_id is not None:
            self.role_id = role_id

    @property
    def name(self):
        """Gets the name of this CustomerRole.  # noqa: E501

        Role name  # noqa: E501

        :return: The name of this CustomerRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerRole.

        Role name  # noqa: E501

        :param name: The name of this CustomerRole.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this CustomerRole.  # noqa: E501

        None  # noqa: E501

        :return: The permissions of this CustomerRole.  # noqa: E501
        :rtype: object
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this CustomerRole.

        None  # noqa: E501

        :param permissions: The permissions of this CustomerRole.  # noqa: E501
        :type: object
        """

        self._permissions = permissions

    @property
    def role_id(self):
        """Gets the role_id of this CustomerRole.  # noqa: E501

        Unique role id  # noqa: E501

        :return: The role_id of this CustomerRole.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this CustomerRole.

        Unique role id  # noqa: E501

        :param role_id: The role_id of this CustomerRole.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

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
        if issubclass(CustomerRole, dict):
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
        if not isinstance(other, CustomerRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerRole):
            return True

        return self.to_dict() != other.to_dict()