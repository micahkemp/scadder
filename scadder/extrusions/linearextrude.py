"""
LinearExtrude
"""
from ..component import ComponentWithChildren
from ..validate import ValidateNumeric


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
