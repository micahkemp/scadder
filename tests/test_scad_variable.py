from scadder.scadvariable import *
from scadder.validators import Validators

import pytest


def test_class_loads():
    my_variable = SCADVariable()


def test_set_get_value():
    my_variable = SCADVariable()
    my_value = "just a value"
    my_variable.value = my_value
    assert my_variable.value == my_value


def test_raises_required():
    my_variable = SCADVariable(required=True)

    with pytest.raises(SCADVariableMissingRequiredValue):
        my_variable.value


def test_set_numeric():
    my_variable = SCADVariable(validator=Validators.validate_numeric)

    # none of these should raise an exception
    my_variable.value = 1
    my_variable.value = 1.0
    my_variable.value = -1
    my_variable.value = 0


def test_set_non_numeric_raises_invalid():
    my_variable = SCADVariable(validator=Validators.validate_numeric)

    with pytest.raises(SCADVariableInvalidValueSet):
        my_variable.value = "just a string"
