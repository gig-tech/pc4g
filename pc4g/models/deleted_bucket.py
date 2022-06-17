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


class DeletedBucket(object):
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
        'bucket_name': 'str',
        'objectspace_name': 'str',
        'objectspace_id': 'str',
        'objectspace_status': 'str',
        'location': 'str',
        'deletion_time': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'objectspace_name': 'objectspace_name',
        'objectspace_id': 'objectspace_id',
        'objectspace_status': 'objectspace_status',
        'location': 'location',
        'deletion_time': 'deletion_time'
    }

    def __init__(self, bucket_name=None, objectspace_name=None, objectspace_id=None, objectspace_status=None, location=None, deletion_time=None, _configuration=None):  # noqa: E501
        """DeletedBucket - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_name = None
        self._objectspace_name = None
        self._objectspace_id = None
        self._objectspace_status = None
        self._location = None
        self._deletion_time = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if objectspace_name is not None:
            self.objectspace_name = objectspace_name
        if objectspace_id is not None:
            self.objectspace_id = objectspace_id
        if objectspace_status is not None:
            self.objectspace_status = objectspace_status
        if location is not None:
            self.location = location
        if deletion_time is not None:
            self.deletion_time = deletion_time

    @property
    def bucket_name(self):
        """Gets the bucket_name of this DeletedBucket.  # noqa: E501

        Bucket name  # noqa: E501

        :return: The bucket_name of this DeletedBucket.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this DeletedBucket.

        Bucket name  # noqa: E501

        :param bucket_name: The bucket_name of this DeletedBucket.  # noqa: E501
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def objectspace_name(self):
        """Gets the objectspace_name of this DeletedBucket.  # noqa: E501

        Objectspace name  # noqa: E501

        :return: The objectspace_name of this DeletedBucket.  # noqa: E501
        :rtype: str
        """
        return self._objectspace_name

    @objectspace_name.setter
    def objectspace_name(self, objectspace_name):
        """Sets the objectspace_name of this DeletedBucket.

        Objectspace name  # noqa: E501

        :param objectspace_name: The objectspace_name of this DeletedBucket.  # noqa: E501
        :type: str
        """

        self._objectspace_name = objectspace_name

    @property
    def objectspace_id(self):
        """Gets the objectspace_id of this DeletedBucket.  # noqa: E501

        Objectspace id  # noqa: E501

        :return: The objectspace_id of this DeletedBucket.  # noqa: E501
        :rtype: str
        """
        return self._objectspace_id

    @objectspace_id.setter
    def objectspace_id(self, objectspace_id):
        """Sets the objectspace_id of this DeletedBucket.

        Objectspace id  # noqa: E501

        :param objectspace_id: The objectspace_id of this DeletedBucket.  # noqa: E501
        :type: str
        """

        self._objectspace_id = objectspace_id

    @property
    def objectspace_status(self):
        """Gets the objectspace_status of this DeletedBucket.  # noqa: E501

        Objectspace status  # noqa: E501

        :return: The objectspace_status of this DeletedBucket.  # noqa: E501
        :rtype: str
        """
        return self._objectspace_status

    @objectspace_status.setter
    def objectspace_status(self, objectspace_status):
        """Sets the objectspace_status of this DeletedBucket.

        Objectspace status  # noqa: E501

        :param objectspace_status: The objectspace_status of this DeletedBucket.  # noqa: E501
        :type: str
        """

        self._objectspace_status = objectspace_status

    @property
    def location(self):
        """Gets the location of this DeletedBucket.  # noqa: E501

        Bucket location  # noqa: E501

        :return: The location of this DeletedBucket.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DeletedBucket.

        Bucket location  # noqa: E501

        :param location: The location of this DeletedBucket.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def deletion_time(self):
        """Gets the deletion_time of this DeletedBucket.  # noqa: E501

        Bucket deletion time  # noqa: E501

        :return: The deletion_time of this DeletedBucket.  # noqa: E501
        :rtype: str
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this DeletedBucket.

        Bucket deletion time  # noqa: E501

        :param deletion_time: The deletion_time of this DeletedBucket.  # noqa: E501
        :type: str
        """

        self._deletion_time = deletion_time

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
        if issubclass(DeletedBucket, dict):
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
        if not isinstance(other, DeletedBucket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeletedBucket):
            return True

        return self.to_dict() != other.to_dict()