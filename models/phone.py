from field import Field
import re

class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r"\+380\d{9}", value):
            raise ValueError("Phone number must be in the format +380XXXXXXXXX.")
        super().__init__(value)

    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value
