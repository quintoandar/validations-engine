# Validations Engine
_Engine for creating and running validation suites for general purposes_

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
| ![Test](https://github.com/quintoandar/validations-engine/workflows/Test/badge.svg) | ![Publish](https://github.com/quintoandar/validations-engine/workflows/Publish/badge.svg) | [![Documentation Status](https://readthedocs.org/projects/validations-engine/badge/?version=latest)](https://validations-engine.readthedocs.io/en/latest/?badge=latest) | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=validations-engine&metric=alert_status)](https://sonarcloud.io/dashboard?id=validations-engine) |

To check library main features you can check [Validations Engine's Documentation](https://validations-engine.readthedocs.io/en/latest/), which is hosted by Read the Docs.

### Purpose

**Simulate** key communication/integration lines between services that compose our ELT jobs, to guarantee there is no failures in the pipeline (and **early catch** eventual failures).

### **Why?**

During the pipeline execution every day early mornings, we usually have some problems related to:

- Network access (like VPC, peering, etc)
- API failures
- Database connections failures (access, authentication, networking related errors)
- Failures in Python requirements installing (via init scripts) and its dependencies installing
- DML errors
- and the list goes on 😿 🙈

Eventually, there are modifications in Quintoandar's platform (infra, services, etc) that lead to bugs and failures in the ELT daily runs. Also, eventual external factors (like a lib dependency update) may also lead to such problems. And we definitely cannot rely on the official daily executions to validate if everything will run accordingly.

It is pretty important therefore that we have some internal validation processes to guarantee (*as much as we can*) that the pipeline will run without failures the next day. For example, we can be proactive and force the errors before the moment they are supposed to happen by simulating some operations we are supposed to do in our ELT Spark Jobs.

### Engine core concepts

**Executors**

Executors are responsible for executing all the respective validation suites that inherit them (because it inherits from `BaseValidationSuitesExecutor`).
Also, they may contain default and generic code and tests for a group of suites.

We may have executors for validating *Databases* and another for validating *APIs* for example.

**Validation Suites**

A validation suite works like a python unit test class. You may define validation methods following the name pattern and these methods will be run.

Inside the validation suite, you may define the validation methods you want to implement, for each source for example.
You are free to implement a custom validation inside your suite, but if this is a common validation we may want to generalize it and use the `DatabaseValidationSuitesExecutor` for doing the validation. Every suite must inherit from an executor, in order to be parsed and executed.

The `validation_*` methods inside the suite and inside the executor classes will run automatically by the validation engine.

## License
[Apache License 2.0](https://github.com/quintoandar/validations-engine/blob/main/LICENSE)

## Contributing
All contributions are welcome! Feel free to open Pull Requests. Check the development and contributing **guidelines** 
described in [CONTRIBUTING.md](https://github.com/quintoandar/validations-engine/blob/main/CONTRIBUTING.md)

Made with :heart: by the **Data Engineering** team from [QuintoAndar](https://github.com/quintoandar/)
