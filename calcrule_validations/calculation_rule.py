import uuid
from calcrule_validations.config import CLASS_RULE_PARAM_VALIDATION, DESCRIPTION_CONTRIBUTION_VALUATION, FROM_TO
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType

from calcrule_validations.strategies import (
    ValidationStrategyStorage
)
from core.abs_calculation_rule import AbsStrategy
from core.signals import *
from core import datetime


class ValidationsCalculationRule(AbsStrategy):
    version = 1
    uuid = "4362f958-5894-435b-9bda-df6cadf88352"
    calculation_rule_name = "Calculation rule: validations"
    description = DESCRIPTION_CONTRIBUTION_VALUATION
    impacted_class_parameter = CLASS_RULE_PARAM_VALIDATION
    date_valid_from = datetime.datetime(2000, 1, 1)
    date_valid_to = None
    status = "pasive"
    from_to = FROM_TO
    type = "validations"
    sub_type = "individual"
    CLASS_NAME_CHECK = ['Individual', 'Beneficiary', 'BenefitPlan']


    @classmethod
    def run_calculation_rules(
        cls, sender, validation_class,
        user, context, **kwargs
    ):
        field_name = kwargs.pop('field_name')
        field_value = kwargs.pop('field_value')
        return cls.calculate_if_active_for_object(
            validation_class,
            field_name=field_name,
            field_value=field_value,
            **kwargs
        )

    @classmethod
    def calculate_if_active_for_object(
        cls, validation_class, calculation_uuid, **kwargs
    ):
        field_name = kwargs.pop('field_name')
        field_value = kwargs.pop('field_value')
        if cls.active_for_object(validation_class, calculation_uuid):
            return cls.calculate(validation_class, field_name, field_value, **kwargs)

    @classmethod
    def active_for_object(cls, validation_class, calculation_uuid):
        return cls.check_calculation(validation_class, calculation_uuid)

    @classmethod
    def get_linked_class(cls, sender, class_name, **kwargs):
        return ["Calculation"]

    @classmethod
    def check_calculation(cls, validation_class, calculation_uuid, **kwargs):
        return ValidationStrategyStorage.choose_strategy(validation_class).check_calculation(cls, calculation_uuid)

    @classmethod
    def calculate(cls, validation_class, field_name, field_value, **kwargs):
        return ValidationStrategyStorage.choose_strategy(validation_class)\
            .calculate(cls, field_name, field_value, **kwargs)
