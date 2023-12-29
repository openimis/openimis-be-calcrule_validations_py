from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy


class NumberInputValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "NumberInputValidationStrategy"

    @classmethod
    def validate(cls, record, field_name, field_value, **kwargs) -> (object, bool, str):
        try:
            converted_value = int(field_value)
            return record, True, field_name, "Ok"
        except ValueError:
            return record, False, field_name, "Invalid number input, it's not an integer"
