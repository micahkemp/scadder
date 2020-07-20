"""
Regular Polygons
"""
from math import sin, cos, radians

from ..primitives2d import Polygon
from ..coordinates import XY
from ..component import InvalidParameters


class RegularPolygon(Polygon):
    """Regular Polygon"""
    def __init__(self, name=None, radius=None, sides=None):
        if not radius:
            raise InvalidParameters("Must set radius")

        if not sides or sides < 3:
            raise InvalidParameters("Must set sides >= 3")

        self.radius = radius
        self.sides = sides

        super(RegularPolygon, self).__init__(name=name, points=self.points_list())

    @property
    def point_to_point_angle_deg(self):
        """
        :return: The angle, in degrees, between points
        """
        return 360/self.sides

    @property
    def point_to_point_angle_rad(self):
        """
        :return: The angle, in radians, between points
        """
        return radians(self.point_to_point_angle_deg)

    def point_angle_rad(self, point):
        """
        :param point: The point number, zero-indexed
        :return: The angle, in radians, between points
        """
        return point*self.point_to_point_angle_rad

    def point_x(self, point):
        """
        :param point: The point number, zero-indexed
        :return: The x value for the point
        """
        return cos(self.point_angle_rad(point)) * self.radius

    def point_y(self, point):
        """
        :param point: The point number, zero-indexed
        :return: The y value for the point
        """
        return sin(self.point_angle_rad(point)) * self.radius

    def points_list(self):
        """
        :return: A list of point coordinates that define this polygon
        """
        return [
            XY(
                self.point_x(point_number),
                self.point_y(point_number),
            ).list() for point_number in range(0, self.sides)
        ]


class Triangle(RegularPolygon):
    """
    Triangle
    """
    def __init__(self, name=None, radius=None):
        super(Triangle, self).__init__(name=name, radius=radius, sides=3)


class Hexagon(RegularPolygon):
    """
    Hexagon
    """
    def __init__(self, name=None, radius=None):
        super(Hexagon, self).__init__(name=name, radius=radius, sides=6)

class Octagon(RegularPolygon):
    """
    Octagon
    """
    def __init__(self, name=None, radius=None):
        super(Octagon, self).__init__(name=name, radius=radius, sides=8)
