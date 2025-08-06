import re

from models.field import Field


class Name(Field):
    NAME_REGEXP = r"[A-Za-zА-Яа-яЇїІіЄєҐґ]+"

    def __init__(self, name: str):
        self._validate(name)
        super().__init__(name)

    def __eq__(self, other):
        return isinstance(other, Name) and self.value == other.value

    @classmethod
    def _validate(cls, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        if not re.fullmatch(cls.NAME_REGEXP, name):
            raise ValueError("Name must contain only letters.")
