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


class CustomerRoleFullRolePermissions(object):
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
        'create': 'bool',
        'delete': 'bool',
        'execute': 'bool',
        'read': 'bool',
        'update': 'bool'
    }

    attribute_map = {
        'create': 'create',
        'delete': 'delete',
        'execute': 'execute',
        'read': 'read',
        'update': 'update'
    }

    def __init__(self, create=None, delete=None, execute=None, read=None, update=None, _configuration=None):  # noqa: E501
        """CustomerRoleFullRolePermissions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create = None
        self._delete = None
        self._execute = None
        self._read = None
        self._update = None
        self.discriminator = None

        if create is not None:
            self.create = create
        if delete is not None:
            self.delete = delete
        if execute is not None:
            self.execute = execute
        if read is not None:
            self.read = read
        if update is not None:
            self.update = update

    @property
    def create(self):
        """Gets the create of this CustomerRoleFullRolePermissions.  # noqa: E501

        Create access. Allows to create resources.  # noqa: E501

        :return: The create of this CustomerRoleFullRolePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this CustomerRoleFullRolePermissions.

        Create access. Allows to create resources.  # noqa: E501

        :param create: The create of this CustomerRoleFullRolePermissions.  # noqa: E501
        :type: bool
        """

        self._create = create

    @property
    def delete(self):
        """Gets the delete of this CustomerRoleFullRolePermissions.  # noqa: E501

        Delete access. Allows to delete deployed resources.  # noqa: E501

        :return: The delete of this CustomerRoleFullRolePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this CustomerRoleFullRolePermissions.

        Delete access. Allows to delete deployed resources.  # noqa: E501

        :param delete: The delete of this CustomerRoleFullRolePermissions.  # noqa: E501
        :type: bool
        """

        self._delete = delete

    @property
    def execute(self):
        """Gets the execute of this CustomerRoleFullRolePermissions.  # noqa: E501

        Execute access. Allows to change the status of deployed resources.  # noqa: E501

        :return: The execute of this CustomerRoleFullRolePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._execute

    @execute.setter
    def execute(self, execute):
        """Sets the execute of this CustomerRoleFullRolePermissions.

        Execute access. Allows to change the status of deployed resources.  # noqa: E501

        :param execute: The execute of this CustomerRoleFullRolePermissions.  # noqa: E501
        :type: bool
        """

        self._execute = execute

    @property
    def read(self):
        """Gets the read of this CustomerRoleFullRolePermissions.  # noqa: E501

        Read access. Allows to inspect deployed resources.  # noqa: E501

        :return: The read of this CustomerRoleFullRolePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this CustomerRoleFullRolePermissions.

        Read access. Allows to inspect deployed resources.  # noqa: E501

        :param read: The read of this CustomerRoleFullRolePermissions.  # noqa: E501
        :type: bool
        """

        self._read = read

    @property
    def update(self):
        """Gets the update of this CustomerRoleFullRolePermissions.  # noqa: E501

        Update access. Allows to alter deployed resources.  # noqa: E501

        :return: The update of this CustomerRoleFullRolePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this CustomerRoleFullRolePermissions.

        Update access. Allows to alter deployed resources.  # noqa: E501

        :param update: The update of this CustomerRoleFullRolePermissions.  # noqa: E501
        :type: bool
        """

        self._update = update

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
        if issubclass(CustomerRoleFullRolePermissions, dict):
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
        if not isinstance(other, CustomerRoleFullRolePermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerRoleFullRolePermissions):
            return True

        return self.to_dict() != other.to_dict()
