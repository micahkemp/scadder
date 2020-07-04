"""
Collection of SolidObject types
"""
from .solidobject import SolidObject
from .scadvariable import SCADVariable, Validators


class Cube(SolidObject):
    """
    Cube
    """
    def __init__(self, name, **kwargs):
        self._call_module = "cube"
        self.size = SCADVariable(required=True, validator=Validators.validate_list_numeric)

        super(Cube, self).__init__(name=name, **kwargs)


class Cylinder(SolidObject):
    """
    Cylinder
    """
    def __init__(self, name, **kwargs):
        self._call_module = "cylinder"
        self.radius = SCADVariable(validator=Validators.validate_numeric, template_as="r")
        self.diameter = SCADVariable(validator=Validators.validate_numeric, template_as="d")
        self.height = SCADVariable(validator=Validators.validate_numeric, template_as="h")

        super(Cylinder, self).__init__(name=name, **kwargs)
