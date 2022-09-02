from validations_engine.base_validation_suites_executor import (
    BaseValidationSuitesExecutor,
)


class FooValidationSuite(BaseValidationSuitesExecutor):
    # TODO add slack example

    def validate_something_false(self):
        # this will raise an error but the other validation will also be executed
        x = 1 / 0

    def validate_something_true(self):
        assert True

    def validate_my_conn(self):
        # You can use the self.auth values here to validate some connection
        client = PostgresClient(auth=self.auth["my_postgres_db_auth"])
        client.fetch_tables()
