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


class ItemPublicTokenExchangeResponse(object):
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
        'access_token': 'str',
        'item_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'item_id': 'item_id',
        'request_id': 'request_id'
    }

    def __init__(self, access_token=None, item_id=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """ItemPublicTokenExchangeResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._item_id = None
        self._request_id = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if item_id is not None:
            self.item_id = item_id
        if request_id is not None:
            self.request_id = request_id

    @property
    def access_token(self):
        """Gets the access_token of this ItemPublicTokenExchangeResponse.  # noqa: E501

        The access token associated with the Item data is being requested for.  # noqa: E501

        :return: The access_token of this ItemPublicTokenExchangeResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this ItemPublicTokenExchangeResponse.

        The access token associated with the Item data is being requested for.  # noqa: E501

        :param access_token: The access_token of this ItemPublicTokenExchangeResponse.  # noqa: E501
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def item_id(self):
        """Gets the item_id of this ItemPublicTokenExchangeResponse.  # noqa: E501

        The `item_id` value of the Item associated with the returned `access_token`  # noqa: E501

        :return: The item_id of this ItemPublicTokenExchangeResponse.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this ItemPublicTokenExchangeResponse.

        The `item_id` value of the Item associated with the returned `access_token`  # noqa: E501

        :param item_id: The item_id of this ItemPublicTokenExchangeResponse.  # noqa: E501
        :type item_id: str
        """

        self._item_id = item_id

    @property
    def request_id(self):
        """Gets the request_id of this ItemPublicTokenExchangeResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this ItemPublicTokenExchangeResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ItemPublicTokenExchangeResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this ItemPublicTokenExchangeResponse.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

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
        if not isinstance(other, ItemPublicTokenExchangeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemPublicTokenExchangeResponse):
            return True

        return self.to_dict() != other.to_dict()
