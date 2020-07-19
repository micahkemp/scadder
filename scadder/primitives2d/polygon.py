"""
Polygon
"""
from ..component import Component
from ..coordinates import XY


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
