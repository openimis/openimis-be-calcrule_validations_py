import re
from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy


class EmailValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "EmailValidationStrategy"

    @classmethod
    def validate(cls, record, field, **kwargs) -> (object, bool, str):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(email_pattern, field):
            return record, True, "Valid email"
        else:
            return record, False, "Invalid email format"
