"""
Components related to variable validation
"""

from numbers import Number


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
        return isinstance(value, Number)

    @staticmethod
    def validate_list_numeric(value):
        """
        Validates the passed value is a list of numeric values
        :param value: The value (list) being validated
        :return: True if :param value: is a list of numeric values
        """
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, Number):
                    # this item is not Numeric, return False
                    return False

            # all items were numeric, return False
            return True

        # not a list, return False
        return False
