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


class ResetObjectspaceModel(object):
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
        'secret_key': 'str',
        'access_key': 'str'
    }

    attribute_map = {
        'secret_key': 'secret_key',
        'access_key': 'access_key'
    }

    def __init__(self, secret_key=None, access_key=None, _configuration=None):  # noqa: E501
        """ResetObjectspaceModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._secret_key = None
        self._access_key = None
        self.discriminator = None

        if secret_key is not None:
            self.secret_key = secret_key
        if access_key is not None:
            self.access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this ResetObjectspaceModel.  # noqa: E501


        :return: The secret_key of this ResetObjectspaceModel.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this ResetObjectspaceModel.


        :param secret_key: The secret_key of this ResetObjectspaceModel.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def access_key(self):
        """Gets the access_key of this ResetObjectspaceModel.  # noqa: E501


        :return: The access_key of this ResetObjectspaceModel.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this ResetObjectspaceModel.


        :param access_key: The access_key of this ResetObjectspaceModel.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

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
        if issubclass(ResetObjectspaceModel, dict):
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
        if not isinstance(other, ResetObjectspaceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResetObjectspaceModel):
            return True

        return self.to_dict() != other.to_dict()