from .scad_class import SCADClass


class SCADClassVariable(object):
    def __init__(self, default=None, required=False):
        self._value = default
        self._required = required

    def set_value(self, value):
        if not self.validate(value):
            raise SCADClassVariableInvalidValue

        self._value = value

    @property
    def is_set(self):
        return self._value is not None

    @property
    def value(self):
        if not self.is_set:
            raise SCADClassVariableUnset
        return self._value

    @property
    def required(self):
        return self._required

    def validate(self, value):
        return True


class SCADClassVariableObject(SCADClassVariable):
    def validate(self, value):
        return isinstance(value, SCADClass)


class SCADClassVariableUnset(Exception):
    pass

class SCADClassVariableInvalidValue(Exception):
    pass
