"""
Model class things go here
"""


class Model:
    """
    Basic Model class
    """
    def __init__(self, name):
        self._name = name

    def component(self):
        """
        Overload this method if your Model class has a "main" object.  Unless overloaded,
        raises NotImplementedError.
        :return: The "main" component for this Model.
        """
        raise NotImplementedError

    def render(self, output_path):
        """
        Renders this Model, by way of calling ``render`` on the component returned by
        ``component()``.
        :param output_path: The output path to render this Model and its related components into.
        :return: None
        """
        self.component().render(output_path=output_path)
