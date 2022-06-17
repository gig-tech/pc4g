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


class VmsModelNetworkInterfaces(object):
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
        'device_name': 'str',
        'mac_address': 'str',
        'ip_address': 'str',
        'network_id': 'int'
    }

    attribute_map = {
        'device_name': 'device_name',
        'mac_address': 'mac_address',
        'ip_address': 'ip_address',
        'network_id': 'network_id'
    }

    def __init__(self, device_name=None, mac_address=None, ip_address=None, network_id=None, _configuration=None):  # noqa: E501
        """VmsModelNetworkInterfaces - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._device_name = None
        self._mac_address = None
        self._ip_address = None
        self._network_id = None
        self.discriminator = None

        if device_name is not None:
            self.device_name = device_name
        if mac_address is not None:
            self.mac_address = mac_address
        if ip_address is not None:
            self.ip_address = ip_address
        if network_id is not None:
            self.network_id = network_id

    @property
    def device_name(self):
        """Gets the device_name of this VmsModelNetworkInterfaces.  # noqa: E501


        :return: The device_name of this VmsModelNetworkInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this VmsModelNetworkInterfaces.


        :param device_name: The device_name of this VmsModelNetworkInterfaces.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def mac_address(self):
        """Gets the mac_address of this VmsModelNetworkInterfaces.  # noqa: E501


        :return: The mac_address of this VmsModelNetworkInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this VmsModelNetworkInterfaces.


        :param mac_address: The mac_address of this VmsModelNetworkInterfaces.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def ip_address(self):
        """Gets the ip_address of this VmsModelNetworkInterfaces.  # noqa: E501


        :return: The ip_address of this VmsModelNetworkInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this VmsModelNetworkInterfaces.


        :param ip_address: The ip_address of this VmsModelNetworkInterfaces.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def network_id(self):
        """Gets the network_id of this VmsModelNetworkInterfaces.  # noqa: E501


        :return: The network_id of this VmsModelNetworkInterfaces.  # noqa: E501
        :rtype: int
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this VmsModelNetworkInterfaces.


        :param network_id: The network_id of this VmsModelNetworkInterfaces.  # noqa: E501
        :type: int
        """

        self._network_id = network_id

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
        if issubclass(VmsModelNetworkInterfaces, dict):
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
        if not isinstance(other, VmsModelNetworkInterfaces):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmsModelNetworkInterfaces):
            return True

        return self.to_dict() != other.to_dict()