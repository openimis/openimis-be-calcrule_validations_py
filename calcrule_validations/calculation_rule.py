import uuid
from calcrule_validations.config import CLASS_RULE_PARAM_VALIDATION, DESCRIPTION_CONTRIBUTION_VALUATION, FROM_TO
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType

from calcrule_validations.strategies import (
    ValidationStrategyStorage
)
from core.abs_calculation_rule import AbsCalculationRule
from core.signals import *
from core import datetime


class ValidationsCalculationRule(AbsCalculationRule):
    version = 1
    uuid = "4362f958-5894-435b-9bda-df6cadf88352"
    calculation_rule_name = "Calculation rule: validations"
    description = DESCRIPTION_CONTRIBUTION_VALUATION
    impacted_class_parameter = CLASS_RULE_PARAM_VALIDATION
    date_valid_from = datetime.datetime(2000, 1, 1)
    date_valid_to = None
    status = "active"
    from_to = FROM_TO
    type = "validations"
    sub_type = "individual"
    CLASS_NAME_CHECK = ['Individual', 'Beneficiary', 'BenefitPlan']

    signal_get_rule_name = Signal(providing_args=[])
    signal_get_rule_details = Signal(providing_args=[])
    signal_get_param = Signal(providing_args=[])
    signal_get_linked_class = Signal(providing_args=[])
    signal_calculate_event = Signal(providing_args=[])
    signal_convert_from_to = Signal(providing_args=[])

    @classmethod
    def ready(cls):
        now = datetime.datetime.now()
        condition_is_valid = (now >= cls.date_valid_from and now <= cls.date_valid_to) \
            if cls.date_valid_to else (now >= cls.date_valid_from and cls.date_valid_to is None)
        if condition_is_valid:
            if cls.status == "active":
                # register signals getParameter to getParameter signal and getLinkedClass ot getLinkedClass signal
                cls.signal_get_rule_name.connect(cls.get_rule_name, dispatch_uid="on_get_rule_name_signal")
                cls.signal_get_rule_details.connect(cls.get_rule_details, dispatch_uid="on_get_rule_details_signal")
                cls.signal_get_param.connect(cls.get_parameters, dispatch_uid="on_get_param_signal")
                cls.signal_get_linked_class.connect(cls.get_linked_class, dispatch_uid="on_get_linked_class_signal")
                cls.signal_calculate_event.connect(cls.run_calculation_rules, dispatch_uid="on_calculate_event_signal")
                cls.signal_convert_from_to.connect(cls.run_convert, dispatch_uid="on_convert_from_to")

    @classmethod
    def run_calculation_rules(
        cls, sender, validation_class, record,
        field_name, field_value, user, context, **kwargs
    ):
        return cls.calculate_if_active_for_object(validation_class, record, field_name, field_value, **kwargs)

    @classmethod
    def calculate_if_active_for_object(
        cls, validation_class, calculation_uuid,
        record, field_name, field_value, **kwargs
    ):
        if cls.active_for_object(validation_class, calculation_uuid):
            return cls.calculate(validation_class, record, field_name, field_value, **kwargs)

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
    def calculate(cls, validation_class, record, field_name, field_value, **kwargs):
        return ValidationStrategyStorage.choose_strategy(validation_class)\
            .calculate(cls, record, field_name, field_value, **kwargs)
