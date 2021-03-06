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


class CloudspaceInfoModelResourceLimits(object):
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
        'memory_quota': 'float',
        'vdisk_space_quota': 'int',
        'public_ip_quota': 'int',
        'vcpu_quota': 'int',
        'external_network_quota': 'int'
    }

    attribute_map = {
        'memory_quota': 'memory_quota',
        'vdisk_space_quota': 'vdisk_space_quota',
        'public_ip_quota': 'public_ip_quota',
        'vcpu_quota': 'vcpu_quota',
        'external_network_quota': 'external_network_quota'
    }

    def __init__(self, memory_quota=None, vdisk_space_quota=None, public_ip_quota=None, vcpu_quota=None, external_network_quota=None, _configuration=None):  # noqa: E501
        """CloudspaceInfoModelResourceLimits - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._memory_quota = None
        self._vdisk_space_quota = None
        self._public_ip_quota = None
        self._vcpu_quota = None
        self._external_network_quota = None
        self.discriminator = None

        if memory_quota is not None:
            self.memory_quota = memory_quota
        if vdisk_space_quota is not None:
            self.vdisk_space_quota = vdisk_space_quota
        if public_ip_quota is not None:
            self.public_ip_quota = public_ip_quota
        if vcpu_quota is not None:
            self.vcpu_quota = vcpu_quota
        if external_network_quota is not None:
            self.external_network_quota = external_network_quota

    @property
    def memory_quota(self):
        """Gets the memory_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501


        :return: The memory_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :rtype: float
        """
        return self._memory_quota

    @memory_quota.setter
    def memory_quota(self, memory_quota):
        """Sets the memory_quota of this CloudspaceInfoModelResourceLimits.


        :param memory_quota: The memory_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :type: float
        """

        self._memory_quota = memory_quota

    @property
    def vdisk_space_quota(self):
        """Gets the vdisk_space_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501


        :return: The vdisk_space_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._vdisk_space_quota

    @vdisk_space_quota.setter
    def vdisk_space_quota(self, vdisk_space_quota):
        """Sets the vdisk_space_quota of this CloudspaceInfoModelResourceLimits.


        :param vdisk_space_quota: The vdisk_space_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :type: int
        """

        self._vdisk_space_quota = vdisk_space_quota

    @property
    def public_ip_quota(self):
        """Gets the public_ip_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501


        :return: The public_ip_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._public_ip_quota

    @public_ip_quota.setter
    def public_ip_quota(self, public_ip_quota):
        """Sets the public_ip_quota of this CloudspaceInfoModelResourceLimits.


        :param public_ip_quota: The public_ip_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :type: int
        """

        self._public_ip_quota = public_ip_quota

    @property
    def vcpu_quota(self):
        """Gets the vcpu_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501


        :return: The vcpu_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._vcpu_quota

    @vcpu_quota.setter
    def vcpu_quota(self, vcpu_quota):
        """Sets the vcpu_quota of this CloudspaceInfoModelResourceLimits.


        :param vcpu_quota: The vcpu_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :type: int
        """

        self._vcpu_quota = vcpu_quota

    @property
    def external_network_quota(self):
        """Gets the external_network_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501


        :return: The external_network_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :rtype: int
        """
        return self._external_network_quota

    @external_network_quota.setter
    def external_network_quota(self, external_network_quota):
        """Sets the external_network_quota of this CloudspaceInfoModelResourceLimits.


        :param external_network_quota: The external_network_quota of this CloudspaceInfoModelResourceLimits.  # noqa: E501
        :type: int
        """

        self._external_network_quota = external_network_quota

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
        if issubclass(CloudspaceInfoModelResourceLimits, dict):
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
        if not isinstance(other, CloudspaceInfoModelResourceLimits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudspaceInfoModelResourceLimits):
            return True

        return self.to_dict() != other.to_dict()
