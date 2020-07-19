"""
Translate
"""
from ..component import ComponentWithChildren
from ..coordinates import XYZ


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
