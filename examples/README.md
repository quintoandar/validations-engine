# How to use Validations Engine

```python
from validations_engine.validations_engine import ValidationsEngine

# 1. instantiate the validator
integrations_validator = ValidationsEngine(validations_suites_root_path='<validations root>')

# 2. Define auth credentials you may need
# This value will be available in the suites through var `self.auth`
# Use it to share values you may need to create connections to your services
AUTH_PARAMS = {"some_db_conn_auth": "<credentials>"}
integrations_validator.set_connections_auth_params(connections_auth_params=AUTH_PARAMS)

# 3. call the main method
# this will execute all the validation suites inside the `validations_suites_root_path`
integrations_validator.run_validation_suites()

```

The file [example.py](example.py) is the main script that implements the code above.
When it runs it will execute the validation suites of the folder `/validation_suites`.

You can check each file to acknowledge the implementation details and run the main file example.py to see the engine 
working.