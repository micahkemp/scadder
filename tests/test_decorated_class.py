from pyscad import SCADConfiguration
from pyscad import SCADClassVariable
from pyscad import SCADClass, UndecoratedSCADClass, SCADClassMissingRequiredArgument

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


@SCADConfiguration()
class MyRequiredArgSCADClass(SCADClass):
    my_required_arg = SCADClassVariable(required=True)
    my_optional_arg = SCADClassVariable()


def test_missing_required():
    with pytest.raises(SCADClassMissingRequiredArgument):
        my_scad_class_obj = MyRequiredArgSCADClass()


def test_missing_optional():
    # just make sure this doesn't throw an exception
    my_scad_class_obj = MyRequiredArgSCADClass(my_required_arg="Who Cares")


class MyUndecoratedSCADClass(SCADClass):
    test_has_default_value = SCADClassVariable()


def test_undecorated():
    with pytest.raises(UndecoratedSCADClass):
        MyUndecoratedSCADClass()
