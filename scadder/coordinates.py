"""
Coordinate classes
"""
from math import atan2, degrees

from .validate import ValidateNumeric


class NamedCoordinates:
    """
    Maintain a variable set of numeric coordinates
    """
    def __init__(self):
        self._coordinates = {}
        self._order = []

    def add_coordinate(self, name, value):
        """
        Add a named coordinate
        :param name: The name of the added coordinate
        :param value: The value of the added coordinate
        """
        if name in self._coordinates:
            raise DuplicateCoordinateName

        self._coordinates[name] = value
        self._order.append(name)

    def list(self):
        """
        :return: The list of coordinate values, in the order defined
        """
        return [
            self._coordinates[name] for name in self._order
        ]

    def __getitem__(self, item):
        return self._coordinates[item]


class XY(NamedCoordinates):
    """
    Represent an X/Y point
    """
    def __init__(self, x_value, y_value):
        super(XY, self).__init__()

        self.add_coordinate("x", ValidateNumeric.validate(x_value))
        self.add_coordinate("y", ValidateNumeric.validate(y_value))

    @property
    def angle_xy_rad(self):
        """
        :return: The angle, in radians, between the X-axis and the point at X, Y
        """
        return atan2(self["y"], self["x"])

    @property
    def angle_xy_deg(self):
        """
        :return: The angle, in degrees, between the X-axis and the point at X, Y
        """
        return degrees(self.angle_xy_rad)


class XYZ(XY):
    """
    Represent X/Y/Z point
    """
    def __init__(self, x_value, y_value, z_value):
        super(XYZ, self).__init__(x_value, y_value)

        self.add_coordinate("z", ValidateNumeric.validate(z_value))

    @property
    def value(self):
        """
        :return: List of x_value, y_value, z_value
        """
        return [
            self["x"],
            self["y"],
            self["z"],
        ]


class DuplicateCoordinateName(Exception):
    """
    Raised when a coordinate is added to a Coordiantes class
    with an identical name of a previously added coordinate
    """
