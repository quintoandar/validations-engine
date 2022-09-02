from os.path import dirname

import pytest

from tests.integration.validation_suites_root_1.foo_validation_suite import (
    FooValidationSuite,
)
from tests.integration.validation_suites_root_2.bar_validation_suite import (
    BarValidationSuite,
)
from validations_engine.validations_engine import ValidationsEngine


class TestValidationsEngine:
    def test_with_no_suites(self):
        # arrange
        SUITES_TESTS_FOLDER = (
            dirname(__file__) + "/non_existent_path_validation_suites/"
        )

        integrations_validator = ValidationsEngine(
            validations_suites_root_path=SUITES_TESTS_FOLDER
        )

        # act
        integrations_validator.run_validation_suites()

        # assert
        assert not integrations_validator._get_suites_have_failures()
        assert integrations_validator.connections_auth_params == {}
        assert integrations_validator._validation_suites == []

    def test_execution_of_validation_method_of_a_suite(self):
        # arrange
        SUITES_TESTS_FOLDER = dirname(__file__) + "/validation_suites_root_1/"
        connection_params = {"key": ["<values>"]}

        integrations_validator = ValidationsEngine(
            validations_suites_root_path=SUITES_TESTS_FOLDER
        )
        integrations_validator.set_connections_auth_params(connection_params)

        # act
        integrations_validator.run_validation_suites()

        # assert
        assert not integrations_validator._get_suites_have_failures()
        assert integrations_validator.connections_auth_params == connection_params
        assert (
            integrations_validator._validation_suites[0].__name__
            == FooValidationSuite.__name__
        )

    def test_execution_of_validation_method_of_a_suit_with_errors(self):
        # arrange
        SUITES_TESTS_FOLDER = dirname(__file__) + "/validation_suites_root_2/"
        connection_params = {"key_bar": ["<values>"]}

        integrations_validator = ValidationsEngine(
            validations_suites_root_path=SUITES_TESTS_FOLDER
        )
        integrations_validator.set_connections_auth_params(connection_params)

        # act
        with pytest.raises(AssertionError) as e:
            integrations_validator.run_validation_suites()

        # assert
        assert (
            str(e.value) == "One or more validations failed! (Please, check the logs)"
        )
        assert integrations_validator._get_suites_have_failures()
        assert integrations_validator.connections_auth_params == connection_params
        assert (
            integrations_validator._validation_suites[0].__name__
            == BarValidationSuite.__name__
        )
