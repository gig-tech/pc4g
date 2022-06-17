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


class ServerPool(object):
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
        'serverpool_id': 'str',
        'name': 'str',
        'description': 'str',
        'hosts': 'list[ServerPoolHost]'
    }

    attribute_map = {
        'serverpool_id': 'serverpool_id',
        'name': 'name',
        'description': 'description',
        'hosts': 'hosts'
    }

    def __init__(self, serverpool_id=None, name=None, description=None, hosts=None, _configuration=None):  # noqa: E501
        """ServerPool - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._serverpool_id = None
        self._name = None
        self._description = None
        self._hosts = None
        self.discriminator = None

        if serverpool_id is not None:
            self.serverpool_id = serverpool_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if hosts is not None:
            self.hosts = hosts

    @property
    def serverpool_id(self):
        """Gets the serverpool_id of this ServerPool.  # noqa: E501

        ID of the server pool  # noqa: E501

        :return: The serverpool_id of this ServerPool.  # noqa: E501
        :rtype: str
        """
        return self._serverpool_id

    @serverpool_id.setter
    def serverpool_id(self, serverpool_id):
        """Sets the serverpool_id of this ServerPool.

        ID of the server pool  # noqa: E501

        :param serverpool_id: The serverpool_id of this ServerPool.  # noqa: E501
        :type: str
        """

        self._serverpool_id = serverpool_id

    @property
    def name(self):
        """Gets the name of this ServerPool.  # noqa: E501

        Name of the server pool  # noqa: E501

        :return: The name of this ServerPool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerPool.

        Name of the server pool  # noqa: E501

        :param name: The name of this ServerPool.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ServerPool.  # noqa: E501

        Description of the server pool  # noqa: E501

        :return: The description of this ServerPool.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServerPool.

        Description of the server pool  # noqa: E501

        :param description: The description of this ServerPool.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hosts(self):
        """Gets the hosts of this ServerPool.  # noqa: E501

        Hosts that are part of the server pool  # noqa: E501

        :return: The hosts of this ServerPool.  # noqa: E501
        :rtype: list[ServerPoolHost]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ServerPool.

        Hosts that are part of the server pool  # noqa: E501

        :param hosts: The hosts of this ServerPool.  # noqa: E501
        :type: list[ServerPoolHost]
        """

        self._hosts = hosts

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
        if issubclass(ServerPool, dict):
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
        if not isinstance(other, ServerPool):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerPool):
            return True

        return self.to_dict() != other.to_dict()