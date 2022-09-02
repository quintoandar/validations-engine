# Adding a new validation suite

**Creating a new validation context (executor)**

If you want to create a validation for a new category (like the categories API or Database), you may first create an executor. The executor must inherit from `BaseValidationSuitesExecutor` and wrap common validation that validation suites may share. And this executor must be inherited by each validation suite you create in this context.

```python

class MyAnotherValidationSuitesExecutor(BaseValidationSuitesExecutor):

	def __init__(self):
		pass

  def method_one(self):
		pass

```

**Creating a new validation suite**

If you want to validate an existing context, like add validations for a new database type, you may only create a new validation suite file.

1 - Add the new Validation Suite file in the validation suites’ path: `/bietlejuice/jobs/composer/validation_suites` inside the most suitable folder: `database` or `api`.

2- Map the consumer class related to that suite

Every suite must inherit a validation suites executor in order to be run.

```python
# imports suppressed

# Note: the orange placeholders stand for the mappings you should do
class <suite name>ValidationSuite(DatabaseValidationSuitesExecutor):
    REPOSITORY_CONSUMER_CLASS = <consumer class>

    def validate_my_source(self):
        db_consumer = self.REPOSITORY_CONSUMER_CLASS(
            self.auth[DatabaseEnum.my_source_enum_key], SparkClient()
        )
        self._validate_connection(db_consumer)

    def validate_my_custom_validation(self):
        ... here you can add a custom other validation you might want to perform

```

**Create a new validation inside an existent validation suite**

If you want to add a validation inside an existent suite, you only need to add/map the new method inside the suite. E.g.:

```python

class MongoValidationSuite(DatabaseValidationSuitesExecutor):
    REPOSITORY_CONSUMER_CLASS = MongoConsumer

    def validate_heimdall(self):
        db_consumer = self.REPOSITORY_CONSUMER_CLASS(
            MongoClient(self.auth[DatabaseEnum.HEIMDALL]), SparkClient()
        )
        self._validate_connection(db_consumer)

    def validate_heimall_another_thing(self):
        db_consumer = self.REPOSITORY_CONSUMER_CLASS(
            MongoClient(self.auth[DatabaseEnum.US_EMAILS]), SparkClient()
        )
        result = db_consumer.validate_another_thing()
				assert result
```

For custom validations, make sure you perform an **`assert`** at the end.