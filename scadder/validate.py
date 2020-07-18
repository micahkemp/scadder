"""
Convenience argument validation
"""
from numbers import Number


class Validator:
    """
    Base class for validators
    """
    @classmethod
    def validate(cls, value):
        """
        Perform validation of passed value
        :param value: The value to be validated
        :return: If valid, returns the passed value.  If invalid, raises InvalidValue
        """
        if not cls.is_valid(value):
            raise InvalidValue

        return value

    @staticmethod
    def is_valid(value):
        """
        Override this function in subclasses.  Raises NotImplementedError otherwise.
        :param value: The value to be validated
        :return: True if valid, otherwise False
        """
        raise NotImplementedError


class ValidateNumeric(Validator):
    """
    Validator for numeric values
    """
    @staticmethod
    def is_valid(value):
        """
        :param value: The value to be validated
        :return: True if numeric, otherwise False
        """
        if isinstance(value, Number):
            return True
        return False


class ValidateString(Validator):
    """
    Validator for string values
    """
    @staticmethod
    def is_valid(value):
        """
        :param value: The value to be validated
        :return: True if a string, otherwise False
        """
        if isinstance(value, str):
            return True
        return False


class InvalidValue(Exception):
    """
    Raised when validation of a value failed
    """
