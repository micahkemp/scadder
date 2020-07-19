"""
Predefined Component classes with children ready to be used
"""
from .component import ComponentWithChildren
from .coordinates import XYZ


class Translate(ComponentWithChildren):
    """
    Translate
    """
    def __init__(self, name=None, children=None, vector=None):
        # default children to empty list
        children = children if children else []
        vector = vector if vector else XYZ(0, 0, 0)

        super(Translate, self).__init__(name=name, children=children)

        self.add_arguments({
            "v": vector.list(),
        })
