from datetime import datetime
from .field import Field
import os
class Birthday(Field):

    def __init__(self, date_str: str):
        self.__validate(date_str)
        super().__init__(date_str)

    def __eq__(self, other):
        return isinstance(other, Birthday) and self.value == other.value

    @classmethod
    def __validate(cls, value: str):
        try:
            datetime_pattern = os.getenv("DATETIME_OBJECT_PATTERN")
            datetime.strptime(value, datetime_pattern)
        except ValueError:
            raise ValueError(f"Invalid birthday format: '{value}', expected DD.MM.YYYY")
