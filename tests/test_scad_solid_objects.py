from scadder.solidobject import SolidObject, SolidObjectWithChildren, ChildNotSolidObject
from scadder.scadvariable import SCADVariable, SCADVariableMissingRequiredValue

import pytest


class BoringSolidObject(SolidObject):
    pass


def test_init_solid_object_base():
    # should not raise an exception
    my_boring_solid_object = BoringSolidObject(name="my_boring_solid_object")


class SolidObjectWithSimpleAttribute(SolidObject):
    def __init__(self, name, **kwargs):
        self.simple_attribute = SCADVariable()

        super(SolidObjectWithSimpleAttribute, self).__init__(name=name, **kwargs)


def test_init_with_simple_attribute_empty():
    # should not raise an exception with missing optional parameter
    my_simple_object = SolidObjectWithSimpleAttribute(name="my_simple_object")


class SolidObjectWithRequiredAttribute(SolidObject):
    def __init__(self, name, **kwargs):
        self.required_attribute = SCADVariable(required=True)

        super(SolidObjectWithRequiredAttribute, self).__init__(name=name, **kwargs)


def test_init_with_missing_required():
    with pytest.raises(SCADVariableMissingRequiredValue):
        my_object_with_missing_required = SolidObjectWithRequiredAttribute(name="my_object_with_missing_required")


def test_module_single_argument_formatted():
    my_simple_object = SolidObjectWithSimpleAttribute(name="my_simple_object", simple_attribute="simple value")

    assert my_simple_object.formatted_call_module_arguments() == 'simple_attribute="simple value"'


class SolidObjectWithTwoArguments(SolidObject):
    def __init__(self, name, **kwargs):
        self.arg1 = SCADVariable()
        self.arg2 = SCADVariable()

        super(SolidObjectWithTwoArguments, self).__init__(name=name, **kwargs)


def test_module_two_arguments_formatted():
    my_two_arg_object = SolidObjectWithTwoArguments(name="my_two_arg_object", arg1="just a string", arg2=1.0)

    assert my_two_arg_object.formatted_call_module_arguments() == 'arg1="just a string", arg2=1.0'


def test_module_arguments_formatted_missing():
    my_two_arg_object = SolidObjectWithTwoArguments(name="my_two_arg_object", arg2="arg2 string")

    assert my_two_arg_object.formatted_call_module_arguments() == 'arg2="arg2 string"'


def test_module_call():
    my_two_arg_object = SolidObjectWithTwoArguments(name="my_two_arg_object", arg1="just a string", arg2=1.0)

    assert my_two_arg_object.formatted_call_module() == 'SolidBaseObject(arg1="just a string", arg2=1.0)'


def test_object_child():
    my_solid_object = SolidObject(name="my_solid_object")

    my_object_with_children = SolidObjectWithChildren(name="my_object_with_children", children=[my_solid_object])


def test_non_object_child():
    with pytest.raises(ChildNotSolidObject):
        my_object_with_children = SolidObjectWithChildren(name="my_object_with_children", children=["just a string"])
