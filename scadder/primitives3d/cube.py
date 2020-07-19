"""
Cube
"""
from ..component import Component
from ..validate import ValidateNumeric


class Cube(Component):
    """
    Cube
    """
    _module_name = "cube"

    def __init__(self, name=None, length=0, width=0, height=0):
        super(Cube, self).__init__(name=name)

        self.add_arguments({
            "size": [
                ValidateNumeric.validate(length),
                ValidateNumeric.validate(width),
                ValidateNumeric.validate(height),
            ]
        })
