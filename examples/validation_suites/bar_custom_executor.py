from validations_engine.base_validation_suites_executor import (
    BaseValidationSuitesExecutor,
)


class BarCustomExecutor(BaseValidationSuitesExecutor):
    """This Executor may be used for sharing features among two or more suites."""

    def some_shared_feature(self):
        pass

    def assert_something(self):
        assert True
