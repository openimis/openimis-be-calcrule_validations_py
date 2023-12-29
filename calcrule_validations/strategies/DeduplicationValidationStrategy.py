from calcrule_validations.strategies.base_strategy import BaseValidationsStrategy
from social_protection.models import Beneficiary


class DeduplicationValidationStrategy(BaseValidationsStrategy):
    VALIDATION_CLASS = "DeduplicationValidationStrategy"

    @classmethod
    def validate(cls, record, field, **kwargs) -> (object, bool, str):
        # Query existing beneficiaries where is_deleted=False
        existing_beneficiaries = Beneficiary.objects.filter(is_deleted=False)

        # Check if the field value is duplicated among existing beneficiaries
        duplicates = [
            beneficiary.id for beneficiary in existing_beneficiaries
            if getattr(beneficiary, 'field_name') == field  # Replace 'field_name' with the actual field name
        ]

        # Flag duplication in json_ext if duplicates are found
        if duplicates:
            record['json_ext'] = {
                'duplicated': True,
                'duplicated_id': duplicates
            }
            return record, True, f"Field value '{field}' is duplicated"

        return record, False, f"Field value '{field}' is not duplicated"
