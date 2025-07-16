from datetime import datetime
from field import Field

class Birthday(Field):
    __FORMAT = "%d.%m.%Y"

    def __init__(self, date_str: str):
        self.__validate(date_str)
        super().__init__(date_str)

    @classmethod
    def __validate(cls, value: str):
        try:
            datetime.strptime(value, cls.__FORMAT)
        except ValueError:
            raise ValueError(f"Invalid birthday format: '{value}', expected DD.MM.YYYY")
