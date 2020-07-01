from .scad_object_tracker import SCADObjectTracker

from jinja2 import Environment, BaseLoader, StrictUndefined
import os


class SCADClass(object):
    _render_template = """
// required modules
{% for required_module in required_modules %}
use <{{ required_module.value.filename }}>
{% endfor %}
// module definition
module {{ name }}() {
    {{ rendered_contents | indent() }}
}

// call module when run directly
{{ name }}();

"""

    def __init__(self, name, **kwargs):
        # before going any further register our name to check for conflicts
        SCADObjectTracker.instance().register_object(name, self)

        self._name = name

        for arg_name, arg_value in kwargs.items():
            arg_obj = getattr(self, arg_name)
            arg_obj.set_value(arg_value)

        try:
            for arg_name, arg_value in self._scad_class_variables.items():
                if arg_value.required and not arg_value.is_set:
                    raise SCADClassMissingRequiredArgument

        except AttributeError:
            raise UndecoratedSCADClass

    @property
    def filename(self):
        return ".".join([self._name, "scad"])

    def filename_at_path(self, path):
        return os.path.join(path, self.filename)

    @property
    def rendered_contents(self):
        module_render_template = Environment(loader=BaseLoader, undefined=StrictUndefined).from_string(self.contents)
        module_rendered_contents = module_render_template.render(self._scad_class_variables)

        render_template = Environment(loader=BaseLoader, undefined=StrictUndefined).from_string(self._render_template)
        rendered_contents = render_template.render({
            "name": self._name,
            "rendered_contents": module_rendered_contents,
            "required_modules": self._scad_class_variable_objects.values(),
        })

        return rendered_contents

    def render(self, path):
        try:
            with open(self.filename_at_path(path), "x") as render_file:
                render_file.write(self.rendered_contents)
        except FileExistsError:
            if not self.is_rendered(path=path):
                raise SCADObjectFileChanged

        for object_name, object in self._scad_class_variable_objects.items():
            object.value.render(path=path)

    def is_rendered(self, path):
        with open(self.filename_at_path(path), "r") as read_file:
            read_contents = read_file.read()

            return read_contents == self.rendered_contents


class UndecoratedSCADClass(Exception):
    pass


class SCADClassMissingRequiredArgument(Exception):
    pass


class SCADObjectFileChanged(Exception):
    pass
