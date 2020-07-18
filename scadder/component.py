"""
Base Component classes
"""
import json


class ComponentBase:
    """
    Base class for Component sub-classes
    """
    def __init__(self, name):
        self.name = name

    @property
    def arguments(self):
        """
        :return: Dictionary of keys/values that should be passed to the called module
        """
        return {}

    def argument_formatted(self, argument_name):
        """
        :param argument_name: The name of the argument to return the value of
        :return: The formatted value, suitable for use in a .scad file
        """
        # the JSON-formatted representation should be suitable to use in a .scad for strings
        if isinstance(self.arguments[argument_name], str):
            return json.dumps(self.arguments[argument_name])

        return self.arguments[argument_name]

    @property
    def arguments_formatted(self):
        """
        :return: Dictionary of keys and their values as returned by ``argument_formatted``
        """
        return {
            arg_name: self.argument_formatted(arg_name) for arg_name in self.arguments
        }

    @property
    def argument_strings(self):
        """
        :return: List of key=value strings, with values formatted as returned by
        ``argument_formatted``
        """
        return [
            f"{arg_name}={self.arguments_formatted[arg_name]}" for arg_name in self.arguments
        ]

    @property
    def arguments_string(self):
        """
        :return: A string containing all key=value pairs, comma-separated, ready to be used
        in a .scad module call
        """
        return ", ".join(self.argument_strings)


class Component(ComponentBase):
    """
    Component without children
    """
    _template_name = "Component.j2"


class ComponentWithChildren(Component):
    """
    Component with children
    """
    _template_name = "ComponentWithChildren.j2"
