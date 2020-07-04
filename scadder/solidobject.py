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

    def __init__(self, name, **kwargs):
        self._object_module_name = name

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
    def call_module(self):
        """
        :return: ``self._module``
        """
        return self._module

    def call_module_arguments(self):
        """
        :return: A list containing the ``formatted_value`` of each argument.
        """
        set_arguments = []
        for argument_name, argument_object in self.variables():
            if argument_object.is_set:
                set_arguments.append([argument_name, argument_object])

        return [
            f"{argument_name}={argument_object.formatted_value}"
            for argument_name, argument_object in set_arguments
        ]

    def formatted_call_module_arguments(self):
        """
        :return: A string containing ``module_arguments`` separated by commas and spaces
        """
        return ", ".join(self.call_module_arguments())

    def formatted_call_module(self):
        """
        :return: A string containing the module name and arguments in the calling form
        """
        return f"{self.call_module}({self.formatted_call_module_arguments()})"



class SolidObject(SolidObjectBase):
    """
    Represents a solid object derived from a module with no children
    """


class SolidObjectWithChildren(SolidObjectBase):
    """
    Represents a solid object derived from a transformation with children
    """
    def __init__(self, name, children, **kwargs):
        for child in children:
            if not isinstance(child, SolidObjectBase):
                raise ChildNotSolidObject
        self._children = children

        super(SolidObjectWithChildren, self).__init__(name, **kwargs)


class ChildNotSolidObject(Exception):
    """
    Raised when a non-SolidObject is passed as a child to SolidObjectWithChildren
    """
