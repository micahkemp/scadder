"""
Text
"""
from ..component import Component
from ..validate import ValidateString


class Text(Component):
    """
    Text
    """
    _module_name = "text"

    def __init__(self, name=None, text=""):
        super(Text, self).__init__(name=name)

        self.add_argument("text", ValidateString.validate(text))
