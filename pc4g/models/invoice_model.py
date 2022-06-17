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


class InvoiceModel(object):
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
        'creation_timestamp': 'int',
        'currency': 'str',
        'customer_id': 'str',
        'due_date_timestamp': 'int',
        'id': 'str',
        'invoice_id': 'str',
        'latest_payment_timestamp': 'int',
        'locations': 'list[Location]',
        'month': 'int',
        'number': 'str',
        'payment_status': 'str',
        'sent_timestamp': 'int',
        'sequence_number': 'int',
        'status': 'str',
        'total_ex': 'float',
        'total_incl': 'float',
        'vat': 'float',
        'vat_comment': 'str',
        'vat_legal_term': 'str',
        'vat_pct': 'float'
    }

    attribute_map = {
        'creation_timestamp': 'creation_timestamp',
        'currency': 'currency',
        'customer_id': 'customer_id',
        'due_date_timestamp': 'due_date_timestamp',
        'id': 'id',
        'invoice_id': 'invoice_id',
        'latest_payment_timestamp': 'latest_payment_timestamp',
        'locations': 'locations',
        'month': 'month',
        'number': 'number',
        'payment_status': 'payment_status',
        'sent_timestamp': 'sent_timestamp',
        'sequence_number': 'sequence_number',
        'status': 'status',
        'total_ex': 'total_ex',
        'total_incl': 'total_incl',
        'vat': 'vat',
        'vat_comment': 'vat_comment',
        'vat_legal_term': 'vat_legal_term',
        'vat_pct': 'vat_pct'
    }

    def __init__(self, creation_timestamp=None, currency=None, customer_id=None, due_date_timestamp=None, id=None, invoice_id=None, latest_payment_timestamp=None, locations=None, month=None, number=None, payment_status=None, sent_timestamp=None, sequence_number=None, status=None, total_ex=None, total_incl=None, vat=None, vat_comment=None, vat_legal_term=None, vat_pct=None, _configuration=None):  # noqa: E501
        """InvoiceModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_timestamp = None
        self._currency = None
        self._customer_id = None
        self._due_date_timestamp = None
        self._id = None
        self._invoice_id = None
        self._latest_payment_timestamp = None
        self._locations = None
        self._month = None
        self._number = None
        self._payment_status = None
        self._sent_timestamp = None
        self._sequence_number = None
        self._status = None
        self._total_ex = None
        self._total_incl = None
        self._vat = None
        self._vat_comment = None
        self._vat_legal_term = None
        self._vat_pct = None
        self.discriminator = None

        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if currency is not None:
            self.currency = currency
        if customer_id is not None:
            self.customer_id = customer_id
        if due_date_timestamp is not None:
            self.due_date_timestamp = due_date_timestamp
        if id is not None:
            self.id = id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if latest_payment_timestamp is not None:
            self.latest_payment_timestamp = latest_payment_timestamp
        if locations is not None:
            self.locations = locations
        if month is not None:
            self.month = month
        if number is not None:
            self.number = number
        if payment_status is not None:
            self.payment_status = payment_status
        if sent_timestamp is not None:
            self.sent_timestamp = sent_timestamp
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if status is not None:
            self.status = status
        if total_ex is not None:
            self.total_ex = total_ex
        if total_incl is not None:
            self.total_incl = total_incl
        if vat is not None:
            self.vat = vat
        if vat_comment is not None:
            self.vat_comment = vat_comment
        if vat_legal_term is not None:
            self.vat_legal_term = vat_legal_term
        if vat_pct is not None:
            self.vat_pct = vat_pct

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this InvoiceModel.  # noqa: E501

        Creation unix timestamp  # noqa: E501

        :return: The creation_timestamp of this InvoiceModel.  # noqa: E501
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this InvoiceModel.

        Creation unix timestamp  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this InvoiceModel.  # noqa: E501
        :type: int
        """

        self._creation_timestamp = creation_timestamp

    @property
    def currency(self):
        """Gets the currency of this InvoiceModel.  # noqa: E501

        Currency used for this invoice  # noqa: E501

        :return: The currency of this InvoiceModel.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoiceModel.

        Currency used for this invoice  # noqa: E501

        :param currency: The currency of this InvoiceModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BYN", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XFU", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                currency not in allowed_values):
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def customer_id(self):
        """Gets the customer_id of this InvoiceModel.  # noqa: E501


        :return: The customer_id of this InvoiceModel.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InvoiceModel.


        :param customer_id: The customer_id of this InvoiceModel.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def due_date_timestamp(self):
        """Gets the due_date_timestamp of this InvoiceModel.  # noqa: E501

        Invoice due date unix timestamp  # noqa: E501

        :return: The due_date_timestamp of this InvoiceModel.  # noqa: E501
        :rtype: int
        """
        return self._due_date_timestamp

    @due_date_timestamp.setter
    def due_date_timestamp(self, due_date_timestamp):
        """Sets the due_date_timestamp of this InvoiceModel.

        Invoice due date unix timestamp  # noqa: E501

        :param due_date_timestamp: The due_date_timestamp of this InvoiceModel.  # noqa: E501
        :type: int
        """

        self._due_date_timestamp = due_date_timestamp

    @property
    def id(self):
        """Gets the id of this InvoiceModel.  # noqa: E501


        :return: The id of this InvoiceModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceModel.


        :param id: The id of this InvoiceModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this InvoiceModel.  # noqa: E501


        :return: The invoice_id of this InvoiceModel.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this InvoiceModel.


        :param invoice_id: The invoice_id of this InvoiceModel.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def latest_payment_timestamp(self):
        """Gets the latest_payment_timestamp of this InvoiceModel.  # noqa: E501

        latest payment unix timestamp  # noqa: E501

        :return: The latest_payment_timestamp of this InvoiceModel.  # noqa: E501
        :rtype: int
        """
        return self._latest_payment_timestamp

    @latest_payment_timestamp.setter
    def latest_payment_timestamp(self, latest_payment_timestamp):
        """Sets the latest_payment_timestamp of this InvoiceModel.

        latest payment unix timestamp  # noqa: E501

        :param latest_payment_timestamp: The latest_payment_timestamp of this InvoiceModel.  # noqa: E501
        :type: int
        """

        self._latest_payment_timestamp = latest_payment_timestamp

    @property
    def locations(self):
        """Gets the locations of this InvoiceModel.  # noqa: E501


        :return: The locations of this InvoiceModel.  # noqa: E501
        :rtype: list[Location]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this InvoiceModel.


        :param locations: The locations of this InvoiceModel.  # noqa: E501
        :type: list[Location]
        """

        self._locations = locations

    @property
    def month(self):
        """Gets the month of this InvoiceModel.  # noqa: E501

        Month for the invoiced services unix timestamp  # noqa: E501

        :return: The month of this InvoiceModel.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this InvoiceModel.

        Month for the invoiced services unix timestamp  # noqa: E501

        :param month: The month of this InvoiceModel.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def number(self):
        """Gets the number of this InvoiceModel.  # noqa: E501

        Invoice formatted number  # noqa: E501

        :return: The number of this InvoiceModel.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InvoiceModel.

        Invoice formatted number  # noqa: E501

        :param number: The number of this InvoiceModel.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def payment_status(self):
        """Gets the payment_status of this InvoiceModel.  # noqa: E501


        :return: The payment_status of this InvoiceModel.  # noqa: E501
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """Sets the payment_status of this InvoiceModel.


        :param payment_status: The payment_status of this InvoiceModel.  # noqa: E501
        :type: str
        """

        self._payment_status = payment_status

    @property
    def sent_timestamp(self):
        """Gets the sent_timestamp of this InvoiceModel.  # noqa: E501

        Invoice sending unix timestamp  # noqa: E501

        :return: The sent_timestamp of this InvoiceModel.  # noqa: E501
        :rtype: int
        """
        return self._sent_timestamp

    @sent_timestamp.setter
    def sent_timestamp(self, sent_timestamp):
        """Sets the sent_timestamp of this InvoiceModel.

        Invoice sending unix timestamp  # noqa: E501

        :param sent_timestamp: The sent_timestamp of this InvoiceModel.  # noqa: E501
        :type: int
        """

        self._sent_timestamp = sent_timestamp

    @property
    def sequence_number(self):
        """Gets the sequence_number of this InvoiceModel.  # noqa: E501

        Invoice yearly sequence number  # noqa: E501

        :return: The sequence_number of this InvoiceModel.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this InvoiceModel.

        Invoice yearly sequence number  # noqa: E501

        :param sequence_number: The sequence_number of this InvoiceModel.  # noqa: E501
        :type: int
        """

        self._sequence_number = sequence_number

    @property
    def status(self):
        """Gets the status of this InvoiceModel.  # noqa: E501


        :return: The status of this InvoiceModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InvoiceModel.


        :param status: The status of this InvoiceModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Draft", "Sent"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def total_ex(self):
        """Gets the total_ex of this InvoiceModel.  # noqa: E501

        Total invoice amount without VAT  # noqa: E501

        :return: The total_ex of this InvoiceModel.  # noqa: E501
        :rtype: float
        """
        return self._total_ex

    @total_ex.setter
    def total_ex(self, total_ex):
        """Sets the total_ex of this InvoiceModel.

        Total invoice amount without VAT  # noqa: E501

        :param total_ex: The total_ex of this InvoiceModel.  # noqa: E501
        :type: float
        """

        self._total_ex = total_ex

    @property
    def total_incl(self):
        """Gets the total_incl of this InvoiceModel.  # noqa: E501

        Total Invoice amount after VAT  # noqa: E501

        :return: The total_incl of this InvoiceModel.  # noqa: E501
        :rtype: float
        """
        return self._total_incl

    @total_incl.setter
    def total_incl(self, total_incl):
        """Sets the total_incl of this InvoiceModel.

        Total Invoice amount after VAT  # noqa: E501

        :param total_incl: The total_incl of this InvoiceModel.  # noqa: E501
        :type: float
        """

        self._total_incl = total_incl

    @property
    def vat(self):
        """Gets the vat of this InvoiceModel.  # noqa: E501

        Total VAT amount  # noqa: E501

        :return: The vat of this InvoiceModel.  # noqa: E501
        :rtype: float
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this InvoiceModel.

        Total VAT amount  # noqa: E501

        :param vat: The vat of this InvoiceModel.  # noqa: E501
        :type: float
        """

        self._vat = vat

    @property
    def vat_comment(self):
        """Gets the vat_comment of this InvoiceModel.  # noqa: E501

        VAT comment  # noqa: E501

        :return: The vat_comment of this InvoiceModel.  # noqa: E501
        :rtype: str
        """
        return self._vat_comment

    @vat_comment.setter
    def vat_comment(self, vat_comment):
        """Sets the vat_comment of this InvoiceModel.

        VAT comment  # noqa: E501

        :param vat_comment: The vat_comment of this InvoiceModel.  # noqa: E501
        :type: str
        """

        self._vat_comment = vat_comment

    @property
    def vat_legal_term(self):
        """Gets the vat_legal_term of this InvoiceModel.  # noqa: E501

        VAT Legal Terms  # noqa: E501

        :return: The vat_legal_term of this InvoiceModel.  # noqa: E501
        :rtype: str
        """
        return self._vat_legal_term

    @vat_legal_term.setter
    def vat_legal_term(self, vat_legal_term):
        """Sets the vat_legal_term of this InvoiceModel.

        VAT Legal Terms  # noqa: E501

        :param vat_legal_term: The vat_legal_term of this InvoiceModel.  # noqa: E501
        :type: str
        """

        self._vat_legal_term = vat_legal_term

    @property
    def vat_pct(self):
        """Gets the vat_pct of this InvoiceModel.  # noqa: E501

        Vat percentage  # noqa: E501

        :return: The vat_pct of this InvoiceModel.  # noqa: E501
        :rtype: float
        """
        return self._vat_pct

    @vat_pct.setter
    def vat_pct(self, vat_pct):
        """Sets the vat_pct of this InvoiceModel.

        Vat percentage  # noqa: E501

        :param vat_pct: The vat_pct of this InvoiceModel.  # noqa: E501
        :type: float
        """

        self._vat_pct = vat_pct

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
        if issubclass(InvoiceModel, dict):
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
        if not isinstance(other, InvoiceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceModel):
            return True

        return self.to_dict() != other.to_dict()