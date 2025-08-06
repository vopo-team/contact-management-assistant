import re

from models.field import Field


class Email(Field):
    PATTERN = r"^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    def __init__(self, email: str):
        self._validate(email)
        super().__init__(email)

    def __eq__(self, other):
        return isinstance(other, Email) and self.value == other.value

    @classmethod
    def _validate(cls, value: str):
        if not re.match(cls.PATTERN, value):
            raise ValueError(f"Invalid email: {value}")
