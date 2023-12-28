from calcrule_validations.strategies.validation_strategy_interface import ValidationStrategyInterface


class BaseValidationsStrategy(ValidationStrategyInterface):
    VALIDATION_CLASS = None

    @classmethod
    def check_calculation(cls, calculation, field_validation_class):
        return calculation.uuid == field_validation_class.uuid

    @classmethod
    def calculate(cls, calculation, row_to_validate, field, **kwargs):
        row_validated = cls.validate(
            row_to_validate, field
        )
        return row_validated
