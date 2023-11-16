from unittest import mock
from unittest.mock import Mock

import pytest

from validations_engine.GchatHelper import GchatHelper
from validations_engine.validations_engine import ValidationsEngine


class TestValidationsEngines:
    @mock.patch.object(ValidationsEngine, "handle_errors")
    @mock.patch.object(ValidationsEngine, "set_suites_have_failures")
    @mock.patch.object(ValidationsEngine, "_get_validation_suites")
    def test_run_validation_suites(
        self,
        mock_get_validation_suites,
        mock_set_suites_have_failures,
        mock_handle_errors,
        validations_engine,
    ):
        # arrange
        mock_get_validation_suites.return_value = [Mock()]

        # act
        validations_engine.run_validation_suites()

        # assert
        mock_get_validation_suites.assert_called_once_with()
        mock_set_suites_have_failures.assert_called_once()
        mock_handle_errors.assert_called_once_with()

    @mock.patch.object(GchatHelper, "send_messages")
    @mock.patch.object(ValidationsEngine, "_get_suites_have_failures")
    def test_handle_errors_with_errors_without_slack_notification(
        self, mock_get_suites_have_failures, mock_send_slack_errors, validations_engine
    ):
        # arrange
        mock_get_suites_have_failures.return_value = True
        mock_send_slack_errors.return_value = False

        # act
        with pytest.raises(AssertionError) as e:
            validations_engine.handle_errors()

        # assert
        assert (
            str(e.value) == "One or more validations failed! (Please, check the logs)"
        )
        mock_send_slack_errors.assert_called_once_with(
            validations_engine.error_messages
        )

    @mock.patch.object(GchatHelper, "send_messages")
    @mock.patch.object(ValidationsEngine, "_get_suites_have_failures")
    def test_handle_errors_with_errors_with_slack_notification(
        self, mock_get_suites_have_failures, mock_send_slack_errors, validations_engine
    ):
        # arrange
        mock_get_suites_have_failures.return_value = True
        mock_send_slack_errors.return_value = True

        # act
        validations_engine.handle_errors()

        # assert
        mock_send_slack_errors.assert_called_once_with(
            validations_engine.error_messages
        )

    @mock.patch.object(ValidationsEngine, "_list_validation_suites_files")
    @mock.patch.object(ValidationsEngine, "_import_suite_module")
    @mock.patch.object(ValidationsEngine, "_load_suite_classes_from_module")
    def test_load_validation_suites(
        self,
        mock_load_suite_classes_from_module,
        mock_import_suite_module,
        mock_list_validation_suites_files,
        validations_engine,
    ):
        # arrange
        root_path = "/root/path"
        suite_1_path = "/foo/bar"
        suite_1_module = Mock()
        validation_classes = [Mock(), Mock()]
        mock_list_validation_suites_files.return_value = [suite_1_path]
        mock_import_suite_module.return_value = suite_1_module
        mock_load_suite_classes_from_module.return_value = validation_classes

        # act
        returned_value = validations_engine.load_validation_suites(
            validations_suites_root_path=root_path
        )

        # assert
        mock_list_validation_suites_files.assert_called_once_with(root_path)
        mock_import_suite_module.assert_called_once_with(suite_1_path)
        mock_load_suite_classes_from_module.assert_called_once_with(suite_1_module)
        assert returned_value == validation_classes

    @mock.patch("validations_engine.validations_engine.isclass")
    @mock.patch("validations_engine.validations_engine.dir")
    def test__load_suite_classes_from_module(
        self, mock_dir, mock_isclass, validations_engine
    ):
        # arrange

        module = Mock()
        mock_dir.return_value = ["FooValidationSuite", "BarValidationSuite"]
        mock_isclass.return_value = True

        # act
        returned_value = validations_engine._load_suite_classes_from_module(module)

        # assert
        assert len(returned_value) == 2

    def test_set_suites_have_failures(self, validations_engine):
        # arrange
        validations_engine._suites_have_failures = False
        new_state = True

        # act
        validations_engine.set_suites_have_failures(new_state)

        # assert
        assert validations_engine._get_suites_have_failures()
