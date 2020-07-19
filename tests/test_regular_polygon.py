import pytest

from scadder import RegularPolygon


@pytest.fixture
def square():
    yield RegularPolygon(sides=4, radius=10)


def test_point_to_point_angle(square):
    assert square.point_to_point_angle_deg == 90

@pytest.mark.parametrize("point_number,result_x_y", [
    (0, [10, 0]),
    (1, [0, 10]),
    (2, [-10, 0]),
    (3, [0, -10]),
])
def test_points(square, point_number, result_x_y):
    point_x, point_y = result_x_y

    assert pytest.approx(square.point_x(point_number), 0.001) == point_x
    assert pytest.approx(square.point_y(point_number), 0.001) == point_y
