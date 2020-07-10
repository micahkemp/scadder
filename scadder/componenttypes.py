"""
Collection of Component implementations
"""
from .component import Component
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
