class SCADClassVariable(object):
    def __init__(self, default=None, required=False):
        self._value = default
        self._required = required

    def set_value(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @property
    def required(self):
        return self._required
