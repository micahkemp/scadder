class SCADClass(object):
    def __init__(self, **kwargs):
        for arg_name, arg_value in kwargs.items():
            arg_obj = getattr(self, arg_name)
            arg_obj.set_value(arg_value)

        try:
            for arg_name, arg_value in self._scad_class_variables.items():
                pass
        except AttributeError:
            raise UndecoratedSCADClass("Undecorated SCAD Class!")


class UndecoratedSCADClass(Exception):
    pass
