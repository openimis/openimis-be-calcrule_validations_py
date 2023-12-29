import re

from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy


class PhoneNumberValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "PhoneNumberValidationStrategy"

    @classmethod
    def validate(cls, record, field_name, field_value, **kwargs) -> (object, bool, str):
        if not isinstance(field_value, str):
            return record, False, 'Field is not a valid phone number'
        pattern = r"^\+\d{2,3}\d+$"
        is_valid = bool(re.match(pattern, field_value))
        return (record, is_valid, field_name, 'Ok') if is_valid else (record, is_valid, field_name, 'Field is not a valid phone number')
