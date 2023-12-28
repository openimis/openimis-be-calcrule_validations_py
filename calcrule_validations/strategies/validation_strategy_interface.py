class ValidationStrategyInterface:

    VALIDATION_OBJECT = None

    @classmethod
    def check_calculation(cls, calculation, field_validation_class):
        pass

    @classmethod
    def calculate(cls, calculation, benefit_plan, **kwargs):
        pass

    @classmethod
    def validate(cls, record, field, **kwargs):
        pass
