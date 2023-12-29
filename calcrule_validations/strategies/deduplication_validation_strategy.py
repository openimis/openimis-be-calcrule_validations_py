from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy
from social_protection.models import Beneficiary


class DeduplicationValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "DeduplicationValidationStrategy"

    @classmethod
    def validate(cls, record, field_name, field_value, **kwargs) -> (object, bool, str):
        benefit_plan = kwargs.get('benefit_plan', None)
        # Query existing beneficiaries where is_deleted=False
        existing_beneficiaries = Beneficiary.objects.filter(benefit_plan__id=benefit_plan, is_deleted=False)
        # Check if the field value is duplicated among existing beneficiaries
        duplicates = [
            beneficiary.id for beneficiary in existing_beneficiaries
            if beneficiary.json_ext.get(f'{field_name}') == field_value
        ]
        # Flag duplication in json_ext if duplicates are found
        if duplicates:
            record = {} if record is None else record
            record['duplication_notes'] = {
                'duplicated': True,
                'duplicated_id': duplicates
            }
            return record, True, field_name, f"'{field_name}' Field value '{field_value}' is duplicated"

        return record, False, field_name, f" '{field_name}' Field value '{field_value}' is not duplicated"
