from validations_engine.base_validation_suites_executor import (
    BaseValidationSuitesExecutor,
)


class FooValidationSuite(BaseValidationSuitesExecutor):
    """For testing success"""

    def validate_bar(self):
        assert True
