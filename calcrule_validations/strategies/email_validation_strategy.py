import re
from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy


class EmailValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "EmailValidationStrategy"

    @classmethod
    def validate(cls, record, field_name, field_value, **kwargs) -> (object, bool, str):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(email_pattern, field_value):
            return record, True, field_name, "Ok"
        else:
            return record, False, field_name, "Invalid email format"
