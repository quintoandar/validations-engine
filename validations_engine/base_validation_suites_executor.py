"""Suites base executor."""
import inspect
import logging
from logging import INFO
from typing import Dict, Any, List, Tuple

from validations_engine.message import Message

logging.getLogger().setLevel(INFO)


class BaseValidationSuitesExecutor:
    """Validation suites executors abstract class."""

    GCHAT_MSG_HEADER = ""

    def __init__(self, auth: Dict[str, Any] = None) -> None:
        self.auth = auth
        self._suite_validation_has_failures = False
        self.errors = []  # type: ignore

    def get_suite_validation_has_failures(self) -> bool:
        """Returns the bool state indicating if there were failures."""
        return self._suite_validation_has_failures

    def get_suite_validation_failures_messages(self) -> List[Tuple[str, str]]:
        """Return the errors list."""
        return self.errors

    def _set_suite_validation_has_failures(self, state: bool) -> None:
        self._suite_validation_has_failures = state

    def run(self) -> None:
        """
        Main method executed by the validation suites (E.g.: FooValidationSuite).

        It will run every method prefixed with `validation_` defined in the validation
         suite class. And the default ones defined in the executor class.
        Only stops when all validations are finished.
        """
        suite_validation_methods_names = [
            attr
            for attr in dir(self)
            if inspect.ismethod(getattr(self, attr)) and attr.startswith("validate_")
        ]
        suite_class_name = type(self).__name__

        logging.info(
            f"\n\nm=run, msg=::::::::::::::::: STARTING VALIDATIONS OF SUITE: "
            f"{suite_class_name} :::::::::::::::::"
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
                if self.errors == [] and hasattr(self, "GCHAT_MSG_HEADER"):
                    gchat_header_message_error = Message(
                        content=self.GCHAT_MSG_HEADER,
                        destination=self.__dict__.get("GCHAT_CHANNEL"),
                    )
                    self.errors.append(gchat_header_message_error)

                default_message = (
                    "⚠️ Error validating with "
                    f"{validate_method_name} on {self.__class__.__name__}"
                )
                error_message = self.__dict__.get("GCHAT_MSG", default_message)
                gchat_webhook = self.__dict__.get("GCHAT_CHANNEL")
                gchat_message_error = Message(
                    content=error_message, destination=gchat_webhook
                )
                self.errors.append(gchat_message_error)

                self._set_suite_validation_has_failures(True)
                logging.error(e)
                logging.info(
                    f"m=run, msg=:::: VALIDATION {validate_method_name} FAILED (see "
                    f"log above for error details) ::::"
                )

        logging.info(
            f"m=run, msg=::::::::::::::::: FINISHED VALIDATIONS OF THE SUITE: "
            f"{suite_class_name} :::::::::::::::::\n\n"
        )
