import pytest
import tempfile

from scadder.component import Component, ComponentWithChildren, RenderedFileChanged


@pytest.fixture
def temp_directory_path():
    with tempfile.TemporaryDirectory() as temp_dir_name:
        yield temp_dir_name


@pytest.fixture
def basic_component_class():
    class BasicComponent(Component):
        pass

    return BasicComponent


@pytest.fixture
def basic_component(basic_component_class):
    return basic_component_class()


def test_component_is_rendered(basic_component, temp_directory_path):
    assert not basic_component.is_rendered(temp_directory_path)
    basic_component.render(temp_directory_path)
    assert basic_component.is_rendered(temp_directory_path)


@pytest.fixture
def basic_component_with_children_class():
    class BasicComponentWithChildren(ComponentWithChildren):
        pass

    return BasicComponentWithChildren


def test_component_with_children_is_rendered(basic_component_with_children_class, basic_component, temp_directory_path):
    basic_component_with_children = basic_component_with_children_class(children=[basic_component])

    assert not basic_component_with_children.is_rendered(temp_directory_path)
    basic_component_output_path = basic_component_with_children.child_output_path(basic_component, temp_directory_path)
    assert not basic_component.is_rendered(basic_component_output_path)

    basic_component_with_children.render(temp_directory_path)

    assert basic_component_with_children.is_rendered(temp_directory_path)
    assert basic_component.is_rendered(basic_component_output_path)


def test_rendered_file_changed(basic_component, temp_directory_path):
    basic_component.render(temp_directory_path)
    basic_component.add_argument("new_argument", "new_value")
    with pytest.raises(RenderedFileChanged):
        basic_component.render(temp_directory_path)
