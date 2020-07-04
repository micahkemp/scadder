from scadder.solidobject import SolidObject
from scadder.scadvariable import SCADVariable, SCADVariableMissingRequiredValue

import pytest


class BoringSolidObject(SolidObject):
    pass


def test_init_solid_object_base():
    # should not raise an exception
    my_boring_solid_object = BoringSolidObject()


class SolidObjectWithSimpleAttribute(SolidObject):
    simple_attribute = SCADVariable()


def test_init_with_simple_attribute_empty():
    # should not raise an exception with missing optional parameter
    my_simple_object = SolidObjectWithSimpleAttribute()


class SolidObjectWithRequiredAttribute(SolidObject):
    required_attribute = SCADVariable(required=True)


def test_init_with_missing_required():
    with pytest.raises(SCADVariableMissingRequiredValue):
        my_object_with_missing_required = SolidObjectWithRequiredAttribute()
