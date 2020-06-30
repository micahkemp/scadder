from pyscad import SCADConfiguration
from pyscad import SCADClassVariable
from pyscad import SCADClass

import pytest


@SCADConfiguration()
class MySCADClass(SCADClass):
    my_class_variable = SCADClassVariable(default="default_value")


def test_default():
    my_scad_class_obj = MySCADClass()

    assert my_scad_class_obj.my_class_variable.value == "default_value"


def test_assigned():
    my_scad_class_obj = MySCADClass(my_class_variable="instance_value")

    assert my_scad_class_obj.my_class_variable.value == "instance_value"


class MyUndecoratedSCADClass(SCADClass):
    test_has_default_value = SCADClassVariable()


def test_undecorated():
    with pytest.raises(Exception):
        MyUndecoratedSCADClass()
