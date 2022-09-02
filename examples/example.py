"""
desc
"""
from os.path import dirname

from validations_engine.validations_engine import ValidationsEngine

EXAMPLES_FOLDER = dirname(__file__)

integrations_validator = ValidationsEngine(validations_suites_root_path=EXAMPLES_FOLDER)

# This value will be available in the suites through var `self.auth`
AUTH_PARAMS = {"some_db_conn_auth": "<credentials>"}
integrations_validator.set_connections_auth_params(connections_auth_params=AUTH_PARAMS)

integrations_validator.run_validation_suites()
