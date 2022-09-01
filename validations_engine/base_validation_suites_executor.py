import inspect
import logging
from logging import INFO

logging.getLogger().setLevel(INFO)


class BaseValidationSuitesExecutor:
    """
    Validation suites executors abstract class.
    """

    def __init__(self, auth=None) -> None:
        self.auth = auth
        self._suite_validation_has_failures = False
        self.errors = []

    def get_suite_validation_has_failures(self) -> bool:
        return self._suite_validation_has_failures

    def get_suite_validation_failures_messages(self) -> list:
        return self.errors

    def set_suite_validation_has_failures(self, state) -> None:
        self._suite_validation_has_failures = state

    def run(self) -> None:
        """
        This is the main method executed by the validation suites
         (E.g.: FooValidationSuite).
        It runs every method prefixed with `validation_` defined in the validation suite
         class. And the default ones defined in the executor class.

        Only stops when all validations are finished.
        """

        suite_validation_methods_names = [
            attr
            for attr in dir(self)
            if inspect.ismethod(getattr(self, attr)) and attr.startswith("validate_")
        ]
        suite_class_name = type(self).__name__

        logging.info(
            f"\n\nm=run, msg=::::::::::::::::: STARTING VALIDATIONS OF SUITE: {suite_class_name} :::::::::::::::::"
        )
        for validate_method_name in suite_validation_methods_names:
            logging.info(
                f"m=run, msg=:::: EXECUTING VALIDATION: {validate_method_name}"
            )
            try:
                validate_method = getattr(self, validate_method_name)
                validate_method()

                logging.info("m=run, msg=:::: VALIDATION SUCCEEDED ::::")
            except Exception as e:
                if self.errors == [] and hasattr(self, "SLACK_MSG_HEADER"):
                    self.errors.append(
                        (self.SLACK_MSG_HEADER, self.__dict__.get("SLACK_CHANNEL"))
                    )
                default_message = f":exclamation: Error validating with {validate_method_name} on {self.__class__.__name__}"
                error_message = self.__dict__.get("SLACK_MSG", default_message)
                self.errors.append((error_message, self.__dict__.get("SLACK_CHANNEL")))

                self.set_suite_validation_has_failures(True)
                logging.error(e)
                logging.info(
                    f"m=run, msg=:::: VALIDATION {validate_method_name} FAILED (see log above for error details) ::::"
                )

        logging.info(
            f"m=run, msg=::::::::::::::::: FINISHED VALIDATIONS OF SUITE: {suite_class_name} :::::::::::::::::\n\n"
        )
