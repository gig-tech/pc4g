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


class GetBucketModel(object):
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
        'limit': 'int',
        'deleted': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'limit': 'limit',
        'deleted': 'deleted'
    }

    def __init__(self, name=None, limit=None, deleted=None, _configuration=None):  # noqa: E501
        """GetBucketModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._limit = None
        self._deleted = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if deleted is not None:
            self.deleted = deleted

    @property
    def name(self):
        """Gets the name of this GetBucketModel.  # noqa: E501


        :return: The name of this GetBucketModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetBucketModel.


        :param name: The name of this GetBucketModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def limit(self):
        """Gets the limit of this GetBucketModel.  # noqa: E501


        :return: The limit of this GetBucketModel.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetBucketModel.


        :param limit: The limit of this GetBucketModel.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def deleted(self):
        """Gets the deleted of this GetBucketModel.  # noqa: E501


        :return: The deleted of this GetBucketModel.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this GetBucketModel.


        :param deleted: The deleted of this GetBucketModel.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

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
        if issubclass(GetBucketModel, dict):
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
        if not isinstance(other, GetBucketModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetBucketModel):
            return True

        return self.to_dict() != other.to_dict()
