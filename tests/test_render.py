from scadder import SCADClass, SCADConfiguration, SCADClassVariable, SCADObjectFileChanged

import pytest
import tempfile


@SCADConfiguration()
class MyRenderableSCADClass(SCADClass):
    radius = SCADClassVariable()
    height = SCADClassVariable()
    # contents has very specific whitespace for testing purposes
    # if tests fail ensure there are no diffs to the whitespace here
    contents = """Radius: {{ radius.value }}

Height: {{ height.value }}
"""


my_renderable_object = MyRenderableSCADClass(name="my_renderable_object", radius=10, height=10)


@pytest.fixture(scope="module")
def temp_directory_path():
    with tempfile.TemporaryDirectory() as temp_dir_name:
        yield temp_dir_name


# first render of this object should not raise an exception
def test_render(temp_directory_path):
    my_renderable_object.render(path=temp_directory_path)

    with open(my_renderable_object.filename_at_path(temp_directory_path), "r") as rendered_file:
        rendered_contents = rendered_file.read()

        # the compared string has very specific whitespace for testing purposes
        # if tests fail ensure there are no diffs to the whitespace here
        assert rendered_contents == """
module my_renderable_object() {
    Radius: 10

    Height: 10
}"""


# second render of this object, with the same contents, should not raise an exception
def test_second_render(temp_directory_path):
    my_renderable_object.render(path=temp_directory_path)


# rendering this object after changing its render_template should raise an exception
def test_second_render(temp_directory_path):
    my_renderable_object.contents = "changed"
    with pytest.raises(SCADObjectFileChanged):
        my_renderable_object.render(path=temp_directory_path)
