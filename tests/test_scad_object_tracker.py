from scadder.scad_object_tracker import SCADObjectTracker, SCADObjectTrackerSingleton, SCADObjectTrackerDuplicateName

import pytest


def test_initial_creation():
    # this may throw an exception any time this is run with any other tests, due to ordering
    # so skip it and only test SCADObjectTracker.instance()
    #SCADObjectTracker()
    SCADObjectTracker.instance()


def test_additional_creation():
    with pytest.raises(SCADObjectTrackerSingleton):
        SCADObjectTracker()


def test_first_object_with_name():
    # "first_object" is just a simple string object
    SCADObjectTracker.instance().register_object("first_object_name", "first_object")


def test_conflicting_object_name():
    with pytest.raises(SCADObjectTrackerDuplicateName):
        SCADObjectTracker.instance().register_object("first_object_name", "first_object")
