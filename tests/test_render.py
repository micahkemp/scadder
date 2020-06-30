from pyscad import SCADClass, SCADConfiguration, SCADObjectFileChanged

import pytest
import tempfile


@SCADConfiguration()
class MyRenderableSCADClass(SCADClass):
    render_template = "blah"


my_renderable_object = MyRenderableSCADClass(name="my_renderable_object")


@pytest.fixture(scope="module")
def temp_directory_path():
    # TODO - fix dir="."
    with tempfile.TemporaryDirectory() as temp_dir_name:
        yield temp_dir_name


# first render of this object should not raise an exception
def test_render(temp_directory_path):
    my_renderable_object.render(path=temp_directory_path)


# second render of this object, with the same contents, should not raise an exception
def test_second_render(temp_directory_path):
    my_renderable_object.render(path=temp_directory_path)


# rendering this object after changing its render_template should raise an exception
def test_second_render(temp_directory_path):
    my_renderable_object.render_template = "changed"
    with pytest.raises(SCADObjectFileChanged):
        my_renderable_object.render(path=temp_directory_path)
