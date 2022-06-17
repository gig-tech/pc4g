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


class ImagesModel(object):
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
        'image_id': 'int',
        'status': 'str',
        'name': 'str',
        'description': 'str',
        'os_type': 'str',
        'boot_disk_size': 'int',
        'size': 'int',
        'memory': 'int',
        'tags': 'str',
        'public': 'bool'
    }

    attribute_map = {
        'image_id': 'image_id',
        'status': 'status',
        'name': 'name',
        'description': 'description',
        'os_type': 'os_type',
        'boot_disk_size': 'boot_disk_size',
        'size': 'size',
        'memory': 'memory',
        'tags': 'tags',
        'public': 'public'
    }

    def __init__(self, image_id=None, status=None, name=None, description=None, os_type=None, boot_disk_size=None, size=None, memory=None, tags=None, public=None, _configuration=None):  # noqa: E501
        """ImagesModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._image_id = None
        self._status = None
        self._name = None
        self._description = None
        self._os_type = None
        self._boot_disk_size = None
        self._size = None
        self._memory = None
        self._tags = None
        self._public = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if os_type is not None:
            self.os_type = os_type
        if boot_disk_size is not None:
            self.boot_disk_size = boot_disk_size
        if size is not None:
            self.size = size
        if memory is not None:
            self.memory = memory
        if tags is not None:
            self.tags = tags
        if public is not None:
            self.public = public

    @property
    def image_id(self):
        """Gets the image_id of this ImagesModel.  # noqa: E501


        :return: The image_id of this ImagesModel.  # noqa: E501
        :rtype: int
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImagesModel.


        :param image_id: The image_id of this ImagesModel.  # noqa: E501
        :type: int
        """

        self._image_id = image_id

    @property
    def status(self):
        """Gets the status of this ImagesModel.  # noqa: E501


        :return: The status of this ImagesModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImagesModel.


        :param status: The status of this ImagesModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def name(self):
        """Gets the name of this ImagesModel.  # noqa: E501


        :return: The name of this ImagesModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImagesModel.


        :param name: The name of this ImagesModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ImagesModel.  # noqa: E501


        :return: The description of this ImagesModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImagesModel.


        :param description: The description of this ImagesModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def os_type(self):
        """Gets the os_type of this ImagesModel.  # noqa: E501


        :return: The os_type of this ImagesModel.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ImagesModel.


        :param os_type: The os_type of this ImagesModel.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def boot_disk_size(self):
        """Gets the boot_disk_size of this ImagesModel.  # noqa: E501


        :return: The boot_disk_size of this ImagesModel.  # noqa: E501
        :rtype: int
        """
        return self._boot_disk_size

    @boot_disk_size.setter
    def boot_disk_size(self, boot_disk_size):
        """Sets the boot_disk_size of this ImagesModel.


        :param boot_disk_size: The boot_disk_size of this ImagesModel.  # noqa: E501
        :type: int
        """

        self._boot_disk_size = boot_disk_size

    @property
    def size(self):
        """Gets the size of this ImagesModel.  # noqa: E501


        :return: The size of this ImagesModel.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImagesModel.


        :param size: The size of this ImagesModel.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def memory(self):
        """Gets the memory of this ImagesModel.  # noqa: E501


        :return: The memory of this ImagesModel.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ImagesModel.


        :param memory: The memory of this ImagesModel.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def tags(self):
        """Gets the tags of this ImagesModel.  # noqa: E501


        :return: The tags of this ImagesModel.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ImagesModel.


        :param tags: The tags of this ImagesModel.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def public(self):
        """Gets the public of this ImagesModel.  # noqa: E501

        Public image  # noqa: E501

        :return: The public of this ImagesModel.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ImagesModel.

        Public image  # noqa: E501

        :param public: The public of this ImagesModel.  # noqa: E501
        :type: bool
        """

        self._public = public

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
        if issubclass(ImagesModel, dict):
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
        if not isinstance(other, ImagesModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImagesModel):
            return True

        return self.to_dict() != other.to_dict()
