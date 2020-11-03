# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class Error(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'error_type': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'display_message': 'str',
        'request_id': 'str',
        'causes': 'list[object]',
        'status': 'float',
        'documentation_url': 'str',
        'suggested_action': 'str'
    }

    attribute_map = {
        'error_type': 'error_type',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'display_message': 'display_message',
        'request_id': 'request_id',
        'causes': 'causes',
        'status': 'status',
        'documentation_url': 'documentation_url',
        'suggested_action': 'suggested_action'
    }

    def __init__(self, error_type=None, error_code=None, error_message=None, display_message=None, request_id=None, causes=None, status=None, documentation_url=None, suggested_action=None, local_vars_configuration=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error_type = None
        self._error_code = None
        self._error_message = None
        self._display_message = None
        self._request_id = None
        self._causes = None
        self._status = None
        self._documentation_url = None
        self._suggested_action = None
        self.discriminator = None

        if error_type is not None:
            self.error_type = error_type
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        self.display_message = display_message
        self.request_id = request_id
        if causes is not None:
            self.causes = causes
        self.status = status
        self.documentation_url = documentation_url
        self.suggested_action = suggested_action

    @property
    def error_type(self):
        """Gets the error_type of this Error.  # noqa: E501

        A broad categorization of the error. Safe for programatic use.  # noqa: E501

        :return: The error_type of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """Sets the error_type of this Error.

        A broad categorization of the error. Safe for programatic use.  # noqa: E501

        :param error_type: The error_type of this Error.  # noqa: E501
        :type error_type: str
        """
        allowed_values = ["INVALID_REQUEST", "INVALID_INPUT", "INSTITUTION_ERROR", "RATE_LIMIT_EXCEEDED", "API_ERROR", "ITEM_ERROR", "ASSET_REPORT_ERROR", "RECAPTCHA_ERROR", "OAUTH_ERROR", "PAYMENT_ERROR", "BANK_TRANSFER_ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and error_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `error_type` ({0}), must be one of {1}"  # noqa: E501
                .format(error_type, allowed_values)
            )

        self._error_type = error_type

    @property
    def error_code(self):
        """Gets the error_code of this Error.  # noqa: E501

        The particular error code. Safe for programmatic use.  # noqa: E501

        :return: The error_code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Error.

        The particular error code. Safe for programmatic use.  # noqa: E501

        :param error_code: The error_code of this Error.  # noqa: E501
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this Error.  # noqa: E501

        A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use.  # noqa: E501

        :return: The error_message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this Error.

        A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use.  # noqa: E501

        :param error_message: The error_message of this Error.  # noqa: E501
        :type error_message: str
        """

        self._error_message = error_message

    @property
    def display_message(self):
        """Gets the display_message of this Error.  # noqa: E501

        A user-friendly representation of the error code. `null` if the error is not related to user action.   This may change over time and is not safe for programmatic use.  # noqa: E501

        :return: The display_message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._display_message

    @display_message.setter
    def display_message(self, display_message):
        """Sets the display_message of this Error.

        A user-friendly representation of the error code. `null` if the error is not related to user action.   This may change over time and is not safe for programmatic use.  # noqa: E501

        :param display_message: The display_message of this Error.  # noqa: E501
        :type display_message: str
        """

        self._display_message = display_message

    @property
    def request_id(self):
        """Gets the request_id of this Error.  # noqa: E501

        A unique identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks.  # noqa: E501

        :return: The request_id of this Error.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this Error.

        A unique identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks.  # noqa: E501

        :param request_id: The request_id of this Error.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

    @property
    def causes(self):
        """Gets the causes of this Error.  # noqa: E501

        In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, `causes` will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.   `causes` will only be provided for the `error_type` `ASSET_REPORT_ERROR`.  # noqa: E501

        :return: The causes of this Error.  # noqa: E501
        :rtype: list[object]
        """
        return self._causes

    @causes.setter
    def causes(self, causes):
        """Sets the causes of this Error.

        In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, `causes` will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.   `causes` will only be provided for the `error_type` `ASSET_REPORT_ERROR`.  # noqa: E501

        :param causes: The causes of this Error.  # noqa: E501
        :type causes: list[object]
        """

        self._causes = causes

    @property
    def status(self):
        """Gets the status of this Error.  # noqa: E501

        The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook.  # noqa: E501

        :return: The status of this Error.  # noqa: E501
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Error.

        The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook.  # noqa: E501

        :param status: The status of this Error.  # noqa: E501
        :type status: float
        """

        self._status = status

    @property
    def documentation_url(self):
        """Gets the documentation_url of this Error.  # noqa: E501

        The URL of a Plaid documentation page with more information about the error  # noqa: E501

        :return: The documentation_url of this Error.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this Error.

        The URL of a Plaid documentation page with more information about the error  # noqa: E501

        :param documentation_url: The documentation_url of this Error.  # noqa: E501
        :type documentation_url: str
        """

        self._documentation_url = documentation_url

    @property
    def suggested_action(self):
        """Gets the suggested_action of this Error.  # noqa: E501

        Suggested steps for resolving the error  # noqa: E501

        :return: The suggested_action of this Error.  # noqa: E501
        :rtype: str
        """
        return self._suggested_action

    @suggested_action.setter
    def suggested_action(self, suggested_action):
        """Sets the suggested_action of this Error.

        Suggested steps for resolving the error  # noqa: E501

        :param suggested_action: The suggested_action of this Error.  # noqa: E501
        :type suggested_action: str
        """

        self._suggested_action = suggested_action

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Error):
            return True

        return self.to_dict() != other.to_dict()
