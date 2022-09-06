# Adding a new validation suite

**Creating a new validation context (executor)**

If you want to create a validation for a new category (like the categories API or Database), you may first create an executor. 
The executor must inherit from `BaseValidationSuitesExecutor` and wrap common validation that validation suites may share. 
And this executor must be inherited by each validation suite you create in this context.
E.g.: 

```python
from validations_engine.base_validation_suites_executor import BaseValidationSuitesExecutor

class DatabasesValidationSuitesExecutor(BaseValidationSuitesExecutor):

    def __init__(self, auth):
        """
        :param auth: Authentication dictionary with DB auth needed for connecting in your test.
         You should define it after calling instantiating the ValidationsEngine(). 
         After this, it is automatically filled in this executor by the Validation Engine.
        """
        super().__init__()
        self.auth = auth

    def method_one(self):
        # some code you use in this executor
        pass


    def validation_foo(self):
        # some validation which all the suites of this executor will have
        pass
```

**Creating a new validation suite**

If you want to validate something of an existing context, like add validations for a new database type, you may only create a new validation suite file.

1. Add the new Validation Suite class file in your validation suites' root path.

2. Inherit it from some executor or from the base executor.

3. Create the validations inside each method prefixed with `validate_`.


E.g.:

```python
# imports suppressed
class MyCoolValidationSuite(APIValidationSuitesExecutor):
    # Every suite must inherit a validation suites executor in order to be run.
    
    def validate_auth(self):
        # checking if the API is authenticating and returning data as expected
        conn = self.api_client(self.auth['user'], self.auth['passwd'])
        res = conn.get_some_data()
        assert res.code == 200
```

Make sure you perform an **`assert`** at the end to be sure of your validation.

Felt something is missing? Open an issue and we shall make it clearer =]