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


class ReverseProxyBackEndHealthCheck(object):
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
        'path': 'str',
        'scheme': 'str',
        'port': 'int',
        'interval': 'int',
        'timeout': 'int'
    }

    attribute_map = {
        'path': 'path',
        'scheme': 'scheme',
        'port': 'port',
        'interval': 'interval',
        'timeout': 'timeout'
    }

    def __init__(self, path=None, scheme=None, port=None, interval=None, timeout=None, _configuration=None):  # noqa: E501
        """ReverseProxyBackEndHealthCheck - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._path = None
        self._scheme = None
        self._port = None
        self._interval = None
        self._timeout = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if scheme is not None:
            self.scheme = scheme
        if port is not None:
            self.port = port
        if interval is not None:
            self.interval = interval
        if timeout is not None:
            self.timeout = timeout

    @property
    def path(self):
        """Gets the path of this ReverseProxyBackEndHealthCheck.  # noqa: E501

        path of the health check route  # noqa: E501

        :return: The path of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ReverseProxyBackEndHealthCheck.

        path of the health check route  # noqa: E501

        :param path: The path of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def scheme(self):
        """Gets the scheme of this ReverseProxyBackEndHealthCheck.  # noqa: E501

        http scheme for the health check route  # noqa: E501

        :return: The scheme of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this ReverseProxyBackEndHealthCheck.

        http scheme for the health check route  # noqa: E501

        :param scheme: The scheme of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :type: str
        """

        self._scheme = scheme

    @property
    def port(self):
        """Gets the port of this ReverseProxyBackEndHealthCheck.  # noqa: E501

        Port used in health checking  # noqa: E501

        :return: The port of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ReverseProxyBackEndHealthCheck.

        Port used in health checking  # noqa: E501

        :param port: The port of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def interval(self):
        """Gets the interval of this ReverseProxyBackEndHealthCheck.  # noqa: E501

        Interval between health checking requests  # noqa: E501

        :return: The interval of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ReverseProxyBackEndHealthCheck.

        Interval between health checking requests  # noqa: E501

        :param interval: The interval of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def timeout(self):
        """Gets the timeout of this ReverseProxyBackEndHealthCheck.  # noqa: E501

        Timeout of a health checkint request  # noqa: E501

        :return: The timeout of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ReverseProxyBackEndHealthCheck.

        Timeout of a health checkint request  # noqa: E501

        :param timeout: The timeout of this ReverseProxyBackEndHealthCheck.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if issubclass(ReverseProxyBackEndHealthCheck, dict):
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
        if not isinstance(other, ReverseProxyBackEndHealthCheck):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReverseProxyBackEndHealthCheck):
            return True

        return self.to_dict() != other.to_dict()
