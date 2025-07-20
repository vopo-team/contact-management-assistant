from datetime import datetime
from field import Field
from utils import DATETIME_OBJECT_PATTERN
class Birthday(Field):

    def __init__(self, date_str: str):
        self.__validate(date_str)
        super().__init__(date_str)

    def __eq__(self, other):
        return isinstance(other, Birthday) and self.value == other.value

    @classmethod
    def __validate(cls, value: str):
        try:
            datetime.strptime(value, DATETIME_OBJECT_PATTERN)
        except ValueError:
            raise ValueError(f"Invalid birthday format: '{value}', expected DD.MM.YYYY")
