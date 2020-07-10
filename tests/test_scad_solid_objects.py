import os

from scadder.component import Component, ComponentWithChildren, ChildNotComponent
from scadder.scadvariable import SCADVariable, SCADVariableMissingRequiredValue

import pytest
import tempfile


class BoringComponent(Component):
    pass


def test_init_component():
    # should not raise an exception
    my_boring_component = BoringComponent(name="my_boring_component")


class ComponentWithSimpleAttribute(Component):
    def __init__(self, name, **kwargs):
        self.simple_attribute = SCADVariable()

        super(ComponentWithSimpleAttribute, self).__init__(name=name, **kwargs)


def test_init_with_simple_attribute_empty():
    # should not raise an exception with missing optional parameter
    my_simple_component = ComponentWithSimpleAttribute(name="my_simple_component")


class ComponentWithRequiredAttribute(Component):
    def __init__(self, name, **kwargs):
        self.required_attribute = SCADVariable(required=True)

        super(ComponentWithRequiredAttribute, self).__init__(name=name, **kwargs)


def test_init_with_missing_required():
    with pytest.raises(SCADVariableMissingRequiredValue):
        my_component_with_missing_required = ComponentWithRequiredAttribute(name="my_component_with_missing_required")


def test_module_single_argument_formatted():
    my_simple_component = ComponentWithSimpleAttribute(name="my_simple_component", simple_attribute="simple value")

    assert my_simple_component.formatted_call_module_arguments() == 'simple_attribute="simple value"'


class ComponentWithTwoArguments(Component):
    def __init__(self, name, **kwargs):
        self.arg1 = SCADVariable()
        self.arg2 = SCADVariable()

        super(ComponentWithTwoArguments, self).__init__(name=name, **kwargs)


def test_module_two_arguments_formatted():
    my_two_arg_component = ComponentWithTwoArguments(name="my_two_arg_component", arg1="just a string", arg2=1.0)

    assert my_two_arg_component.formatted_call_module_arguments() == 'arg1="just a string", arg2=1.0'


def test_module_arguments_formatted_missing():
    my_two_arg_component = ComponentWithTwoArguments(name="my_two_arg_component", arg2="arg2 string")

    assert my_two_arg_component.formatted_call_module_arguments() == 'arg2="arg2 string"'


def test_module_call():
    my_two_arg_component = ComponentWithTwoArguments(name="my_two_arg_component", arg1="just a string", arg2=1.0)

    assert my_two_arg_component.formatted_call_module() == 'Component(arg1="just a string", arg2=1.0)'


def test_object_child():
    my_component = Component(name="my_component")

    my_component_with_children = ComponentWithChildren(name="my_component_with_children", children=[my_component])


def test_non_component_child():
    with pytest.raises(ChildNotComponent):
        my_component_with_children = ComponentWithChildren(name="my_component_with_children", children=["just a string"])


def test_component_render_contents():
    my_component = Component(name="my_component")
    assert my_component.render_contents() == \
"""module my_component() {
    Component();
}

// call module when run directly
my_component();"""


def test_component_with_children_render_contents():
    my_child = Component(name="my_component")
    my_component_with_children = ComponentWithChildren(name="my_component_with_children", children=[my_child])

    assert my_component_with_children.render_contents() == \
"""// use modules
use <my_component/my_component.scad>

module my_component_with_children() {
    Component() {
        my_component();
    }
}

// call module when run directly
my_component_with_children();"""


@pytest.fixture(scope="module")
def temp_directory_path():
    with tempfile.TemporaryDirectory() as temp_dir_name:
        yield temp_dir_name


def test_render(temp_directory_path):
    my_child = Component(name="my_child")
    my_component = ComponentWithChildren(name="my_component", children=[my_child])

    assert not my_component.is_rendered(path=temp_directory_path)
    assert not my_child.is_rendered(path=os.path.join(temp_directory_path, my_child.module_name))

    my_component.render(output_path=temp_directory_path)

    assert my_component.is_rendered(path=temp_directory_path)
    assert my_child.is_rendered(path=os.path.join(temp_directory_path, my_child.module_name))

    with open(my_component.filename_at_path(temp_directory_path), "r") as rendered_file:
        rendered_contents = rendered_file.read()

        assert rendered_contents == my_component.render_contents()
