from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy


class NumberInputValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "NumberInputValidationStrategy"

    @classmethod
    def validate(cls, record, field, **kwargs) -> (object, bool, str):
        if not isinstance(field, int):
            return record, False, "Invalid number input, it's not integer"
        return record, True, "Ok"
