"""
Basic definition of solid object class
"""
from inspect import getmembers
import os

from jinja2 import Environment, PackageLoader

from .scadvariable import SCADVariable, SCADVariableMissingRequiredValue


class SolidObjectBase:
    """
    Represents a solid object
    """
    _call_module = "SolidObjectBase"

    def __init__(self, name, **kwargs):
        self._module_name = name
        self._template_name = "SolidObjectBase.scad"

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

    def variables(self):
        """
        :return: The members of this instance of type SCADVariable
        """
        return self.attributes_of_class(SCADVariable)

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
        return template.render({"solid_object": self})

    def is_rendered(self, path):
        """
        :param path: The path the template was or will be rendered to.
        :return: True if the rendered file is present and as expected at the path
        provided.  Otherwise False.
        """
        with open(self.filename_at_path(path), "r") as read_file:
            read_contents = read_file.read()

            return read_contents == self.render_contents()

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

class SolidObject(SolidObjectBase):
    """
    Represents a solid object derived from a module with no children
    """
    def __init__(self, name, **kwargs):
        super(SolidObject, self).__init__(name=name, **kwargs)

        self._template_name = "SolidObject.scad"


class SolidObjectWithChildren(SolidObjectBase):
    """
    Represents a solid object derived from a transformation with children
    """
    def __init__(self, name, children, **kwargs):
        super(SolidObjectWithChildren, self).__init__(name, **kwargs)

        self._template_name = "SolidObjectWithChildren.scad"

        for child in children:
            if not isinstance(child, SolidObjectBase):
                raise ChildNotSolidObject
        self._children = children

    @property
    def children(self):
        """
        :return: The list of children passed in during creation.
        """
        return self._children


class ChildNotSolidObject(Exception):
    """
    Raised when a non-SolidObject is passed as a child to SolidObjectWithChildren
    """

class TemplatedFileChanged(Exception):
    """
    Raised when a templated file is attempted to be templated again, with differing
    contents.
    """
