"""
Component things live here
"""
from inspect import getmembers
import os

from jinja2 import Environment, PackageLoader

from .parameter import Parameter, ParameterMissingRequiredValue


class Component:
    """
    Represents a component
    """
    _call_module = "Component"

    def __init__(self, name, **kwargs):
        self._module_name = name
        self._template_name = "Component.scad"

        for arg_name, arg_value in kwargs.items():
            arg_object = getattr(self, arg_name)
            # get a new instance of Parameter suitable to set the value on
            # required due to how we use class variables for the parameter configuration
            instance_parameter = arg_object.init_copy()
            # set the value on the instance_parameter object to avoid its value bleeding over
            # to other instances of this Component
            instance_parameter.value = arg_value
            # and override our instance's named variable to point to the instance object
            setattr(self, arg_name, instance_parameter)

        for attr_name, attr_object in self.parameters():
            try:
                # just need some way of calling attr_object.value to see if it raises an exception
                isinstance(attr_object.value, object)
            except ParameterMissingRequiredValue as raised_exception:
                print(f"{attr_name} is a required parameter")
                raise raised_exception

    @property
    def module_name(self):
        """
        :return: self._module_name, which is set via ``name`` in ``__init__``
        """
        return self._module_name

    @property
    def template_name(self):
        """
        :return: The template name used by this class.
        """
        return self._template_name

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

    def parameters(self):
        """
        :return: The members of this instance of type Parameter
        """
        return self.attributes_of_class(Parameter)

    @property
    def call_module(self):
        """
        :return: ``self._call_module``
        """
        return self._call_module

    def call_module_arguments(self):
        """
        :return: A list containing the ``formatted_value`` of each argument.
        """
        set_arguments = []
        for argument_name, argument_object in self.parameters():
            if argument_object.is_set:
                set_arguments.append([argument_name, argument_object])

        return [
            # use argument_object.template_as if it exists, otherwise use the variable's name
            f"{argument_object.template_as or argument_name}={argument_object.formatted_value}"
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

    def filename(self):
        """
        :return: The filename to be used based on the module name with ".scad" appended.
        """
        return ".".join([self.module_name, "scad"])

    def filename_at_path(self, path):
        """
        :param path: The directory the file will reside in.
        :return: The full path/filename to this module's file, based on the passed path.
        """
        return os.path.join(path, self.filename())

    def render_contents(self):
        """
        :param template_name: The template to render.  This should be passed when subclasses
        call super()
        :return: The rendered contents of the template.
        """
        env = Environment(
            loader=PackageLoader('scadder'),
        )

        template = env.get_template(self.template_name)
        return template.render({"component": self})

    def is_rendered(self, path):
        """
        :param path: The path the template was or will be rendered to.
        :return: True if the rendered file is present and as expected at the path
        provided.  Otherwise False.
        """
        try:
            with open(self.filename_at_path(path), "r") as read_file:
                read_contents = read_file.read()

            return read_contents == self.render_contents()
        # if the file doesn't exist it hasn't been rendered
        except FileNotFoundError:
            return False

    def render(self, output_path):
        """
        Render the result of ``render_contents`` to the filename appropriate for this module
        in the path specified in this call.
        :param output_path: The path to render files into.
        """
        try:
            with open(self.filename_at_path(output_path), "x") as render_file:
                render_file.write(self.render_contents())
        except FileExistsError:
            if not self.is_rendered(path=output_path):
                raise TemplatedFileChanged


class ComponentWithChildren(Component):
    """
    Represents a Component derived from a transformation with children
    """
    def __init__(self, name, children, **kwargs):
        super(ComponentWithChildren, self).__init__(name, **kwargs)

        self._template_name = "ComponentWithChildren.scad"

        for child in children:
            if not isinstance(child, Component):
                raise ChildNotComponent
        self._children = children

    @property
    def children(self):
        """
        :return: The list of children passed in during creation.
        """
        return self._children

    def render(self, output_path):
        super(ComponentWithChildren, self).render(output_path=output_path)

        for child in self.children:
            child_output_path = os.path.join(output_path, child.module_name)
            try:
                os.mkdir(child_output_path)
            except FileExistsError:
                # already exists is good enough
                pass

            child.render(output_path=child_output_path)


class ChildNotComponent(Exception):
    """
    Raised when a non-Compnonent is passed as a child to ComponentWithChildren
    """

class TemplatedFileChanged(Exception):
    """
    Raised when a templated file is attempted to be templated again, with differing
    contents.
    """
