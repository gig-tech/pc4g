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


class CdromImagesModel(object):
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
        'cdrom_id': 'int',
        'name': 'str',
        'description': 'str',
        'os_type': 'str',
        'public': 'bool',
        'os_name': 'str'
    }

    attribute_map = {
        'cdrom_id': 'cdrom_id',
        'name': 'name',
        'description': 'description',
        'os_type': 'os_type',
        'public': 'public',
        'os_name': 'os_name'
    }

    def __init__(self, cdrom_id=None, name=None, description=None, os_type=None, public=None, os_name=None, _configuration=None):  # noqa: E501
        """CdromImagesModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cdrom_id = None
        self._name = None
        self._description = None
        self._os_type = None
        self._public = None
        self._os_name = None
        self.discriminator = None

        if cdrom_id is not None:
            self.cdrom_id = cdrom_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if os_type is not None:
            self.os_type = os_type
        if public is not None:
            self.public = public
        if os_name is not None:
            self.os_name = os_name

    @property
    def cdrom_id(self):
        """Gets the cdrom_id of this CdromImagesModel.  # noqa: E501


        :return: The cdrom_id of this CdromImagesModel.  # noqa: E501
        :rtype: int
        """
        return self._cdrom_id

    @cdrom_id.setter
    def cdrom_id(self, cdrom_id):
        """Sets the cdrom_id of this CdromImagesModel.


        :param cdrom_id: The cdrom_id of this CdromImagesModel.  # noqa: E501
        :type: int
        """

        self._cdrom_id = cdrom_id

    @property
    def name(self):
        """Gets the name of this CdromImagesModel.  # noqa: E501


        :return: The name of this CdromImagesModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CdromImagesModel.


        :param name: The name of this CdromImagesModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CdromImagesModel.  # noqa: E501


        :return: The description of this CdromImagesModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CdromImagesModel.


        :param description: The description of this CdromImagesModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def os_type(self):
        """Gets the os_type of this CdromImagesModel.  # noqa: E501


        :return: The os_type of this CdromImagesModel.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this CdromImagesModel.


        :param os_type: The os_type of this CdromImagesModel.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def public(self):
        """Gets the public of this CdromImagesModel.  # noqa: E501

        Public image  # noqa: E501

        :return: The public of this CdromImagesModel.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this CdromImagesModel.

        Public image  # noqa: E501

        :param public: The public of this CdromImagesModel.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def os_name(self):
        """Gets the os_name of this CdromImagesModel.  # noqa: E501

        Specific name of the Operating system  # noqa: E501

        :return: The os_name of this CdromImagesModel.  # noqa: E501
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this CdromImagesModel.

        Specific name of the Operating system  # noqa: E501

        :param os_name: The os_name of this CdromImagesModel.  # noqa: E501
        :type: str
        """

        self._os_name = os_name

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
        if issubclass(CdromImagesModel, dict):
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
        if not isinstance(other, CdromImagesModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CdromImagesModel):
            return True

        return self.to_dict() != other.to_dict()
