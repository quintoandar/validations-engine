# About

## Motivation

During the daily data engineering pipeline execution, may occur some problems related to:

- Network access (like VPC, peering, etc).
- API failures.
- Database connections failures (access, authentication, networking related errors).
- Failures in Python requirements installing (via init scripts) and its dependencies installing.
- DML errors.
- and the list goes on... 😿🙈.

Eventually, internal modifications in service's platform (infra, services, etc) can lead to bugs and failures in the ELT daily runs.
Also, eventual external factors (like a lib dependency update) may also lead to such problems. And we definitely cannot
expect that everything will run accordingly on the official daily executions.

It is pretty important therefore to have internal processes to guarantee (*as much as we can*) that the pipelines will
run without failures.