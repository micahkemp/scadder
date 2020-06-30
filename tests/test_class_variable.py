from scadder import SCADClassVariable, SCADClassVariableObject, SCADClassVariableUnset, SCADClassVariableInvalidValue

import pytest


def test_set_variable():
    set_value = "some value"
    set_variable = SCADClassVariable()
    set_variable.set_value(set_value)

    assert set_variable.is_set

    assert set_variable.value == set_value


def test_unset_variable():
    unset_variable = SCADClassVariable()

    assert not unset_variable.is_set

    with pytest.raises(SCADClassVariableUnset):
        unset_variable.value


def test_invalid_variable_value():
    invalid_variable = SCADClassVariableObject()

    with pytest.raises(SCADClassVariableInvalidValue):
        invalid_variable.set_value("just a string")
