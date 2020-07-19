"""
Predefined Component classes with children ready to be used
"""
from .component import ComponentWithChildren
from .coordinates import XYZ
from .validate import ValidateNumeric


class Translate(ComponentWithChildren):
    """
    Translate
    """
    _module_name = "translate"

    def __init__(self, name=None, children=None, vector=None):
        super(Translate, self).__init__(name=name, children=children)

        vector = vector if vector else XYZ(0, 0, 0)

        self.add_arguments({
            "v": vector.list(),
        })


class LinearExtrude(ComponentWithChildren):
    """
    Linear Extrude
    """
    _module_name = "linear_extrude"

    def __init__(self, name=None, children=None, height=1):
        super(LinearExtrude, self).__init__(name=name, children=children)

        self.add_arguments({
            "height": ValidateNumeric.validate(height),
        })
