"""
Cylinder
"""
from ..component import Component, InvalidParameters
from ..validate import ValidateNumeric


class Cylinder(Component):
    """
    Cylinder
    """
    _module_name = "cylinder"

    def __init__(self, name=None, radius=None, diameter=None, height=None):
        super(Cylinder, self).__init__(name=name)

        if radius and diameter:
            raise InvalidParameters("Can not specify both radius and diameter")

        if not radius and not diameter:
            raise InvalidParameters("Must specify either radius or diameter")

        if not height:
            raise InvalidParameters("Must set height")

        if diameter:
            radius = diameter/2

        self.add_arguments({
            "r": ValidateNumeric.validate(radius),
            "h": ValidateNumeric.validate(height),
        })
