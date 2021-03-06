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


class Datacenter(object):
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
        'address': 'str',
        'city': 'str',
        'code': 'str',
        'coordinates': 'object',
        'country': 'str',
        'country_code': 'str',
        'created_at': 'float',
        'created_by': 'str',
        'name': 'str'
    }

    attribute_map = {
        'address': 'address',
        'city': 'city',
        'code': 'code',
        'coordinates': 'coordinates',
        'country': 'country',
        'country_code': 'country_code',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'name': 'name'
    }

    def __init__(self, address=None, city=None, code=None, coordinates=None, country=None, country_code=None, created_at=None, created_by=None, name=None, _configuration=None):  # noqa: E501
        """Datacenter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._city = None
        self._code = None
        self._coordinates = None
        self._country = None
        self._country_code = None
        self._created_at = None
        self._created_by = None
        self._name = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if code is not None:
            self.code = code
        if coordinates is not None:
            self.coordinates = coordinates
        if country is not None:
            self.country = country
        if country_code is not None:
            self.country_code = country_code
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if name is not None:
            self.name = name

    @property
    def address(self):
        """Gets the address of this Datacenter.  # noqa: E501


        :return: The address of this Datacenter.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Datacenter.


        :param address: The address of this Datacenter.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this Datacenter.  # noqa: E501


        :return: The city of this Datacenter.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Datacenter.


        :param city: The city of this Datacenter.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def code(self):
        """Gets the code of this Datacenter.  # noqa: E501


        :return: The code of this Datacenter.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Datacenter.


        :param code: The code of this Datacenter.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def coordinates(self):
        """Gets the coordinates of this Datacenter.  # noqa: E501


        :return: The coordinates of this Datacenter.  # noqa: E501
        :rtype: object
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Datacenter.


        :param coordinates: The coordinates of this Datacenter.  # noqa: E501
        :type: object
        """

        self._coordinates = coordinates

    @property
    def country(self):
        """Gets the country of this Datacenter.  # noqa: E501


        :return: The country of this Datacenter.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Datacenter.


        :param country: The country of this Datacenter.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_code(self):
        """Gets the country_code of this Datacenter.  # noqa: E501


        :return: The country_code of this Datacenter.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Datacenter.


        :param country_code: The country_code of this Datacenter.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def created_at(self):
        """Gets the created_at of this Datacenter.  # noqa: E501


        :return: The created_at of this Datacenter.  # noqa: E501
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Datacenter.


        :param created_at: The created_at of this Datacenter.  # noqa: E501
        :type: float
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Datacenter.  # noqa: E501


        :return: The created_by of this Datacenter.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Datacenter.


        :param created_by: The created_by of this Datacenter.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def name(self):
        """Gets the name of this Datacenter.  # noqa: E501


        :return: The name of this Datacenter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Datacenter.


        :param name: The name of this Datacenter.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(Datacenter, dict):
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
        if not isinstance(other, Datacenter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Datacenter):
            return True

        return self.to_dict() != other.to_dict()
