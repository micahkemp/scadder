"""
Base Component classes
"""
import json
from jinja2 import Environment, PackageLoader


class ComponentBase:
    """
    Base class for Component sub-classes
    """
    _template_name = "ComponentBase.j2"

    def __init__(self, name=None):
        # name defaults to the {module_name}_component
        self.name = name if name else f"{self.module_name}_component"
        self._arguments = {}

    def add_argument(self, name, value):
        """
        Add an argument to be passed to the called module
        :param name: The name of the argument when calling the module
        :param value: The value to be used when calling the module
        """
        self._arguments[name] = value

    def add_arguments(self, arguments):
        """
        Add arguments to be passed to the called module
        :param arguments: A dictionary of arguments and their values to pass to the module
        """
        for name, value in arguments.items():
            self.add_argument(name, value)

    @property
    def arguments(self):
        """
        :return: Dictionary of keys/values that should be passed to the called module
        """
        return self._arguments

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

    @property
    def module_name(self):
        """
        The module name to call in the .scad file. Currently defined as the class name in lowercase.
        :return: The module name
        """
        return self.__class__.__name__.lower()

    @property
    def filename(self):
        """
        :return: The filename for this component
        """
        return f"{self.name}.scad"

    def rendered_contents(self):
        """
        :return: The rendered contents of the template.
        """
        env = Environment(
            loader=PackageLoader('scadder'),
        )

        template = env.get_template(self._template_name)
        return template.render({"component": self})


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

    def __init__(self, name, children):
        super(ComponentWithChildren, self).__init__(name=name)

        self.children = []
        self.add_children(children)

    def add_child(self, child):
        """
        Add a single child to this component
        :param child: The child to add
        """
        if not isinstance(child, ComponentBase):
            raise InvalidChild
        self.children.append(child)

    def add_children(self, children):
        """
        Add children to this component
        :param children: A list of children to add
        """
        for child in children:
            self.add_child(child)


class InvalidChild(Exception):
    """
    Indicates a non-child was attempted to be added to a component's children
    """
