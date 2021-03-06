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


class CustomCloudspaceFirewall(object):
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
        'cdrom_id': 'int',
        'type': 'str',
        'disk_size': 'int',
        'vcpus': 'int',
        'memory': 'int'
    }

    attribute_map = {
        'image_id': 'image_id',
        'cdrom_id': 'cdrom_id',
        'type': 'type',
        'disk_size': 'disk_size',
        'vcpus': 'vcpus',
        'memory': 'memory'
    }

    def __init__(self, image_id=None, cdrom_id=None, type='Linux', disk_size=None, vcpus=None, memory=None, _configuration=None):  # noqa: E501
        """CustomCloudspaceFirewall - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._image_id = None
        self._cdrom_id = None
        self._type = None
        self._disk_size = None
        self._vcpus = None
        self._memory = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if cdrom_id is not None:
            self.cdrom_id = cdrom_id
        if type is not None:
            self.type = type
        if disk_size is not None:
            self.disk_size = disk_size
        if vcpus is not None:
            self.vcpus = vcpus
        if memory is not None:
            self.memory = memory

    @property
    def image_id(self):
        """Gets the image_id of this CustomCloudspaceFirewall.  # noqa: E501

        Image ID to use for custom firewall  # noqa: E501

        :return: The image_id of this CustomCloudspaceFirewall.  # noqa: E501
        :rtype: int
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CustomCloudspaceFirewall.

        Image ID to use for custom firewall  # noqa: E501

        :param image_id: The image_id of this CustomCloudspaceFirewall.  # noqa: E501
        :type: int
        """

        self._image_id = image_id

    @property
    def cdrom_id(self):
        """Gets the cdrom_id of this CustomCloudspaceFirewall.  # noqa: E501

        CDROM Image ID to use for custom firewall  # noqa: E501

        :return: The cdrom_id of this CustomCloudspaceFirewall.  # noqa: E501
        :rtype: int
        """
        return self._cdrom_id

    @cdrom_id.setter
    def cdrom_id(self, cdrom_id):
        """Sets the cdrom_id of this CustomCloudspaceFirewall.

        CDROM Image ID to use for custom firewall  # noqa: E501

        :param cdrom_id: The cdrom_id of this CustomCloudspaceFirewall.  # noqa: E501
        :type: int
        """

        self._cdrom_id = cdrom_id

    @property
    def type(self):
        """Gets the type of this CustomCloudspaceFirewall.  # noqa: E501

        Firewall VM OS type. Required when passing image_id  # noqa: E501

        :return: The type of this CustomCloudspaceFirewall.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomCloudspaceFirewall.

        Firewall VM OS type. Required when passing image_id  # noqa: E501

        :param type: The type of this CustomCloudspaceFirewall.  # noqa: E501
        :type: str
        """
        allowed_values = ["Linux", "Windows", "Unix", "BSD", "Darwin", "Other"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def disk_size(self):
        """Gets the disk_size of this CustomCloudspaceFirewall.  # noqa: E501

        Disk size to use for custom firewall VM  # noqa: E501

        :return: The disk_size of this CustomCloudspaceFirewall.  # noqa: E501
        :rtype: int
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        """Sets the disk_size of this CustomCloudspaceFirewall.

        Disk size to use for custom firewall VM  # noqa: E501

        :param disk_size: The disk_size of this CustomCloudspaceFirewall.  # noqa: E501
        :type: int
        """

        self._disk_size = disk_size

    @property
    def vcpus(self):
        """Gets the vcpus of this CustomCloudspaceFirewall.  # noqa: E501

        VCPUs to use for custom firewall VM  # noqa: E501

        :return: The vcpus of this CustomCloudspaceFirewall.  # noqa: E501
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this CustomCloudspaceFirewall.

        VCPUs to use for custom firewall VM  # noqa: E501

        :param vcpus: The vcpus of this CustomCloudspaceFirewall.  # noqa: E501
        :type: int
        """

        self._vcpus = vcpus

    @property
    def memory(self):
        """Gets the memory of this CustomCloudspaceFirewall.  # noqa: E501

        Memory to use for custom firewall VM  # noqa: E501

        :return: The memory of this CustomCloudspaceFirewall.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this CustomCloudspaceFirewall.

        Memory to use for custom firewall VM  # noqa: E501

        :param memory: The memory of this CustomCloudspaceFirewall.  # noqa: E501
        :type: int
        """

        self._memory = memory

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
        if issubclass(CustomCloudspaceFirewall, dict):
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
        if not isinstance(other, CustomCloudspaceFirewall):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomCloudspaceFirewall):
            return True

        return self.to_dict() != other.to_dict()
