# flake8-sleep
flake8 plugin which checks that sleep is not used
[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/asottile.flake8-2020?branchName=master)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=27&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/27/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=27&branchName=master)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/flake8-2020/master.svg)](https://results.pre-commit.ci/latest/github/asottile/flake8-2020/master)

flake8-sleeep
===========

flake8 plugin which checks for use of sleep function.

## installation

<!-- `pip install flake8-2020` -->
Until pipy release, it will have to be done using git clone and local pip install:
```shell
git clone git@github.com:Nathanmalnoury/flake8-sleep.git
pip install ./flake8-sleep
```


## flake8 codes

| Code   | Description                                            |
|--------|--------------------------------------------------------|
| SLP100 | SLP100 sleep found             |
| SLP101 | SLP101 sleep used as a function name.            |


## rationale

Using sleep function should be done carefully, as it will slow down an application. As such, one may want to mark every volountary usage of sleep with a `noqa: SLPXXX` and have a warning otherwise.
s
## as a pre-commit hook

Not available until pypi release.
