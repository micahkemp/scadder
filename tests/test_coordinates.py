from scadder import XY, XYZ


def test_xy_list():
    assert XY(1, 2).list() == [1, 2]


def test_xyz_list():
    assert XYZ(1, 2, 3).list() == [1, 2, 3]


def test_xy_angle_degrees():
    # simple tests to ensure we ordered the X/Y correctly for the atan2 function
    assert XY(1, 1).angle_xy_deg == 45
    assert XY(1, -1).angle_xy_deg == -45
