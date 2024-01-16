"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.485.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from plaid.exceptions import ApiAttributeError


def lazy_import():
    from plaid.model.risk_check_email_domain_is_custom import RiskCheckEmailDomainIsCustom
    from plaid.model.risk_check_email_domain_is_disposable import RiskCheckEmailDomainIsDisposable
    from plaid.model.risk_check_email_domain_is_free_provider import RiskCheckEmailDomainIsFreeProvider
    from plaid.model.risk_check_email_is_deliverable_status import RiskCheckEmailIsDeliverableStatus
    from plaid.model.risk_check_email_top_level_domain_is_suspicious import RiskCheckEmailTopLevelDomainIsSuspicious
    from plaid.model.risk_check_linked_service import RiskCheckLinkedService
    globals()['RiskCheckEmailDomainIsCustom'] = RiskCheckEmailDomainIsCustom
    globals()['RiskCheckEmailDomainIsDisposable'] = RiskCheckEmailDomainIsDisposable
    globals()['RiskCheckEmailDomainIsFreeProvider'] = RiskCheckEmailDomainIsFreeProvider
    globals()['RiskCheckEmailIsDeliverableStatus'] = RiskCheckEmailIsDeliverableStatus
    globals()['RiskCheckEmailTopLevelDomainIsSuspicious'] = RiskCheckEmailTopLevelDomainIsSuspicious
    globals()['RiskCheckLinkedService'] = RiskCheckLinkedService


class RiskCheckEmail(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('linked_services',): {
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = True

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'is_deliverable': (RiskCheckEmailIsDeliverableStatus,),  # noqa: E501
            'breach_count': (int, none_type,),  # noqa: E501
            'first_breached_at': (date, none_type,),  # noqa: E501
            'last_breached_at': (date, none_type,),  # noqa: E501
            'domain_registered_at': (date, none_type,),  # noqa: E501
            'domain_is_free_provider': (RiskCheckEmailDomainIsFreeProvider,),  # noqa: E501
            'domain_is_custom': (RiskCheckEmailDomainIsCustom,),  # noqa: E501
            'domain_is_disposable': (RiskCheckEmailDomainIsDisposable,),  # noqa: E501
            'top_level_domain_is_suspicious': (RiskCheckEmailTopLevelDomainIsSuspicious,),  # noqa: E501
            'linked_services': ([RiskCheckLinkedService],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'is_deliverable': 'is_deliverable',  # noqa: E501
        'breach_count': 'breach_count',  # noqa: E501
        'first_breached_at': 'first_breached_at',  # noqa: E501
        'last_breached_at': 'last_breached_at',  # noqa: E501
        'domain_registered_at': 'domain_registered_at',  # noqa: E501
        'domain_is_free_provider': 'domain_is_free_provider',  # noqa: E501
        'domain_is_custom': 'domain_is_custom',  # noqa: E501
        'domain_is_disposable': 'domain_is_disposable',  # noqa: E501
        'top_level_domain_is_suspicious': 'top_level_domain_is_suspicious',  # noqa: E501
        'linked_services': 'linked_services',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, is_deliverable, breach_count, first_breached_at, last_breached_at, domain_registered_at, domain_is_free_provider, domain_is_custom, domain_is_disposable, top_level_domain_is_suspicious, linked_services, *args, **kwargs):  # noqa: E501
        """RiskCheckEmail - a model defined in OpenAPI

        Args:
            is_deliverable (RiskCheckEmailIsDeliverableStatus):
            breach_count (int, none_type): Count of all known breaches of this email address if known.
            first_breached_at (date, none_type): A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).
            last_breached_at (date, none_type): A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).
            domain_registered_at (date, none_type): A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).
            domain_is_free_provider (RiskCheckEmailDomainIsFreeProvider):
            domain_is_custom (RiskCheckEmailDomainIsCustom):
            domain_is_disposable (RiskCheckEmailDomainIsDisposable):
            top_level_domain_is_suspicious (RiskCheckEmailTopLevelDomainIsSuspicious):
            linked_services ([RiskCheckLinkedService]): A list of online services where this email address has been detected to have accounts or other activity.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.is_deliverable = is_deliverable
        self.breach_count = breach_count
        self.first_breached_at = first_breached_at
        self.last_breached_at = last_breached_at
        self.domain_registered_at = domain_registered_at
        self.domain_is_free_provider = domain_is_free_provider
        self.domain_is_custom = domain_is_custom
        self.domain_is_disposable = domain_is_disposable
        self.top_level_domain_is_suspicious = top_level_domain_is_suspicious
        self.linked_services = linked_services
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, is_deliverable, breach_count, first_breached_at, last_breached_at, domain_registered_at, domain_is_free_provider, domain_is_custom, domain_is_disposable, top_level_domain_is_suspicious, linked_services, *args, **kwargs):  # noqa: E501
        """RiskCheckEmail - a model defined in OpenAPI

        Args:
            is_deliverable (RiskCheckEmailIsDeliverableStatus):
            breach_count (int, none_type): Count of all known breaches of this email address if known.
            first_breached_at (date, none_type): A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).
            last_breached_at (date, none_type): A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).
            domain_registered_at (date, none_type): A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).
            domain_is_free_provider (RiskCheckEmailDomainIsFreeProvider):
            domain_is_custom (RiskCheckEmailDomainIsCustom):
            domain_is_disposable (RiskCheckEmailDomainIsDisposable):
            top_level_domain_is_suspicious (RiskCheckEmailTopLevelDomainIsSuspicious):
            linked_services ([RiskCheckLinkedService]): A list of online services where this email address has been detected to have accounts or other activity.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.is_deliverable = is_deliverable
        self.breach_count = breach_count
        self.first_breached_at = first_breached_at
        self.last_breached_at = last_breached_at
        self.domain_registered_at = domain_registered_at
        self.domain_is_free_provider = domain_is_free_provider
        self.domain_is_custom = domain_is_custom
        self.domain_is_disposable = domain_is_disposable
        self.top_level_domain_is_suspicious = top_level_domain_is_suspicious
        self.linked_services = linked_services
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
