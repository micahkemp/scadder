from scadder.componentswithchildren import *
from scadder.components import *
from scadder.validate import *

import pytest


@pytest.fixture
def my_cube():
    return Cube(name="my_cube", length=1, width=2, height=3)


@pytest.fixture
def my_translate(my_cube):
    return Translate(
        name="my_translate",
        children=[my_cube],
        vector_x=1,
        vector_y=2,
        vector_z=3
    )


def test_translate_rendered_contents(my_translate):
    assert my_translate.rendered_contents() == """// use modules
use <my_cube/my_cube.scad>

module my_translate() {
    translate(v=[1, 2, 3]) {
        my_cube();
    }
}

// call module when run directly
my_translate();"""
