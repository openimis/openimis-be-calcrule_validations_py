from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy


class NumberInputValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "NumberInputValidationStrategy"

    @classmethod
    def validate(cls, record, field, **kwargs) -> (object, bool, str):
        try:
            converted_value = int(field)
            return record, True, "Ok"
        except ValueError:
            return record, False, "Invalid number input, it's not an integer"
