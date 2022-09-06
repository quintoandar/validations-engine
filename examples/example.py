from os.path import dirname

from validations_engine.validations_engine import ValidationsEngine

EXAMPLES_FOLDER = dirname(__file__)

# 1. instantiate the validator
integrations_validator = ValidationsEngine(validations_suites_root_path=EXAMPLES_FOLDER)

# 2. Define auth credentials you may need
# This value will be available in the suites through var `self.auth`
# Use it to share values you may need to create connections to your services
AUTH_PARAMS = {"some_db_conn_auth": "<credentials>"}
integrations_validator.set_connections_auth_params(connections_auth_params=AUTH_PARAMS)

# 3. call the main method
# this will execute all the validation suites inside the `validations_suites_root_path`
integrations_validator.run_validation_suites()

# the validation suites inside EXAMPLES_FOLDER will be run
# The failures will be printed and an error will be raised at the end if any failure occurs.
