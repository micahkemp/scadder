class Model:
    def __init__(self, name):
        self._name = name

    # overload component if the class has a "main" component
    def component(self):
        raise NotImplementedError

    def render(self, output_path):
        self.component().render(output_path=output_path)
