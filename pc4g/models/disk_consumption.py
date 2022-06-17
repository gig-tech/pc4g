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


class DiskConsumption(object):
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
        'disk_id': 'int',
        'invoice_lines': 'list[InvoiceLine]',
        'resources': 'ResourceConsumption',
        'total_ex': 'float',
        'total_incl': 'float'
    }

    attribute_map = {
        'disk_id': 'disk_id',
        'invoice_lines': 'invoice_lines',
        'resources': 'resources',
        'total_ex': 'total_ex',
        'total_incl': 'total_incl'
    }

    def __init__(self, disk_id=None, invoice_lines=None, resources=None, total_ex=None, total_incl=None, _configuration=None):  # noqa: E501
        """DiskConsumption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._disk_id = None
        self._invoice_lines = None
        self._resources = None
        self._total_ex = None
        self._total_incl = None
        self.discriminator = None

        if disk_id is not None:
            self.disk_id = disk_id
        if invoice_lines is not None:
            self.invoice_lines = invoice_lines
        if resources is not None:
            self.resources = resources
        if total_ex is not None:
            self.total_ex = total_ex
        if total_incl is not None:
            self.total_incl = total_incl

    @property
    def disk_id(self):
        """Gets the disk_id of this DiskConsumption.  # noqa: E501

        Disk ID  # noqa: E501

        :return: The disk_id of this DiskConsumption.  # noqa: E501
        :rtype: int
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, disk_id):
        """Sets the disk_id of this DiskConsumption.

        Disk ID  # noqa: E501

        :param disk_id: The disk_id of this DiskConsumption.  # noqa: E501
        :type: int
        """

        self._disk_id = disk_id

    @property
    def invoice_lines(self):
        """Gets the invoice_lines of this DiskConsumption.  # noqa: E501


        :return: The invoice_lines of this DiskConsumption.  # noqa: E501
        :rtype: list[InvoiceLine]
        """
        return self._invoice_lines

    @invoice_lines.setter
    def invoice_lines(self, invoice_lines):
        """Sets the invoice_lines of this DiskConsumption.


        :param invoice_lines: The invoice_lines of this DiskConsumption.  # noqa: E501
        :type: list[InvoiceLine]
        """

        self._invoice_lines = invoice_lines

    @property
    def resources(self):
        """Gets the resources of this DiskConsumption.  # noqa: E501


        :return: The resources of this DiskConsumption.  # noqa: E501
        :rtype: ResourceConsumption
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this DiskConsumption.


        :param resources: The resources of this DiskConsumption.  # noqa: E501
        :type: ResourceConsumption
        """

        self._resources = resources

    @property
    def total_ex(self):
        """Gets the total_ex of this DiskConsumption.  # noqa: E501

        Total initial price  # noqa: E501

        :return: The total_ex of this DiskConsumption.  # noqa: E501
        :rtype: float
        """
        return self._total_ex

    @total_ex.setter
    def total_ex(self, total_ex):
        """Sets the total_ex of this DiskConsumption.

        Total initial price  # noqa: E501

        :param total_ex: The total_ex of this DiskConsumption.  # noqa: E501
        :type: float
        """

        self._total_ex = total_ex

    @property
    def total_incl(self):
        """Gets the total_incl of this DiskConsumption.  # noqa: E501

        Total amount after VAT  # noqa: E501

        :return: The total_incl of this DiskConsumption.  # noqa: E501
        :rtype: float
        """
        return self._total_incl

    @total_incl.setter
    def total_incl(self, total_incl):
        """Sets the total_incl of this DiskConsumption.

        Total amount after VAT  # noqa: E501

        :param total_incl: The total_incl of this DiskConsumption.  # noqa: E501
        :type: float
        """

        self._total_incl = total_incl

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
        if issubclass(DiskConsumption, dict):
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
        if not isinstance(other, DiskConsumption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiskConsumption):
            return True

        return self.to_dict() != other.to_dict()
