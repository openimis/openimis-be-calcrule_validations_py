import re
from dataclasses import asdict
from django.utils.translation import gettext_lazy as _

from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy
from calcrule_validations.strategies.validation_strategy_interface import ValidationResult


class EmailValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "EmailValidationStrategy"

    @classmethod
    def validate(cls, field_name, field_value, **kwargs):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(email_pattern, field_value):
            return asdict(ValidationResult(success=True, field_name=field_name, note=_("Ok")))
        else:
            return asdict(ValidationResult(success=False, field_name=field_name, note=_("Invalid email format")))
