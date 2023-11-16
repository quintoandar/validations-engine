# Changelog
All notable changes to this project will be documented in this file.

Preferably use **Added**, **Changed**, **Removed** and **Fixed** topics in each release or unreleased log for a better organization.

## [2.0.0](https://github.com/quintoandar/validations-engine/releases/tag/2.0.0)
### Changed
GchatHelper and message classes were added as the main messenger service. So in this release, the errors can't be sent to Slack. In the next minor version (2.1.0), we'll add the option to choose between Slack and GChat services.
## [1.0.1](https://github.com/quintoandar/validations-engine/releases/tag/1.0.1)
### Fixed
SlackHelper send_slack_errors method returns the correct Boolean value depending on the success of messages.
## [1.0.0](https://github.com/quintoandar/validations-engine/releases/tag/1.0.0)
### Added
First modules and entities of Validations Engine package.
