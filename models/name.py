from .field import Field
import re

class Name(Field):
    __NAME_REGEXP = r"[A-Za-zА-Яа-яЇїІіЄєҐґ]+"

    def __init__(self, name: str):
        self.__validate(name)
        super().__init__(name)

    def __eq__(self, other):
        return isinstance(other, Name) and self.value == other.value
    
    @classmethod
    def __validate(cls, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        if not re.fullmatch(cls.__NAME_REGEXP, name):
            raise ValueError("Name must contain only letters.")
