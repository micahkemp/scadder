from scadder.coordinates import XYZ


def test_xyz_angle_degrees():
    # simple tests to ensure we ordered the X/Y correctly for the atan2 function
    assert XYZ(1, 1, 0).angle_xy_deg == 45
    assert XYZ(1, -1, 0).angle_xy_deg == -45
