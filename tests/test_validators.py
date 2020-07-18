from scadder.validate import *

import pytest


def test_valid_numeric():
    assert ValidateNumeric.validate(123) == 123
    assert ValidateNumeric.validate(123) == 123.0


def test_invalid_numeric():
    with pytest.raises(InvalidValue):
        ValidateNumeric.validate("123")


def test_valid_string():
    assert ValidateString.validate("just a string") == "just a string"
    assert ValidateString.validate("123") == "123"


def test_invalid_string():
    with pytest.raises(InvalidValue):
        ValidateString.validate(123)
