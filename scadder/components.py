"""
Predefined Component classes ready to be used
"""
from .component import Component
from .validate import ValidateNumeric, ValidateString


class Cube(Component):
    """
    Cube
    """
    def __init__(self, name=None, length=0, width=0, height=0):
        super(Cube, self).__init__(name=name)

        self.add_arguments({
            "size": [
                ValidateNumeric.validate(length),
                ValidateNumeric.validate(width),
                ValidateNumeric.validate(height),
            ]
        })


class Text(Component):
    """
    Text
    """
    def __init__(self, name=None, text=""):
        super(Text, self).__init__(name=name)

        self.add_argument("text", ValidateString.validate(text))
