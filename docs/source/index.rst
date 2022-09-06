Validations Engine
===========================
Made with |:heart:| by the **Data Engineering** team from `QuintoAndar <https://github.com/quintoandar/>`_.

Engine for creating and running validation for general purposes

Purpose
----------

This automation engine was conceived to simulate key communication/integration lines between services that compose the
core jobs of the data engineering pipeline at QuintoAndar, to guarantee there is no failures in the pipeline (and **early catch** eventual failures).
But it can execute validations for general purposes.

Structure and the engine core concepts
--------------------------------------

This engine is composed by the Executors and the ValidationSuites.

**Executors**

Executors are responsible for executing all the respective validation suites that inherit them.
A suite can inherit a custom executor or the ``BaseValidationSuitesExecutor``.
The executor may contain default and generic code and tests for a group of suites. For example, we may have one executor
with features for validating a group of *Databases* and another for validating some *APIs*.

**Validation Suites**

A validation suite works like a Python unit test class. Once you define the validation methods (following the name pattern),
these methods will be run by the engine.

Inside the validation suite class, you may implement into the validation methods the validations you want to perform.
You can implement a custom validation inside your suite or if it is a common validation you may want to generalize it
and use a custom executor like ``DatabaseValidationSuitesExecutor`` for sharing the same validation among other suites that inherits it.
Every suite must inherit from an executor, in order to be parsed and run. So it should inherit from the
``BaseValidationSuitesExecutor`` or from a custom one (that inherits from the base executor).

The ``validation_*`` methods inside the suite and inside the executor classes will run automatically by the validation engine.


Navigation
^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   getstarted
   about
   modules
   new_validation_suite