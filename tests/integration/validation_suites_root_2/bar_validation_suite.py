from validations_engine.base_validation_suites_executor import (
    BaseValidationSuitesExecutor,
)


class BarValidationSuite(BaseValidationSuitesExecutor):
    """For testing failure"""

    def validate_foo(self):
        assert False
