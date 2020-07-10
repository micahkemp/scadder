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
    def __init__(self, name, **kwargs):
        self._call_module = "cube"
        self.size = Parameter(required=True, validator=Validators.validate_list_numeric)

        super(Cube, self).__init__(name=name, **kwargs)


class Cylinder(Component):
    """
    Cylinder
    """
    def __init__(self, name, **kwargs):
        self._call_module = "cylinder"
        self.radius = Parameter(validator=Validators.validate_numeric, template_as="r")
        self.diameter = Parameter(validator=Validators.validate_numeric, template_as="d")
        self.height = Parameter(validator=Validators.validate_numeric, template_as="h")

        super(Cylinder, self).__init__(name=name, **kwargs)
