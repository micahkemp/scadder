from scadder import SCADClass, SCADConfiguration, SCADClassVariable, SCADObjectFileChanged

import pytest
import tempfile


@SCADConfiguration()
class MyRenderableSCADClass(SCADClass):
    radius = SCADClassVariable()
    render_template = "Radius: {{ radius.value }}"


my_renderable_object = MyRenderableSCADClass(name="my_renderable_object", radius=10)


@pytest.fixture(scope="module")
def temp_directory_path():
    with tempfile.TemporaryDirectory() as temp_dir_name:
        yield temp_dir_name


# first render of this object should not raise an exception
def test_render(temp_directory_path):
    my_renderable_object.render(path=temp_directory_path)

    with open(my_renderable_object.filename_at_path(temp_directory_path), "r") as rendered_file:
        rendered_contents = rendered_file.read()

        assert rendered_contents == "Radius: 10"


# second render of this object, with the same contents, should not raise an exception
def test_second_render(temp_directory_path):
    my_renderable_object.render(path=temp_directory_path)


# rendering this object after changing its render_template should raise an exception
def test_second_render(temp_directory_path):
    my_renderable_object.render_template = "changed"
    with pytest.raises(SCADObjectFileChanged):
        my_renderable_object.render(path=temp_directory_path)
