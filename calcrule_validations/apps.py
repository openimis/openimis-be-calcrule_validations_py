import importlib
import inspect
from django.apps import AppConfig
from calculation.apps import CALCULATION_RULES
from calculation.apps import read_all_calculation_rules


MODULE_NAME = "calcrule_validations"
DEFAULT_CFG = {}




class CalcruleValidationsConfig(AppConfig):
    name = MODULE_NAME

    def ready(self):
        from core.models import ModuleConfiguration
        cfg = ModuleConfiguration.get_or_default(MODULE_NAME, DEFAULT_CFG)
        read_all_calculation_rules(MODULE_NAME, CALCULATION_RULES )

