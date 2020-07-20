"""
Cube
"""
from ..component import Component, InvalidParameters
from ..validate import ValidateNumeric


class Cube(Component):
    """
    Cube
    """
    _module_name = "cube"

    def __init__(self, name=None, length=None, width=None, height=None):
        if not length or not width or not height:
            raise InvalidParameters("Must set length, width, and height")

        super(Cube, self).__init__(name=name)

        self.add_arguments({
            "size": [
                ValidateNumeric.validate(length),
                ValidateNumeric.validate(width),
                ValidateNumeric.validate(height),
            ]
        })
