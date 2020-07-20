"""
Translate
"""
from ..component import ComponentWithChildren, InvalidParameters


class Translate(ComponentWithChildren):
    """
    Translate
    """
    _module_name = "translate"

    def __init__(self, name=None, children=None, vector=None):
        if not vector:
            raise InvalidParameters("Must set vector")

        super(Translate, self).__init__(name=name, children=children)

        self.add_arguments({
            "v": vector.list(),
        })
