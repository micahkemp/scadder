"""
Text
"""
from ..component import Component, InvalidParameters
from ..validate import ValidateString


class Text(Component):
    """
    Text
    """
    _module_name = "text"

    def __init__(self, name=None, text=None):
        if not text:
            raise InvalidParameters("Must set text")

        super(Text, self).__init__(name=name)

        self.add_argument("text", ValidateString.validate(text))
