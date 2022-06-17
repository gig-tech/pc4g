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


class ShowReverseProxyFull(object):
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
        'reverseproxy_id': 'str',
        'name': 'str',
        'description': 'str',
        'front_end': 'ReverseProxyFrontEnd',
        'back_end': 'ShowReverseProxyBackEnd'
    }

    attribute_map = {
        'reverseproxy_id': 'reverseproxy_id',
        'name': 'name',
        'description': 'description',
        'front_end': 'front_end',
        'back_end': 'back_end'
    }

    def __init__(self, reverseproxy_id=None, name=None, description=None, front_end=None, back_end=None, _configuration=None):  # noqa: E501
        """ShowReverseProxyFull - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._reverseproxy_id = None
        self._name = None
        self._description = None
        self._front_end = None
        self._back_end = None
        self.discriminator = None

        if reverseproxy_id is not None:
            self.reverseproxy_id = reverseproxy_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if front_end is not None:
            self.front_end = front_end
        if back_end is not None:
            self.back_end = back_end

    @property
    def reverseproxy_id(self):
        """Gets the reverseproxy_id of this ShowReverseProxyFull.  # noqa: E501

        ID of the reverse proxy  # noqa: E501

        :return: The reverseproxy_id of this ShowReverseProxyFull.  # noqa: E501
        :rtype: str
        """
        return self._reverseproxy_id

    @reverseproxy_id.setter
    def reverseproxy_id(self, reverseproxy_id):
        """Sets the reverseproxy_id of this ShowReverseProxyFull.

        ID of the reverse proxy  # noqa: E501

        :param reverseproxy_id: The reverseproxy_id of this ShowReverseProxyFull.  # noqa: E501
        :type: str
        """

        self._reverseproxy_id = reverseproxy_id

    @property
    def name(self):
        """Gets the name of this ShowReverseProxyFull.  # noqa: E501

        Name of the reverse proxy  # noqa: E501

        :return: The name of this ShowReverseProxyFull.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowReverseProxyFull.

        Name of the reverse proxy  # noqa: E501

        :param name: The name of this ShowReverseProxyFull.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowReverseProxyFull.  # noqa: E501

        description of the reverse proxy  # noqa: E501

        :return: The description of this ShowReverseProxyFull.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowReverseProxyFull.

        description of the reverse proxy  # noqa: E501

        :param description: The description of this ShowReverseProxyFull.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def front_end(self):
        """Gets the front_end of this ShowReverseProxyFull.  # noqa: E501


        :return: The front_end of this ShowReverseProxyFull.  # noqa: E501
        :rtype: ReverseProxyFrontEnd
        """
        return self._front_end

    @front_end.setter
    def front_end(self, front_end):
        """Sets the front_end of this ShowReverseProxyFull.


        :param front_end: The front_end of this ShowReverseProxyFull.  # noqa: E501
        :type: ReverseProxyFrontEnd
        """

        self._front_end = front_end

    @property
    def back_end(self):
        """Gets the back_end of this ShowReverseProxyFull.  # noqa: E501


        :return: The back_end of this ShowReverseProxyFull.  # noqa: E501
        :rtype: ShowReverseProxyBackEnd
        """
        return self._back_end

    @back_end.setter
    def back_end(self, back_end):
        """Sets the back_end of this ShowReverseProxyFull.


        :param back_end: The back_end of this ShowReverseProxyFull.  # noqa: E501
        :type: ShowReverseProxyBackEnd
        """

        self._back_end = back_end

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
        if issubclass(ShowReverseProxyFull, dict):
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
        if not isinstance(other, ShowReverseProxyFull):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShowReverseProxyFull):
            return True

        return self.to_dict() != other.to_dict()