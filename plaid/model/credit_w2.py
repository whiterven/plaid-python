"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.419.0
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
    from plaid.model.credit_document_metadata import CreditDocumentMetadata
    from plaid.model.credit_pay_stub_employee import CreditPayStubEmployee
    from plaid.model.credit_pay_stub_employer import CreditPayStubEmployer
    from plaid.model.w2_box12 import W2Box12
    from plaid.model.w2_state_and_local_wages import W2StateAndLocalWages
    globals()['CreditDocumentMetadata'] = CreditDocumentMetadata
    globals()['CreditPayStubEmployee'] = CreditPayStubEmployee
    globals()['CreditPayStubEmployer'] = CreditPayStubEmployer
    globals()['W2Box12'] = W2Box12
    globals()['W2StateAndLocalWages'] = W2StateAndLocalWages


class CreditW2(ModelNormal):
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
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

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
            'document_metadata': (CreditDocumentMetadata,),  # noqa: E501
            'document_id': (str,),  # noqa: E501
            'employer': (CreditPayStubEmployer,),  # noqa: E501
            'employee': (CreditPayStubEmployee,),  # noqa: E501
            'tax_year': (str, none_type,),  # noqa: E501
            'employer_id_number': (str, none_type,),  # noqa: E501
            'wages_tips_other_comp': (str, none_type,),  # noqa: E501
            'federal_income_tax_withheld': (str, none_type,),  # noqa: E501
            'social_security_wages': (str, none_type,),  # noqa: E501
            'social_security_tax_withheld': (str, none_type,),  # noqa: E501
            'medicare_wages_and_tips': (str, none_type,),  # noqa: E501
            'medicare_tax_withheld': (str, none_type,),  # noqa: E501
            'social_security_tips': (str, none_type,),  # noqa: E501
            'allocated_tips': (str, none_type,),  # noqa: E501
            'box_9': (str, none_type,),  # noqa: E501
            'dependent_care_benefits': (str, none_type,),  # noqa: E501
            'nonqualified_plans': (str, none_type,),  # noqa: E501
            'box_12': ([W2Box12],),  # noqa: E501
            'statutory_employee': (str, none_type,),  # noqa: E501
            'retirement_plan': (str, none_type,),  # noqa: E501
            'third_party_sick_pay': (str, none_type,),  # noqa: E501
            'other': (str, none_type,),  # noqa: E501
            'state_and_local_wages': ([W2StateAndLocalWages],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'document_metadata': 'document_metadata',  # noqa: E501
        'document_id': 'document_id',  # noqa: E501
        'employer': 'employer',  # noqa: E501
        'employee': 'employee',  # noqa: E501
        'tax_year': 'tax_year',  # noqa: E501
        'employer_id_number': 'employer_id_number',  # noqa: E501
        'wages_tips_other_comp': 'wages_tips_other_comp',  # noqa: E501
        'federal_income_tax_withheld': 'federal_income_tax_withheld',  # noqa: E501
        'social_security_wages': 'social_security_wages',  # noqa: E501
        'social_security_tax_withheld': 'social_security_tax_withheld',  # noqa: E501
        'medicare_wages_and_tips': 'medicare_wages_and_tips',  # noqa: E501
        'medicare_tax_withheld': 'medicare_tax_withheld',  # noqa: E501
        'social_security_tips': 'social_security_tips',  # noqa: E501
        'allocated_tips': 'allocated_tips',  # noqa: E501
        'box_9': 'box_9',  # noqa: E501
        'dependent_care_benefits': 'dependent_care_benefits',  # noqa: E501
        'nonqualified_plans': 'nonqualified_plans',  # noqa: E501
        'box_12': 'box_12',  # noqa: E501
        'statutory_employee': 'statutory_employee',  # noqa: E501
        'retirement_plan': 'retirement_plan',  # noqa: E501
        'third_party_sick_pay': 'third_party_sick_pay',  # noqa: E501
        'other': 'other',  # noqa: E501
        'state_and_local_wages': 'state_and_local_wages',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, document_metadata, document_id, employer, employee, tax_year, employer_id_number, wages_tips_other_comp, federal_income_tax_withheld, social_security_wages, social_security_tax_withheld, medicare_wages_and_tips, medicare_tax_withheld, social_security_tips, allocated_tips, box_9, dependent_care_benefits, nonqualified_plans, box_12, statutory_employee, retirement_plan, third_party_sick_pay, other, state_and_local_wages, *args, **kwargs):  # noqa: E501
        """CreditW2 - a model defined in OpenAPI

        Args:
            document_metadata (CreditDocumentMetadata):
            document_id (str): An identifier of the document referenced by the document metadata.
            employer (CreditPayStubEmployer):
            employee (CreditPayStubEmployee):
            tax_year (str, none_type): The tax year of the W2 document.
            employer_id_number (str, none_type): An employee identification number or EIN.
            wages_tips_other_comp (str, none_type): Wages from tips and other compensation.
            federal_income_tax_withheld (str, none_type): Federal income tax withheld for the tax year.
            social_security_wages (str, none_type): Wages from social security.
            social_security_tax_withheld (str, none_type): Social security tax withheld for the tax year.
            medicare_wages_and_tips (str, none_type): Wages and tips from medicare.
            medicare_tax_withheld (str, none_type): Medicare tax withheld for the tax year.
            social_security_tips (str, none_type): Tips from social security.
            allocated_tips (str, none_type): Allocated tips.
            box_9 (str, none_type): Contents from box 9 on the W2.
            dependent_care_benefits (str, none_type): Dependent care benefits.
            nonqualified_plans (str, none_type): Nonqualified plans.
            box_12 ([W2Box12]):
            statutory_employee (str, none_type): Statutory employee.
            retirement_plan (str, none_type): Retirement plan.
            third_party_sick_pay (str, none_type): Third party sick pay.
            other (str, none_type): Other.
            state_and_local_wages ([W2StateAndLocalWages]):

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

        self.document_metadata = document_metadata
        self.document_id = document_id
        self.employer = employer
        self.employee = employee
        self.tax_year = tax_year
        self.employer_id_number = employer_id_number
        self.wages_tips_other_comp = wages_tips_other_comp
        self.federal_income_tax_withheld = federal_income_tax_withheld
        self.social_security_wages = social_security_wages
        self.social_security_tax_withheld = social_security_tax_withheld
        self.medicare_wages_and_tips = medicare_wages_and_tips
        self.medicare_tax_withheld = medicare_tax_withheld
        self.social_security_tips = social_security_tips
        self.allocated_tips = allocated_tips
        self.box_9 = box_9
        self.dependent_care_benefits = dependent_care_benefits
        self.nonqualified_plans = nonqualified_plans
        self.box_12 = box_12
        self.statutory_employee = statutory_employee
        self.retirement_plan = retirement_plan
        self.third_party_sick_pay = third_party_sick_pay
        self.other = other
        self.state_and_local_wages = state_and_local_wages
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
    def __init__(self, document_metadata, document_id, employer, employee, tax_year, employer_id_number, wages_tips_other_comp, federal_income_tax_withheld, social_security_wages, social_security_tax_withheld, medicare_wages_and_tips, medicare_tax_withheld, social_security_tips, allocated_tips, box_9, dependent_care_benefits, nonqualified_plans, box_12, statutory_employee, retirement_plan, third_party_sick_pay, other, state_and_local_wages, *args, **kwargs):  # noqa: E501
        """CreditW2 - a model defined in OpenAPI

        Args:
            document_metadata (CreditDocumentMetadata):
            document_id (str): An identifier of the document referenced by the document metadata.
            employer (CreditPayStubEmployer):
            employee (CreditPayStubEmployee):
            tax_year (str, none_type): The tax year of the W2 document.
            employer_id_number (str, none_type): An employee identification number or EIN.
            wages_tips_other_comp (str, none_type): Wages from tips and other compensation.
            federal_income_tax_withheld (str, none_type): Federal income tax withheld for the tax year.
            social_security_wages (str, none_type): Wages from social security.
            social_security_tax_withheld (str, none_type): Social security tax withheld for the tax year.
            medicare_wages_and_tips (str, none_type): Wages and tips from medicare.
            medicare_tax_withheld (str, none_type): Medicare tax withheld for the tax year.
            social_security_tips (str, none_type): Tips from social security.
            allocated_tips (str, none_type): Allocated tips.
            box_9 (str, none_type): Contents from box 9 on the W2.
            dependent_care_benefits (str, none_type): Dependent care benefits.
            nonqualified_plans (str, none_type): Nonqualified plans.
            box_12 ([W2Box12]):
            statutory_employee (str, none_type): Statutory employee.
            retirement_plan (str, none_type): Retirement plan.
            third_party_sick_pay (str, none_type): Third party sick pay.
            other (str, none_type): Other.
            state_and_local_wages ([W2StateAndLocalWages]):

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

        self.document_metadata = document_metadata
        self.document_id = document_id
        self.employer = employer
        self.employee = employee
        self.tax_year = tax_year
        self.employer_id_number = employer_id_number
        self.wages_tips_other_comp = wages_tips_other_comp
        self.federal_income_tax_withheld = federal_income_tax_withheld
        self.social_security_wages = social_security_wages
        self.social_security_tax_withheld = social_security_tax_withheld
        self.medicare_wages_and_tips = medicare_wages_and_tips
        self.medicare_tax_withheld = medicare_tax_withheld
        self.social_security_tips = social_security_tips
        self.allocated_tips = allocated_tips
        self.box_9 = box_9
        self.dependent_care_benefits = dependent_care_benefits
        self.nonqualified_plans = nonqualified_plans
        self.box_12 = box_12
        self.statutory_employee = statutory_employee
        self.retirement_plan = retirement_plan
        self.third_party_sick_pay = third_party_sick_pay
        self.other = other
        self.state_and_local_wages = state_and_local_wages
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
