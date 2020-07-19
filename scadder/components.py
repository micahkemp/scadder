"""
Predefined Component classes ready to be used
"""
from .component import Component
from .validate import ValidateNumeric, ValidateString
from .coordinates import XY


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


class Text(Component):
    """
    Text
    """
    _module_name = "text"

    def __init__(self, name=None, text=""):
        super(Text, self).__init__(name=name)

        self.add_argument("text", ValidateString.validate(text))


class Polygon(Component):
    """
    Polygon
    """
    _module_name = "polygon"

    def __init__(self, name=None, points=None):
        super(Polygon, self).__init__(name=name)

        self.points = points if points is not None else []

        self.add_argument(
            "points",
            [XY(*coordinates).list() for coordinates in points]
        )
