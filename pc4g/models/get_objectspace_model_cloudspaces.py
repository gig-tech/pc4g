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


class GetObjectspaceModelCloudspaces(object):
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
        'ip_address': 'str',
        'external_ip_address': 'str',
        'status': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cloudspace_id': 'cloudspace_id',
        'ip_address': 'ip_address',
        'external_ip_address': 'external_ip_address',
        'status': 'status',
        'mode': 'mode'
    }

    def __init__(self, name=None, cloudspace_id=None, ip_address=None, external_ip_address=None, status=None, mode=None, _configuration=None):  # noqa: E501
        """GetObjectspaceModelCloudspaces - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._cloudspace_id = None
        self._ip_address = None
        self._external_ip_address = None
        self._status = None
        self._mode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cloudspace_id is not None:
            self.cloudspace_id = cloudspace_id
        if ip_address is not None:
            self.ip_address = ip_address
        if external_ip_address is not None:
            self.external_ip_address = external_ip_address
        if status is not None:
            self.status = status
        if mode is not None:
            self.mode = mode

    @property
    def name(self):
        """Gets the name of this GetObjectspaceModelCloudspaces.  # noqa: E501


        :return: The name of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetObjectspaceModelCloudspaces.


        :param name: The name of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cloudspace_id(self):
        """Gets the cloudspace_id of this GetObjectspaceModelCloudspaces.  # noqa: E501


        :return: The cloudspace_id of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :rtype: str
        """
        return self._cloudspace_id

    @cloudspace_id.setter
    def cloudspace_id(self, cloudspace_id):
        """Sets the cloudspace_id of this GetObjectspaceModelCloudspaces.


        :param cloudspace_id: The cloudspace_id of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :type: str
        """

        self._cloudspace_id = cloudspace_id

    @property
    def ip_address(self):
        """Gets the ip_address of this GetObjectspaceModelCloudspaces.  # noqa: E501


        :return: The ip_address of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this GetObjectspaceModelCloudspaces.


        :param ip_address: The ip_address of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def external_ip_address(self):
        """Gets the external_ip_address of this GetObjectspaceModelCloudspaces.  # noqa: E501


        :return: The external_ip_address of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :rtype: str
        """
        return self._external_ip_address

    @external_ip_address.setter
    def external_ip_address(self, external_ip_address):
        """Sets the external_ip_address of this GetObjectspaceModelCloudspaces.


        :param external_ip_address: The external_ip_address of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :type: str
        """

        self._external_ip_address = external_ip_address

    @property
    def status(self):
        """Gets the status of this GetObjectspaceModelCloudspaces.  # noqa: E501


        :return: The status of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetObjectspaceModelCloudspaces.


        :param status: The status of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def mode(self):
        """Gets the mode of this GetObjectspaceModelCloudspaces.  # noqa: E501


        :return: The mode of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this GetObjectspaceModelCloudspaces.


        :param mode: The mode of this GetObjectspaceModelCloudspaces.  # noqa: E501
        :type: str
        """

        self._mode = mode

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
        if issubclass(GetObjectspaceModelCloudspaces, dict):
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
        if not isinstance(other, GetObjectspaceModelCloudspaces):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetObjectspaceModelCloudspaces):
            return True

        return self.to_dict() != other.to_dict()
