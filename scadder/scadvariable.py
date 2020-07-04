class SCADVariable(object):
    def __init__(self, default=None, required=False):
        self._default = default
        self._is_required = required
        self._is_set = False

    @property
    def value(self):
        if self._is_required and not self._is_set:
            raise SCADMissingRequiredValue

        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self._is_set = True


class SCADMissingRequiredValue(Exception):
    pass
