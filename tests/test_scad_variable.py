from scadder.scadvariable import *

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

    with pytest.raises(SCADMissingRequiredValue):
        my_variable.value
