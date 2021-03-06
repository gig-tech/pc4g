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


class AddProxyInput(object):
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
        'config': 'AddProxyConfig',
        'certificates': 'object'
    }

    attribute_map = {
        'config': 'config',
        'certificates': 'certificates'
    }

    def __init__(self, config=None, certificates=None, _configuration=None):  # noqa: E501
        """AddProxyInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._config = None
        self._certificates = None
        self.discriminator = None

        self.config = config
        if certificates is not None:
            self.certificates = certificates

    @property
    def config(self):
        """Gets the config of this AddProxyInput.  # noqa: E501


        :return: The config of this AddProxyInput.  # noqa: E501
        :rtype: AddProxyConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this AddProxyInput.


        :param config: The config of this AddProxyInput.  # noqa: E501
        :type: AddProxyConfig
        """
        if self._configuration.client_side_validation and config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def certificates(self):
        """Gets the certificates of this AddProxyInput.  # noqa: E501


        :return: The certificates of this AddProxyInput.  # noqa: E501
        :rtype: object
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this AddProxyInput.


        :param certificates: The certificates of this AddProxyInput.  # noqa: E501
        :type: object
        """

        self._certificates = certificates

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
        if issubclass(AddProxyInput, dict):
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
        if not isinstance(other, AddProxyInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddProxyInput):
            return True

        return self.to_dict() != other.to_dict()
