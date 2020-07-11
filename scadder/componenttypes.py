"""
Collection of Component implementations
"""
from .component import Component, ComponentWithChildren
from .parameter import Parameter
from .validators import Validators


class Cube(Component):
    """
    Cube
    """
    _call_module = "cube"
    size = Parameter(required=True, validator=Validators.validate_list_numeric)


class Cylinder(Component):
    """
    Cylinder
    """
    _call_module = "cylinder"
    radius = Parameter(validator=Validators.validate_numeric, template_as="r")
    diameter = Parameter(validator=Validators.validate_numeric, template_as="d")
    height = Parameter(validator=Validators.validate_numeric, template_as="h")


class Translate(ComponentWithChildren):
    """
    Translate
    """
    _call_module = "translate"
    vector = Parameter(
        required=True,
        validator=Validators.validate_list_numeric,
        template_as="v"
    )


class Union(ComponentWithChildren):
    """
    Union
    """
    _call_module = "union"


class Difference(ComponentWithChildren):
    """
    Difference
    """
    _call_module = "difference"


class Mirror(ComponentWithChildren):
    """
    Mirror
    """
    _call_module = "mirror"

    vector = Parameter(
        required=True,
        validator=Validators.validate_list_numeric,
        template_as="v"
    )


class Rotate(ComponentWithChildren):
    """
    Rotate
    """
    _call_module = "rotate"

    angle = Parameter(
        required=True,
        validator=Validators.validate_numeric,
        template_as="a"
    )

    vector = Parameter(
        required=True,
        validator=Validators.validate_list_numeric,
        template_as="v"
    )


class RotateExtrude(ComponentWithChildren):
    """
    RotateExtrude
    """
    _call_module = "rotate_extrude"

    angle = Parameter(
        required=True,
        validator=Validators.validate_numeric
    )


class Circle(Component):
    """
    Circle
    """
    _call_module = "circle"

    radius = Parameter(
        required=True,
        validator=Validators.validate_numeric,
        template_as="r"
    )
