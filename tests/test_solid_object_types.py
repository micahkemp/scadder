from scadder.componenttypes import Cube, Cylinder


def test_basic_cube():
    my_cube = Cube(name="my_cube", size=[1, 2, 3])

    assert my_cube.render_contents() == \
"""module my_cube() {
    cube(size=[1, 2, 3]);
}

// call module when run directly
my_cube();"""


def test_cylinder_radius():
    my_cylinder = Cylinder(name="my_cylinder", radius=1, height=2)

    assert my_cylinder.render_contents() == \
"""module my_cylinder() {
    cylinder(h=2, r=1);
}

// call module when run directly
my_cylinder();"""


def test_cylinder_diameter():
    my_cylinder = Cylinder(name="my_cylinder", diameter=1, height=2)

    assert my_cylinder.render_contents() == \
"""module my_cylinder() {
    cylinder(d=1, h=2);
}

// call module when run directly
my_cylinder();"""
