from .scad_class_variable import SCADClassVariable

from inspect import getmembers

class SCADConfiguration(object):
    def __init__(self, o=None, **kwargs):
        self._settings = kwargs

    def __call__(self, o):
        o.name = o.__name__
        o._settings = self._settings

        is_scad_class_variable = lambda attribute: isinstance(attribute, SCADClassVariable)
        scad_class_variables = getmembers(o, is_scad_class_variable)

        o._scad_class_variables = {}
        for attr_name, scad_class_variable in scad_class_variables:
            o._scad_class_variables[attr_name] =scad_class_variable

        return o
