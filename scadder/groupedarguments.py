"""
Group arguments that always live together
"""
from math import atan2, degrees

from .validate import ValidateNumeric


class XY:
    """
    Represent an X/Y point
    """
    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value

    @property
    def value(self):
        """
        :return: List of x_value, y_value
        """
        return [
            self.x_value,
            self.y_value,
        ]

    @property
    def angle_xy_rad(self):
        """
        :return: The angle, in radians, between the X-axis and the point at X, Y
        """
        return atan2(self.y_value, self.x_value)

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

        self.z_value = ValidateNumeric.validate(z_value)

    @property
    def value(self):
        """
        :return: List of x_value, y_value, z_value
        """
        return [
            self.x_value,
            self.y_value,
            self.z_value,
        ]
