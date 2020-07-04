from scadder.solidobject import SolidObject
from scadder.scadvariable import SCADVariable, SCADVariableMissingRequiredValue

import pytest


class BoringSolidObject(SolidObject):
    pass


def test_init_solid_object_base():
    # should not raise an exception
    my_boring_solid_object = BoringSolidObject()


class SolidObjectWithSimpleAttribute(SolidObject):
    simple_attribute = SCADVariable()


def test_init_with_simple_attribute_empty():
    # should not raise an exception with missing optional parameter
    my_simple_object = SolidObjectWithSimpleAttribute()


class SolidObjectWithRequiredAttribute(SolidObject):
    required_attribute = SCADVariable(required=True)


def test_init_with_missing_required():
    with pytest.raises(SCADVariableMissingRequiredValue):
        my_object_with_missing_required = SolidObjectWithRequiredAttribute()


def test_module_single_argument_formatted():
    my_simple_object = SolidObjectWithSimpleAttribute(simple_attribute="simple value")

    assert my_simple_object.formatted_module_arguments() == 'simple_attribute="simple value"'


class SolidObjectWithTwoArguments(SolidObject):
    arg1 = SCADVariable()
    arg2 = SCADVariable()


def test_module_two_arguments_formatted():
    my_two_arg_object = SolidObjectWithTwoArguments(arg1="just a string", arg2=1.0)

    assert my_two_arg_object.formatted_module_arguments() == 'arg1="just a string", arg2=1.0'


def test_module_call():
    my_two_arg_object = SolidObjectWithTwoArguments(arg1="just a string", arg2=1.0)

    assert my_two_arg_object.module_call() == 'SolidBaseObject(arg1="just a string", arg2=1.0)'
