"""
Components related to parameters passed to OpenSCAD modules
"""

from numbers import Number

from .validators import Validators


class Parameter:
    """
    Represents a parameter passed to an OpenSCAD module
    """
    def __init__(
            self,
            default=None,
            required=False,
            validator=Validators.validate_true,
            template_as=None
    ):
        """
        :param default: Default value for this parameter.  Defaults to None.
        :param required: Is this parameter required to be explicitly set?  Defaults to False.
        :param validator: The function to determine if a passed value is valid.
        :param template_as: The name of the parameter to use when templating.  Defaults to None.
        """
        # _value has no value until set by the setter
        self._value = None
        self._default = default
        self._is_required = required
        self._is_set = False
        self._validator = validator
        self._template_as = template_as

    @property
    def is_set(self):
        """"
        :return: True if the value has been explicitly false.  Otherwise False.
        """
        return self._is_set

    @property
    def template_as(self):
        """
        :return: The parameter name to use when templating, if it should override
        the instance variable name.
        """
        return self._template_as

    @property
    def value(self):
        """
        Get the value set.  If this parameter is required, and no default is configured, raises
        :class:`SCADMissingRequiredValue`.
        """
        if self._is_required and not self.is_set:
            raise ParameterMissingRequiredValue

        return self._value

    @value.setter
    def value(self, value):
        if not self.validate_value(value):
            raise ParameterInvalidValueSet

        self._value = value
        self._is_set = True

    def validate_value(self, value):
        """
        :param value: The value to be validated.
        :return: The result of the ``validator`` function.
        """
        return self._validator(value)

    @property
    def formatted_value(self):
        """
        :return: The ``value`` property formatted appropriately for passing in module arguments.
        """
        # no quotes necessary
        if isinstance(self.value, Number):
            return self.value

        if isinstance(self.value, str):
            # surround resulting string in double quotes
            return f'"{self.value}"'

        if isinstance(self.value, list):
            # explicitly ask for stringification here
            return f"{self.value}"

        raise ParameterUnknownValueType

    def init_copy(self):
        """
        Create a new instance of this Parameter, suitable to use as an instance variable to override
        the class variable.  Setting a value on a class variable instance will result in all
        instances of that class having that value going forward, which isn't what we want.
        :return: A new instance of Parameter with the same configuration as this one, as allowed
        by ``__init__``.
        """
        return Parameter(
            default=self._default,
            required=self._is_required,
            validator=self._validator,
            template_as=self._template_as,
        )


class ParameterMissingRequiredValue(Exception):
    """
    Raised when :class:`Parameter` instance is asked for its value when there is none,
    and the instance is defined as required.
    """


class ParameterInvalidValueSet(Exception):
    """
    Raised when :class:`Parameter` instance is asked to set an invalid value.
    """

class ParameterUnknownValueType(Exception):
    """
    Raised when :class:`Parameter` instance is asked for its formatted_value for an unknown
    typed value.
    """
