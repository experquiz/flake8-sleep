flake8-sleep
===========

flake8 plugin which checks for use of sleep function.

## installation
Using Pypi:
```shell
pip install flake8-sleep
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

```
-   repo: https://github.com/pycqa/flake8
    rev: 3.7.8
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-sleep]
```
