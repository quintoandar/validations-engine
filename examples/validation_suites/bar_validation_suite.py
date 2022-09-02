from examples.validation_suites.bar_custom_executor import BarCustomExecutor


class BarValidationSuite(BarCustomExecutor):
    def validate_something(self):
        self.assert_something()
