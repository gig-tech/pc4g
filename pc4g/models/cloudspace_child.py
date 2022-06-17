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


class CloudspaceChild(object):
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
        'cloudspace_id': 'str',
        'ip_in_parent_network': 'str',
        'private_network': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cloudspace_id': 'cloudspace_id',
        'ip_in_parent_network': 'ip_in_parent_network',
        'private_network': 'private_network'
    }

    def __init__(self, name=None, cloudspace_id=None, ip_in_parent_network=None, private_network=None, _configuration=None):  # noqa: E501
        """CloudspaceChild - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._cloudspace_id = None
        self._ip_in_parent_network = None
        self._private_network = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cloudspace_id is not None:
            self.cloudspace_id = cloudspace_id
        if ip_in_parent_network is not None:
            self.ip_in_parent_network = ip_in_parent_network
        if private_network is not None:
            self.private_network = private_network

    @property
    def name(self):
        """Gets the name of this CloudspaceChild.  # noqa: E501

        CLoudspace name  # noqa: E501

        :return: The name of this CloudspaceChild.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudspaceChild.

        CLoudspace name  # noqa: E501

        :param name: The name of this CloudspaceChild.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cloudspace_id(self):
        """Gets the cloudspace_id of this CloudspaceChild.  # noqa: E501

        CLoudspace ID  # noqa: E501

        :return: The cloudspace_id of this CloudspaceChild.  # noqa: E501
        :rtype: str
        """
        return self._cloudspace_id

    @cloudspace_id.setter
    def cloudspace_id(self, cloudspace_id):
        """Sets the cloudspace_id of this CloudspaceChild.

        CLoudspace ID  # noqa: E501

        :param cloudspace_id: The cloudspace_id of this CloudspaceChild.  # noqa: E501
        :type: str
        """

        self._cloudspace_id = cloudspace_id

    @property
    def ip_in_parent_network(self):
        """Gets the ip_in_parent_network of this CloudspaceChild.  # noqa: E501

        Cloudspace IP address in the parent network  # noqa: E501

        :return: The ip_in_parent_network of this CloudspaceChild.  # noqa: E501
        :rtype: str
        """
        return self._ip_in_parent_network

    @ip_in_parent_network.setter
    def ip_in_parent_network(self, ip_in_parent_network):
        """Sets the ip_in_parent_network of this CloudspaceChild.

        Cloudspace IP address in the parent network  # noqa: E501

        :param ip_in_parent_network: The ip_in_parent_network of this CloudspaceChild.  # noqa: E501
        :type: str
        """

        self._ip_in_parent_network = ip_in_parent_network

    @property
    def private_network(self):
        """Gets the private_network of this CloudspaceChild.  # noqa: E501

        Cloudspace private network  # noqa: E501

        :return: The private_network of this CloudspaceChild.  # noqa: E501
        :rtype: str
        """
        return self._private_network

    @private_network.setter
    def private_network(self, private_network):
        """Sets the private_network of this CloudspaceChild.

        Cloudspace private network  # noqa: E501

        :param private_network: The private_network of this CloudspaceChild.  # noqa: E501
        :type: str
        """

        self._private_network = private_network

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
        if issubclass(CloudspaceChild, dict):
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
        if not isinstance(other, CloudspaceChild):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudspaceChild):
            return True

        return self.to_dict() != other.to_dict()
