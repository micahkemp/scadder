"""
Basic definition of solid object class
"""
from inspect import getmembers

from .scadvariable import SCADVariable, SCADVariableMissingRequiredValue


class SolidObjectBase:
    """
    Represents a solid object
    """
    _module = "SolidBaseObject"

    def __init__(self, **kwargs):
        for arg_name, arg_value in kwargs.items():
            arg_object = getattr(self, arg_name)
            arg_object.value = arg_value

        for attr_name, attr_object in self.variables():
            try:
                # just need some way of calling attr_object.value to see if it raises an exception
                isinstance(attr_object.value, object)
            except SCADVariableMissingRequiredValue as raised_exception:
                print(f"{attr_name} is a required parameter")
                raise raised_exception

    def attributes_of_class(self, cls):
        """
        Returns members of this instance of the requested class.
        :param cls: The class of members to return.
        :return: The members matching the requested class.
        """
        return getmembers(
            self,
            lambda attribute: isinstance(attribute, cls),
        )

    def variables(self):
        """
        :return: The members of this instance of type SCADVariable
        """
        return self.attributes_of_class(SCADVariable)

    @property
    def module(self):
        """
        :return: ``self._module``
        """
        return self._module

    def module_arguments(self):
        """
        :return: A list containing the ``formatted_value`` of each argument.
        """
        return [
            f"{argument_name}={argument_object.formatted_value}"
            for argument_name, argument_object in self.variables()
        ]

    def formatted_module_arguments(self):
        """
        :return: A string containing ``module_arguments`` separated by commas and spaces
        """
        return ", ".join(self.module_arguments())

    def module_call(self):
        """
        :return: A string containing the module name and arguments in the calling form
        """
        return f"{self.module}({self.formatted_module_arguments()})"


class SolidObject(SolidObjectBase):
    """
    Represents a solid object derived from a module with no children
    """


class SolidObjectWithChildren(SolidObjectBase):
    """
    Represents a solid object derived from a transformation with children
    """
