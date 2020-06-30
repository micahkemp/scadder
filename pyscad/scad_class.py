class SCADClass(object):
    def __init__(self, **kwargs):
        try:
            getattr(self, "_scad_class_variables")
        except:
            raise Exception("Undecorated SCADClass!")

        for arg_name, arg_value in kwargs.items():
            arg_obj = getattr(self, arg_name)
            arg_obj.set_value(arg_value)
