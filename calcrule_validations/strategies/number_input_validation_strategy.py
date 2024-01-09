from dataclasses import asdict
from django.utils.translation import gettext_lazy as _

from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy
from calcrule_validations.strategies.validation_strategy_interface import ValidationResult


class NumberInputValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "NumberInputValidationStrategy"

    @classmethod
    def validate(cls, field_name, field_value, **kwargs):
        try:
            converted_value = int(field_value)
            return asdict(ValidationResult(success=True, field_name=field_name, note="Ok"))
        except ValueError:
            return asdict(ValidationResult(
                success=False,
                field_name=field_name,
                note=_("Invalid number input, it's not an integer")
            ))
