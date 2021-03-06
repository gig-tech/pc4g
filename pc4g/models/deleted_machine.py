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


class DeletedMachine(object):
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
        'vm_name': 'str',
        'vm_id': 'int',
        'cloudspace_name': 'str',
        'cloudspace_id': 'str',
        'cloudspace_status': 'str',
        'location': 'str',
        'deletion_time': 'str'
    }

    attribute_map = {
        'vm_name': 'vm_name',
        'vm_id': 'vm_id',
        'cloudspace_name': 'cloudspace_name',
        'cloudspace_id': 'cloudspace_id',
        'cloudspace_status': 'cloudspace_status',
        'location': 'location',
        'deletion_time': 'deletion_time'
    }

    def __init__(self, vm_name=None, vm_id=None, cloudspace_name=None, cloudspace_id=None, cloudspace_status=None, location='Virtual Machine location', deletion_time=None, _configuration=None):  # noqa: E501
        """DeletedMachine - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vm_name = None
        self._vm_id = None
        self._cloudspace_name = None
        self._cloudspace_id = None
        self._cloudspace_status = None
        self._location = None
        self._deletion_time = None
        self.discriminator = None

        if vm_name is not None:
            self.vm_name = vm_name
        if vm_id is not None:
            self.vm_id = vm_id
        if cloudspace_name is not None:
            self.cloudspace_name = cloudspace_name
        if cloudspace_id is not None:
            self.cloudspace_id = cloudspace_id
        if cloudspace_status is not None:
            self.cloudspace_status = cloudspace_status
        if location is not None:
            self.location = location
        if deletion_time is not None:
            self.deletion_time = deletion_time

    @property
    def vm_name(self):
        """Gets the vm_name of this DeletedMachine.  # noqa: E501

        Virtual Machine name  # noqa: E501

        :return: The vm_name of this DeletedMachine.  # noqa: E501
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """Sets the vm_name of this DeletedMachine.

        Virtual Machine name  # noqa: E501

        :param vm_name: The vm_name of this DeletedMachine.  # noqa: E501
        :type: str
        """

        self._vm_name = vm_name

    @property
    def vm_id(self):
        """Gets the vm_id of this DeletedMachine.  # noqa: E501

        Virtual Machine id  # noqa: E501

        :return: The vm_id of this DeletedMachine.  # noqa: E501
        :rtype: int
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this DeletedMachine.

        Virtual Machine id  # noqa: E501

        :param vm_id: The vm_id of this DeletedMachine.  # noqa: E501
        :type: int
        """

        self._vm_id = vm_id

    @property
    def cloudspace_name(self):
        """Gets the cloudspace_name of this DeletedMachine.  # noqa: E501

        Cloudspace name  # noqa: E501

        :return: The cloudspace_name of this DeletedMachine.  # noqa: E501
        :rtype: str
        """
        return self._cloudspace_name

    @cloudspace_name.setter
    def cloudspace_name(self, cloudspace_name):
        """Sets the cloudspace_name of this DeletedMachine.

        Cloudspace name  # noqa: E501

        :param cloudspace_name: The cloudspace_name of this DeletedMachine.  # noqa: E501
        :type: str
        """

        self._cloudspace_name = cloudspace_name

    @property
    def cloudspace_id(self):
        """Gets the cloudspace_id of this DeletedMachine.  # noqa: E501

        Cloudspace id  # noqa: E501

        :return: The cloudspace_id of this DeletedMachine.  # noqa: E501
        :rtype: str
        """
        return self._cloudspace_id

    @cloudspace_id.setter
    def cloudspace_id(self, cloudspace_id):
        """Sets the cloudspace_id of this DeletedMachine.

        Cloudspace id  # noqa: E501

        :param cloudspace_id: The cloudspace_id of this DeletedMachine.  # noqa: E501
        :type: str
        """

        self._cloudspace_id = cloudspace_id

    @property
    def cloudspace_status(self):
        """Gets the cloudspace_status of this DeletedMachine.  # noqa: E501

        Cloudspace status  # noqa: E501

        :return: The cloudspace_status of this DeletedMachine.  # noqa: E501
        :rtype: str
        """
        return self._cloudspace_status

    @cloudspace_status.setter
    def cloudspace_status(self, cloudspace_status):
        """Sets the cloudspace_status of this DeletedMachine.

        Cloudspace status  # noqa: E501

        :param cloudspace_status: The cloudspace_status of this DeletedMachine.  # noqa: E501
        :type: str
        """

        self._cloudspace_status = cloudspace_status

    @property
    def location(self):
        """Gets the location of this DeletedMachine.  # noqa: E501


        :return: The location of this DeletedMachine.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DeletedMachine.


        :param location: The location of this DeletedMachine.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def deletion_time(self):
        """Gets the deletion_time of this DeletedMachine.  # noqa: E501

        Virtual Machine deletion time  # noqa: E501

        :return: The deletion_time of this DeletedMachine.  # noqa: E501
        :rtype: str
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this DeletedMachine.

        Virtual Machine deletion time  # noqa: E501

        :param deletion_time: The deletion_time of this DeletedMachine.  # noqa: E501
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
        if issubclass(DeletedMachine, dict):
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
        if not isinstance(other, DeletedMachine):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeletedMachine):
            return True

        return self.to_dict() != other.to_dict()
