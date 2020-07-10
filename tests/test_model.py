import pytest
import tempfile

from scadder.model import Model
from scadder.componenttypes import Cube


def test_unimplemented_component():
    my_model = Model(name="my_model")

    with pytest.raises(NotImplementedError):
        my_model.component()


class ImplementsComponentModel(Model):
    def component(self):
        return Cube(name="my_model", size=[10, 10, 10])


@pytest.fixture(scope="module")
def temp_directory_path():
    with tempfile.TemporaryDirectory() as temp_dir_name:
        yield temp_dir_name


def test_implemented_component(temp_directory_path):
    my_implements_component_model = ImplementsComponentModel(name="my_implements_component_model")

    my_implements_component_model.render(output_path=temp_directory_path)
