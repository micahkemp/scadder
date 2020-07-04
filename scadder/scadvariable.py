"""
Components related to variables passed to OpenSCAD modules
"""

from .validators import Validators


class SCADVariable:
    """
    Represents a variable passed to an OpenSCAD module
    """
    def __init__(self, default=None, required=False, validator=Validators.validate_true):
        """
        :param default: Default value for this variable.  Defaults to None.
        :param required: Is this variable required to be explicitly set?  Defaults to False.
        :param validator: The function to determine if a passed value is valid.
        """
        self._default = default
        self._is_required = required
        self._is_set = False
        self._validator = validator

    @property
    def value(self):
        """
        Get the value set.  If this variable is required, and no default is configured, raises
        :class:`SCADMissingRequiredValue`.
        """
        if self._is_required and not self._is_set:
            raise SCADMissingRequiredValue

        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self._is_set = True

    def validate_value(self, value):
        """
        :param value: The value to be validated.
        :return: The result of the ``validator`` function.
        """
        return self._validator(value)


class SCADMissingRequiredValue(Exception):
    """
    Raised when :class:`SCADVariable` instance is asked for its value when there is none,
    and the instance is defined as required.
    """
