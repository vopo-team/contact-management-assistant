from field import Field
import re

class Name(Field):
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        if not re.fullmatch(r"[A-Za-zА-Яа-яЇїІіЄєҐґ]+", name):
            raise ValueError("Name must contain only letters.")
        super().__init__(name)
