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


class ReverseProxyBackEndOptions(object):
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
        'sticky_session_cookie': 'ReverseProxyBackEndStickCookie',
        'health_check': 'ReverseProxyBackEndHealthCheck'
    }

    attribute_map = {
        'sticky_session_cookie': 'sticky_session_cookie',
        'health_check': 'health_check'
    }

    def __init__(self, sticky_session_cookie=None, health_check=None, _configuration=None):  # noqa: E501
        """ReverseProxyBackEndOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sticky_session_cookie = None
        self._health_check = None
        self.discriminator = None

        if sticky_session_cookie is not None:
            self.sticky_session_cookie = sticky_session_cookie
        if health_check is not None:
            self.health_check = health_check

    @property
    def sticky_session_cookie(self):
        """Gets the sticky_session_cookie of this ReverseProxyBackEndOptions.  # noqa: E501


        :return: The sticky_session_cookie of this ReverseProxyBackEndOptions.  # noqa: E501
        :rtype: ReverseProxyBackEndStickCookie
        """
        return self._sticky_session_cookie

    @sticky_session_cookie.setter
    def sticky_session_cookie(self, sticky_session_cookie):
        """Sets the sticky_session_cookie of this ReverseProxyBackEndOptions.


        :param sticky_session_cookie: The sticky_session_cookie of this ReverseProxyBackEndOptions.  # noqa: E501
        :type: ReverseProxyBackEndStickCookie
        """

        self._sticky_session_cookie = sticky_session_cookie

    @property
    def health_check(self):
        """Gets the health_check of this ReverseProxyBackEndOptions.  # noqa: E501


        :return: The health_check of this ReverseProxyBackEndOptions.  # noqa: E501
        :rtype: ReverseProxyBackEndHealthCheck
        """
        return self._health_check

    @health_check.setter
    def health_check(self, health_check):
        """Sets the health_check of this ReverseProxyBackEndOptions.


        :param health_check: The health_check of this ReverseProxyBackEndOptions.  # noqa: E501
        :type: ReverseProxyBackEndHealthCheck
        """

        self._health_check = health_check

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
        if issubclass(ReverseProxyBackEndOptions, dict):
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
        if not isinstance(other, ReverseProxyBackEndOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReverseProxyBackEndOptions):
            return True

        return self.to_dict() != other.to_dict()
