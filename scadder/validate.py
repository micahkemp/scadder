from numbers import Number


class Validator:
    @classmethod
    def validate(cls, value):
        if not cls.is_valid(value):
            raise InvalidValue

        return value

    @staticmethod
    def is_valid(value):
        raise NotImplemented


class ValidateNumeric(Validator):
    @staticmethod
    def is_valid(value):
        if isinstance(value, Number):
            return True
        return False


class ValidateString(Validator):
    @staticmethod
    def is_valid(value):
        if isinstance(value, str):
            return True
        return False


class InvalidValue(Exception):
    pass
