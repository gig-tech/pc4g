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


class ReverseProxyBackEndStickCookie(object):
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
        'secure': 'bool',
        'http_only': 'bool',
        'same_site': 'str'
    }

    attribute_map = {
        'name': 'name',
        'secure': 'secure',
        'http_only': 'http_only',
        'same_site': 'same_site'
    }

    def __init__(self, name=None, secure=None, http_only=None, same_site=None, _configuration=None):  # noqa: E501
        """ReverseProxyBackEndStickCookie - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._secure = None
        self._http_only = None
        self._same_site = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if secure is not None:
            self.secure = secure
        if http_only is not None:
            self.http_only = http_only
        if same_site is not None:
            self.same_site = same_site

    @property
    def name(self):
        """Gets the name of this ReverseProxyBackEndStickCookie.  # noqa: E501

        Name of reverse proxy stick cookie  # noqa: E501

        :return: The name of this ReverseProxyBackEndStickCookie.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReverseProxyBackEndStickCookie.

        Name of reverse proxy stick cookie  # noqa: E501

        :param name: The name of this ReverseProxyBackEndStickCookie.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def secure(self):
        """Gets the secure of this ReverseProxyBackEndStickCookie.  # noqa: E501

        Wether the cookie is secure  # noqa: E501

        :return: The secure of this ReverseProxyBackEndStickCookie.  # noqa: E501
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure):
        """Sets the secure of this ReverseProxyBackEndStickCookie.

        Wether the cookie is secure  # noqa: E501

        :param secure: The secure of this ReverseProxyBackEndStickCookie.  # noqa: E501
        :type: bool
        """

        self._secure = secure

    @property
    def http_only(self):
        """Gets the http_only of this ReverseProxyBackEndStickCookie.  # noqa: E501

        Whether the cookie is http only  # noqa: E501

        :return: The http_only of this ReverseProxyBackEndStickCookie.  # noqa: E501
        :rtype: bool
        """
        return self._http_only

    @http_only.setter
    def http_only(self, http_only):
        """Sets the http_only of this ReverseProxyBackEndStickCookie.

        Whether the cookie is http only  # noqa: E501

        :param http_only: The http_only of this ReverseProxyBackEndStickCookie.  # noqa: E501
        :type: bool
        """

        self._http_only = http_only

    @property
    def same_site(self):
        """Gets the same_site of this ReverseProxyBackEndStickCookie.  # noqa: E501

        Same site value for the stick cookie  # noqa: E501

        :return: The same_site of this ReverseProxyBackEndStickCookie.  # noqa: E501
        :rtype: str
        """
        return self._same_site

    @same_site.setter
    def same_site(self, same_site):
        """Sets the same_site of this ReverseProxyBackEndStickCookie.

        Same site value for the stick cookie  # noqa: E501

        :param same_site: The same_site of this ReverseProxyBackEndStickCookie.  # noqa: E501
        :type: str
        """

        self._same_site = same_site

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
        if issubclass(ReverseProxyBackEndStickCookie, dict):
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
        if not isinstance(other, ReverseProxyBackEndStickCookie):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReverseProxyBackEndStickCookie):
            return True

        return self.to_dict() != other.to_dict()
