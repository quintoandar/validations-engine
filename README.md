# Validations Engine
_Engine for creating and running validations for general purposes._

<img height="200" src="validations_engine_logo.png" />

[![Release](https://img.shields.io/github/v/release/quintoandar/validations-engine)]((https://pypi.org/project/validations-engine/))
![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8-brightgreen.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

| Source    | Downloads                                                                                                       | Page                                                 | Installation Command                       |
|-----------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| **PyPi**  | [![PyPi Downloads](https://pepy.tech/badge/validations-engine)](https://pypi.org/project/validations-engine/) | [Link](https://pypi.org/project/validations-engine/)        | `pip install validations-engine `                  |

### Build status
| Develop                                                                     | Stable                                                                            | Documentation                                                                                                                                           | Sonar                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Test](https://github.com/quintoandar/validations-engine/workflows/Test/badge.svg) | ![Publish](https://github.com/quintoandar/validations-engine/workflows/Publish/badge.svg) | [![Documentation Status](https://readthedocs.org/projects/validations-engine/badge/?version=latest)](https://validations-engine.readthedocs.io/en/latest/?badge=latest) | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=quintoandar_validations-engine&metric=alert_status)](https://sonarcloud.io/dashboard?id=quintoandar_validations-engine) |


### Purpose
This automation engine was conceived to simulate key communication/integration lines between services that compose the 
core jobs of the data engineering pipeline at QuintoAndar, to guarantee there is no failures in the pipeline (and **early catch** eventual failures).
But it can execute validations for general purposes.

### Structure and the engine core concepts 

This engine is composed by the Executors and the ValidationSuites. 

**Executors**

Executors are responsible for executing all the respective validation suites that inherit them. 
A suite can inherit a custom executor or the `BaseValidationSuitesExecutor`.
The executor may contain default and generic code and tests for a group of suites. For example, we may have one executor 
with features for validating a group of *Databases* and another for validating some *APIs*.

**Validation Suites**

A validation suite works like a Python unit test class. Once you define the validation methods (following the name pattern), 
these methods will be run by the engine.

Inside the validation suite class, you may implement into the validation methods the validations you want to perform.
You can implement a custom validation inside your suite or if it is a common validation you may want to generalize it 
and use a custom executor like `DatabaseValidationSuitesExecutor` for sharing the same validation among other suites that inherits it. 
Every suite must inherit from an executor, in order to be parsed and run. So it should inherit from the 
`BaseValidationSuitesExecutor` or from a custom one (that inherits from the base executor). 

The `validation_*` methods inside the suite and inside the executor classes will run automatically by the validation engine.


To check library main features and full documentation you can check the [Validations Engine's Documentation](https://validations-engine.readthedocs.io/en/latest/), which is hosted by Read the Docs.

## License
[Apache License 2.0](https://github.com/quintoandar/validations-engine/blob/main/LICENSE)

## Contributing
All contributions are welcome! Feel free to open Pull Requests. Check the development and contributing **guidelines** 
described in [CONTRIBUTING.md](https://github.com/quintoandar/validations-engine/blob/main/CONTRIBUTING.md)

Made with :heart: by the **Data Engineering** team from [QuintoAndar](https://github.com/quintoandar/)
