from scadder import *

import pytest


@pytest.mark.parametrize("test_input,raises", [
    ([10, 10, 10], False),
    (["10", 10, 10], True),
    ([10, "10", 10], True),
    ([10, 10, "10"], True),
])
def test_cube_arguments(test_input, raises):
    length, width, height = test_input

    if raises:
        with pytest.raises(InvalidValue):
            Cube(name="cube", length=length, width=width, height=height)
    else:
        Cube(name="cube", length=length, width=width, height=height)


@pytest.fixture
def cube_1_2_3():
    return Cube(name="cube_1_2_3", length=1, width=2, height=3)


def test_cube_arguments(cube_1_2_3):
    assert cube_1_2_3.arguments == {"size": [1, 2, 3]}


def test_cube_argument_strings(cube_1_2_3):
    assert cube_1_2_3.argument_strings == ["size=[1, 2, 3]"]


def test_cube_arguments_string(cube_1_2_3):
    assert cube_1_2_3.arguments_string == "size=[1, 2, 3]"


def test_cube_name(cube_1_2_3):
    assert cube_1_2_3.name == "cube_1_2_3"


def test_cube_module_name(cube_1_2_3):
    assert cube_1_2_3.module_name == "cube"


def test_cube_rendered_contents(cube_1_2_3):
    assert cube_1_2_3.rendered_contents() == """module cube_1_2_3() {
    cube(size=[1, 2, 3]);
}

// call module when run directly
cube_1_2_3();"""


def test_cube_name_none_given():
    cube_no_name_given = Cube()

    assert cube_no_name_given.name == "cube_component"


@pytest.mark.parametrize("test_input,raises", [
    ("just a string", False),
    ("123", False),
    (123, True),
])
def test_text_arguments(test_input, raises):
    if raises:
        with pytest.raises(InvalidValue):
            Text(name="text", text=test_input)

    else:
        Text(name="text", text=test_input)


@pytest.fixture
def text_just_a_string():
    return Text(name="text", text="just a string")


def test_text_arguments(text_just_a_string):
    assert text_just_a_string.arguments == {"text": "just a string"}


def test_text_argument_formatted(text_just_a_string):
    assert text_just_a_string.argument_formatted("text") == '"just a string"'


def test_text_argument_strings(text_just_a_string):
    assert text_just_a_string.argument_strings == ['text="just a string"']


def test_text_module_name(text_just_a_string):
    assert text_just_a_string.module_name == "text"


@pytest.fixture
def text_with_quotes():
    return Text(name="text_with_quotes", text='embedded "quotes" in a string')


def test_text_with_quotes_arguments(text_with_quotes):
    assert text_with_quotes.arguments == {"text": 'embedded "quotes" in a string'}


def test_text_with_quotes_argument_formatted(text_with_quotes):
    assert text_with_quotes.argument_formatted("text") == '"embedded \\\"quotes\\\" in a string"'


def test_text_with_quotes_argument_strings(text_with_quotes):
    assert text_with_quotes.argument_strings == ["text=\"embedded \\\"quotes\\\" in a string\""]
