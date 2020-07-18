"""
Predefined Component classes ready to be used
"""
from .component import Component
from .validate import ValidateNumeric, ValidateString


class Cube(Component):
    """
    Cube
    """
    def __init__(self, name, length, width, height):
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
    def __init__(self, name, text):
        super(Text, self).__init__(name=name)

        self.add_argument("text", ValidateString.validate(text))
