"""Validations Engine main class."""
import importlib
import pathlib
import sys
from glob import glob
from inspect import isclass
from os.path import dirname
from types import ModuleType
from typing import List, Any, Dict

from validations_engine.GchatHelper import GchatHelper
from validations_engine.message import Message
from validations_engine.base_validation_suites_executor import (
    BaseValidationSuitesExecutor,
)


class ValidationsEngine:
    """
    The Validator engine main file.

    This class is responsible for parsing all validation suites and running
     its validation methods individually.
    """

    def __init__(self, validations_suites_root_path: str):
        self._validation_suites = self.load_validation_suites(
            validations_suites_root_path
        )
        # Stores all auth params for conn validations
        self.connections_auth_params = {}  # type: ignore
        # Controls validations state
        self._suites_have_failures = False
        self.error_messages = []  # type: ignore

    @staticmethod
    def _list_validation_suites_files(validations_suites_root_path: str) -> List[str]:
        """
        Lists all the validation suites files inside root.

        Searches for any file `*_validation_suite.py` anywhere below root path.
        """
        validation_suites_classes_pattern = (
            f"{validations_suites_root_path}/**/*_validation_suite.py"
        )
        validation_suites_files = glob(
            validation_suites_classes_pattern, recursive=True
        )
        return validation_suites_files

    @staticmethod
    def _import_suite_module(suite_file_path: str) -> ModuleType:
        """
        Imports each suite's module.

        Dynamically loads the file's module into system registered modules
         and returns its reference.
        """
        module_path = dirname(suite_file_path)

        # We need to append the path into the sys.paths, so its module can be
        #  found by importlib.import_module
        sys.path.append(module_path)

        # Get the module name and import it
        module_name = pathlib.Path(suite_file_path).stem
        module = importlib.import_module(module_name)

        return module

    @staticmethod
    def _load_suite_classes_from_module(
        module: ModuleType,
    ) -> List[BaseValidationSuitesExecutor]:
        """Parses and loads the *Suite classes from module."""
        validation_suites_classes = []
        for class_name in dir(module):
            if class_name.endswith("Suite") and isclass(getattr(module, class_name)):
                validation_suites_classes.append(getattr(module, class_name))

        return validation_suites_classes

    def load_validation_suites(
        self, validations_suites_root_path: str
    ) -> List[BaseValidationSuitesExecutor]:
        """
        Import suites' modules and loads a list with their classes.

        Get each suite file, imports it as a python module and loads the
         suite class.
        """
        all_validation_suites_classes = []
        for suite_path in self._list_validation_suites_files(
            validations_suites_root_path
        ):
            module = self._import_suite_module(suite_path)
            validation_suites_classes = self._load_suite_classes_from_module(module)
            all_validation_suites_classes.extend(validation_suites_classes)

        return all_validation_suites_classes

    def set_suites_have_failures(
        self, param: bool, messages: List[Message] = None
    ) -> None:
        """Merges previous state with new one."""
        self._suites_have_failures |= param
        if messages:
            self.error_messages.extend(messages)

    def _get_suites_have_failures(self) -> bool:
        return self._suites_have_failures

    def set_connections_auth_params(
        self, connections_auth_params: Dict[str, Any]
    ) -> None:
        """Setter of connections_auth_params."""
        self.connections_auth_params = connections_auth_params

    def _get_validation_suites(self) -> List[BaseValidationSuitesExecutor]:
        return self._validation_suites

    def handle_errors(self) -> None:
        """Ensures (raises) a failure in the end of all validations."""
        if self._get_suites_have_failures():
            send_status = GchatHelper.send_messages(self.error_messages)

            if not send_status or any(
                error.destination is None for error in self.error_messages
            ):
                raise AssertionError(
                    "One or more validations failed! (Please, check the logs)"
                )

    def run_validation_suites(self) -> None:
        """
        The main method.

        Runs all validations from Suite classes and raises an error if some
         validation failed.
        """
        for validation_suite in self._get_validation_suites():
            v = validation_suite(auth=self.connections_auth_params)  # type: ignore
            v.run()
            self.set_suites_have_failures(
                v.get_suite_validation_has_failures(),
                v.get_suite_validation_failures_messages(),
            )

        self.handle_errors()
