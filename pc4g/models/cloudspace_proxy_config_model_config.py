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


class CloudspaceProxyConfigModelConfig(object):
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
        'static': 'object',
        'provider': 'object',
        'acme': 'str'
    }

    attribute_map = {
        'static': 'static',
        'provider': 'provider',
        'acme': 'acme'
    }

    def __init__(self, static=None, provider=None, acme=None, _configuration=None):  # noqa: E501
        """CloudspaceProxyConfigModelConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._static = None
        self._provider = None
        self._acme = None
        self.discriminator = None

        if static is not None:
            self.static = static
        if provider is not None:
            self.provider = provider
        if acme is not None:
            self.acme = acme

    @property
    def static(self):
        """Gets the static of this CloudspaceProxyConfigModelConfig.  # noqa: E501


        :return: The static of this CloudspaceProxyConfigModelConfig.  # noqa: E501
        :rtype: object
        """
        return self._static

    @static.setter
    def static(self, static):
        """Sets the static of this CloudspaceProxyConfigModelConfig.


        :param static: The static of this CloudspaceProxyConfigModelConfig.  # noqa: E501
        :type: object
        """

        self._static = static

    @property
    def provider(self):
        """Gets the provider of this CloudspaceProxyConfigModelConfig.  # noqa: E501


        :return: The provider of this CloudspaceProxyConfigModelConfig.  # noqa: E501
        :rtype: object
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CloudspaceProxyConfigModelConfig.


        :param provider: The provider of this CloudspaceProxyConfigModelConfig.  # noqa: E501
        :type: object
        """

        self._provider = provider

    @property
    def acme(self):
        """Gets the acme of this CloudspaceProxyConfigModelConfig.  # noqa: E501


        :return: The acme of this CloudspaceProxyConfigModelConfig.  # noqa: E501
        :rtype: str
        """
        return self._acme

    @acme.setter
    def acme(self, acme):
        """Sets the acme of this CloudspaceProxyConfigModelConfig.


        :param acme: The acme of this CloudspaceProxyConfigModelConfig.  # noqa: E501
        :type: str
        """

        self._acme = acme

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
        if issubclass(CloudspaceProxyConfigModelConfig, dict):
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
        if not isinstance(other, CloudspaceProxyConfigModelConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudspaceProxyConfigModelConfig):
            return True

        return self.to_dict() != other.to_dict()
