from scadder import Component

import pytest


@pytest.fixture
def my_component():
    class MyComponent(Component):
        @property
        def arguments(self):
            return {
                # hardcoded argument because we aren't testing init variables
                "length": 10,
                "text": "10",
            }

    return MyComponent(name="my_component")


def test_argument_formatted(my_component):
    assert my_component.argument_formatted("length") == 10
    assert my_component.argument_formatted("text") == '"10"'


def test_arguments_formatted(my_component):
    assert my_component.arguments_formatted == {
        "length": 10,
        "text": '"10"',
    }


def test_argument_strings(my_component):
    assert my_component.argument_strings == [
        'length=10',
        'text="10"',
    ]


def test_arguments_string(my_component):
    assert my_component.arguments_string == 'length=10, text="10"'
