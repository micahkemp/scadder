class SCADObjectTracker(object):
    __instance = None

    def __init__(self):
        if SCADObjectTracker.__instance is not None:
            raise SCADObjectTrackerSingleton

        self._tracked_objects = {}

        SCADObjectTracker.__instance = self

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            SCADObjectTracker()

        return cls.__instance

    def register_object(self, name, object):
        if name in self._tracked_objects:
            raise SCADObjectTrackerDuplicateName
        self._tracked_objects[name] = object


class SCADObjectTrackerSingleton(Exception):
    pass


class SCADObjectTrackerDuplicateName(Exception):
    pass
