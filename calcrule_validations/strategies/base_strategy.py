from calcrule_validations.strategies.validation_strategy_interface import ValidationStrategyInterface
from uuid import UUID

class BaseValidationsStrategy(ValidationStrategyInterface):
    VALIDATION_CLASS = None

    @classmethod
    def check_calculation(cls, calculation, calculation_uuid):
        return UUID(calculation.uuid) == UUID(calculation_uuid)

    @classmethod
    def calculate(cls, calculation, field_name, field_value, **kwargs):
        row_validated = cls.validate(
            field_name, field_value, **kwargs
        )
        return row_validated
