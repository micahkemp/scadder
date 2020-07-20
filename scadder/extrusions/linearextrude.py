"""
LinearExtrude
"""
from ..component import ComponentWithChildren, InvalidParameters
from ..validate import ValidateNumeric


class LinearExtrude(ComponentWithChildren):
    """
    Linear Extrude
    """
    _module_name = "linear_extrude"

    def __init__(self, name=None, children=None, height=None):
        if not height:
            raise InvalidParameters("Must set height")

        super(LinearExtrude, self).__init__(name=name, children=children)

        self.add_arguments({
            "height": ValidateNumeric.validate(height),
        })
