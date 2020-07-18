"""
Predefined Component classes with children ready to be used
"""
from .component import ComponentWithChildren
from .validate import ValidateNumeric


class Translate(ComponentWithChildren):
    """
    Translate
    """
    def __init__(self, name=None, children=[], vector_x=0, vector_y=0, vector_z=0):
        super(Translate, self).__init__(name=name, children=children)

        self.add_arguments({
            "v": [
                ValidateNumeric.validate(vector_x),
                ValidateNumeric.validate(vector_y),
                ValidateNumeric.validate(vector_z),
            ]
        })
