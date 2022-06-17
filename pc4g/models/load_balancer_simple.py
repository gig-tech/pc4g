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


class LoadBalancerSimple(object):
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
        'loadbalancer_id': 'str',
        'name': 'str',
        'serverpool_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'loadbalancer_id': 'loadbalancer_id',
        'name': 'name',
        'serverpool_name': 'serverpool_name',
        'type': 'type'
    }

    def __init__(self, loadbalancer_id=None, name=None, serverpool_name=None, type=None, _configuration=None):  # noqa: E501
        """LoadBalancerSimple - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._loadbalancer_id = None
        self._name = None
        self._serverpool_name = None
        self._type = None
        self.discriminator = None

        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if name is not None:
            self.name = name
        if serverpool_name is not None:
            self.serverpool_name = serverpool_name
        if type is not None:
            self.type = type

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this LoadBalancerSimple.  # noqa: E501

        Load balancer ID  # noqa: E501

        :return: The loadbalancer_id of this LoadBalancerSimple.  # noqa: E501
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this LoadBalancerSimple.

        Load balancer ID  # noqa: E501

        :param loadbalancer_id: The loadbalancer_id of this LoadBalancerSimple.  # noqa: E501
        :type: str
        """

        self._loadbalancer_id = loadbalancer_id

    @property
    def name(self):
        """Gets the name of this LoadBalancerSimple.  # noqa: E501

        Load balancer Name  # noqa: E501

        :return: The name of this LoadBalancerSimple.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancerSimple.

        Load balancer Name  # noqa: E501

        :param name: The name of this LoadBalancerSimple.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def serverpool_name(self):
        """Gets the serverpool_name of this LoadBalancerSimple.  # noqa: E501

        Name of the server pool used by the load balancer  # noqa: E501

        :return: The serverpool_name of this LoadBalancerSimple.  # noqa: E501
        :rtype: str
        """
        return self._serverpool_name

    @serverpool_name.setter
    def serverpool_name(self, serverpool_name):
        """Sets the serverpool_name of this LoadBalancerSimple.

        Name of the server pool used by the load balancer  # noqa: E501

        :param serverpool_name: The serverpool_name of this LoadBalancerSimple.  # noqa: E501
        :type: str
        """

        self._serverpool_name = serverpool_name

    @property
    def type(self):
        """Gets the type of this LoadBalancerSimple.  # noqa: E501

        Type of the load balancer [TCP, UDP]  # noqa: E501

        :return: The type of this LoadBalancerSimple.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LoadBalancerSimple.

        Type of the load balancer [TCP, UDP]  # noqa: E501

        :param type: The type of this LoadBalancerSimple.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(LoadBalancerSimple, dict):
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
        if not isinstance(other, LoadBalancerSimple):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoadBalancerSimple):
            return True

        return self.to_dict() != other.to_dict()