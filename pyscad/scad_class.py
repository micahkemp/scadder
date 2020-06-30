from .scad_object_tracker import SCADObjectTracker

import jinja2
import os


class SCADClass(object):
    def __init__(self, name, **kwargs):
        # before going any further register our name to check for conflicts
        SCADObjectTracker.instance().register_object(name, self)

        self._name = name

        for arg_name, arg_value in kwargs.items():
            arg_obj = getattr(self, arg_name)
            arg_obj.set_value(arg_value)

        try:
            for arg_name, arg_value in self._scad_class_variables.items():
                if arg_value.required and arg_value.value is None:
                    raise SCADClassMissingRequiredArgument

        except AttributeError:
            raise UndecoratedSCADClass

    @property
    def filename(self):
        return ".".join([self._name, "scad"])

    def filename_at_path(self, path):
        return os.path.join(path, self.filename)

    def render(self, path):
        render_contents = self.render_template

        try:
            with open(self.filename_at_path(path), "x") as render_file:
                render_file.write(render_contents)
        except FileExistsError:
            with open(self.filename_at_path(path), "r") as read_file:
                read_contents = read_file.read()

                if not read_contents == render_contents:
                    raise SCADObjectFileChanged


class UndecoratedSCADClass(Exception):
    pass


class SCADClassMissingRequiredArgument(Exception):
    pass


class SCADObjectFileChanged(Exception):
    pass
