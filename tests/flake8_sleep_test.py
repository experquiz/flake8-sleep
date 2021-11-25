import ast

import pytest

from flake8_sleep import Plugin


def results(s):
    return {"{}:{}: {}".format(*r) for r in Plugin(ast.parse(s)).run()}


@pytest.mark.parametrize(
    "s",
    (
        "def func():\n\treturn 1",
        "asleep(1)",
        "def my_sleep_function():\n\treturn 2",
    ),
)
def test_ok(s):
    assert results(s) == set()


def test_return_100():
    s = "sleep(1)"
    assert results(s) == {"1:0: SLP100 sleep found"}


def test_return_100_2():
    s = """
def myfunc():
    x = 1
    sleep(2)
    return x
    """
    print(s)
    assert results(s) == {"4:4: SLP100 sleep found"}


def test_return_101():
    s = """
def sleep(t):
    return t
    """

    assert results(s) == {"2:0: SLP101 sleep used as a function name."}
