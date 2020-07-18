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

        self.length = ValidateNumeric.validate(length)
        self.width = ValidateNumeric.validate(width)
        self.height = ValidateNumeric.validate(height)

    @property
    def arguments(self):
        """
        :return: Dictionary of arguments to pass to the cube() module
        """
        return {
            "size": [
                self.length,
                self.width,
                self.height,
            ]
        }


class Text(Component):
    """
    Text
    """
    def __init__(self, name, text):
        super(Text, self).__init__(name=name)

        self.text = ValidateString.validate(text)

    @property
    def arguments(self):
        """
        :return: Dictionary of argumnets to pass to the text() module
        """
        return {
            "text": self.text,
        }
