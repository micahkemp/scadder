"""
Components related to variable validation
"""


class Validators:
    """
    Collection of validator functions for common uses.
    """
    @staticmethod
    def validate_true(value):
        """
        Always returns True
        :param value: The value being validated
        :return: True
        """
        return value or True

    @staticmethod
    def validate_numeric(value):
        """
        Validates the passed value is numeric
        :param value: The value being validated
        :return: True if :param value: is numeric
        """
        return isinstance(value, int)
