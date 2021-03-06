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


class CustomerRoleFull(object):
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
        'description': 'str',
        'iam_organization': 'str',
        'name': 'str',
        'permissions': 'object',
        'role_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'iam_organization': 'iam_organization',
        'name': 'name',
        'permissions': 'permissions',
        'role_id': 'role_id'
    }

    def __init__(self, description=None, iam_organization=None, name=None, permissions=None, role_id=None, _configuration=None):  # noqa: E501
        """CustomerRoleFull - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._iam_organization = None
        self._name = None
        self._permissions = None
        self._role_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if iam_organization is not None:
            self.iam_organization = iam_organization
        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions
        if role_id is not None:
            self.role_id = role_id

    @property
    def description(self):
        """Gets the description of this CustomerRoleFull.  # noqa: E501

        Role description  # noqa: E501

        :return: The description of this CustomerRoleFull.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomerRoleFull.

        Role description  # noqa: E501

        :param description: The description of this CustomerRoleFull.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def iam_organization(self):
        """Gets the iam_organization of this CustomerRoleFull.  # noqa: E501

        Organization in IAM that defines to whom the role is granted  # noqa: E501

        :return: The iam_organization of this CustomerRoleFull.  # noqa: E501
        :rtype: str
        """
        return self._iam_organization

    @iam_organization.setter
    def iam_organization(self, iam_organization):
        """Sets the iam_organization of this CustomerRoleFull.

        Organization in IAM that defines to whom the role is granted  # noqa: E501

        :param iam_organization: The iam_organization of this CustomerRoleFull.  # noqa: E501
        :type: str
        """

        self._iam_organization = iam_organization

    @property
    def name(self):
        """Gets the name of this CustomerRoleFull.  # noqa: E501

        Role name  # noqa: E501

        :return: The name of this CustomerRoleFull.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerRoleFull.

        Role name  # noqa: E501

        :param name: The name of this CustomerRoleFull.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this CustomerRoleFull.  # noqa: E501

        None  # noqa: E501

        :return: The permissions of this CustomerRoleFull.  # noqa: E501
        :rtype: object
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this CustomerRoleFull.

        None  # noqa: E501

        :param permissions: The permissions of this CustomerRoleFull.  # noqa: E501
        :type: object
        """

        self._permissions = permissions

    @property
    def role_id(self):
        """Gets the role_id of this CustomerRoleFull.  # noqa: E501

        Unique role id  # noqa: E501

        :return: The role_id of this CustomerRoleFull.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this CustomerRoleFull.

        Unique role id  # noqa: E501

        :param role_id: The role_id of this CustomerRoleFull.  # noqa: E501
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
        if issubclass(CustomerRoleFull, dict):
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
        if not isinstance(other, CustomerRoleFull):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerRoleFull):
            return True

        return self.to_dict() != other.to_dict()
