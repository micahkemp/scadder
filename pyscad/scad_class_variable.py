class SCADClassVariable(object):
    def __init__(self, default=None):
        self._value = default

    def set_value(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
