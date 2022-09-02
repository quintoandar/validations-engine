from unittest import mock

import pytest

from validations_engine.validations_engine import ValidationsEngine


@pytest.fixture()
@mock.patch.object(ValidationsEngine, "load_validation_suites")
def validations_engine(mock_load_validation_suites):
    return ValidationsEngine(validations_suites_root_path="/foo")
