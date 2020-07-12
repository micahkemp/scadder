from scadder.parameter import *
from scadder.validators import Validators

import pytest


def test_class_loads():
    my_variable = Parameter()


def test_set_get_value():
    my_variable = Parameter()
    my_value = "just a value"
    my_variable.value = my_value
    assert my_variable.value == my_value


def test_raises_required():
    my_variable = Parameter(required=True)

    with pytest.raises(ParameterMissingRequiredValue):
        my_variable.value


def test_set_numeric():
    my_variable = Parameter(validator=Validators.validate_numeric)

    # none of these should raise an exception
    my_variable.value = 1
    my_variable.value = 1.0
    my_variable.value = -1
    my_variable.value = 0


def test_set_non_numeric_raises_invalid():
    my_variable = Parameter(validator=Validators.validate_numeric)

    with pytest.raises(ParameterInvalidValueSet):
        my_variable.value = "just a string"


def test_set_list():
    my_variable = Parameter(validator=Validators.validate_list_numeric)

    # none of these should raise an exception
    my_variable.value = []
    my_variable.value = [1, 2.0, -1]


def test_set_non_list():
    my_variable = Parameter(validator=Validators.validate_list_numeric)

    with pytest.raises(ParameterInvalidValueSet):
        my_variable.value = "not a list"


def test_set_list_non_numeric():
    my_variable = Parameter(validator=Validators.validate_list_numeric)

    with pytest.raises(ParameterInvalidValueSet):
        my_variable.value = ["not a number"]


def test_set_list_list_numeric():
    my_variable = Parameter(validator=Validators.validate_list_list_numeric)

    my_variable.value = [[1, 2, 3], [3, 4, 5]]


def test_set_list_non_list():
    my_variable = Parameter(validator=Validators.validate_list_list_numeric)

    with pytest.raises(ParameterInvalidValueSet):
        my_variable.value = [1, 2, 3]


def test_set_list_list_non_numeric():
    my_variable = Parameter(validator=Validators.validate_list_list_numeric)

    with pytest.raises(ParameterInvalidValueSet):
        my_variable.value = [[1, 2, 3], ["1", 2, 3]]


def test_formatted_number():
    my_variable = Parameter()

    my_variable.value = 1.0

    assert my_variable.formatted_value == 1.0


def test_formatted_string():
    my_variable = Parameter()

    my_variable.value = "just a string"

    assert my_variable.formatted_value == '"just a string"'


def test_formatted_list_numbers():
    my_variable = Parameter()

    my_variable.value = [1.0, 2, -1, "and a string"]

    assert my_variable.formatted_value == "[1.0, 2, -1, 'and a string']"


def test_formatted_unknown():
    my_variable = Parameter()

    my_variable.value = None

    with pytest.raises(ParameterUnknownValueType):
        assert my_variable.formatted_value == None
