class SCADClass(object):
    def __init__(self, **kwargs):
        for arg_name, arg_value in kwargs.items():
            arg_obj = getattr(self, arg_name)
            arg_obj.set_value(arg_value)

        try:
            for arg_name, arg_value in self._scad_class_variables.items():
                if arg_value.required and arg_value.value is None:
                    raise SCADClassMissingRequiredArgument

        except AttributeError:
            raise UndecoratedSCADClass


class UndecoratedSCADClass(Exception):
    pass


class SCADClassMissingRequiredArgument(Exception):
    pass
