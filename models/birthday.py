from datetime import datetime
from models.field import Field


class Birthday(Field):
    __FORMAT = "%d.%m.%Y"

    def __init__(self, date_str: str):
        self.__validate(date_str)
        super().__init__(date_str)

    @staticmethod
    def __validate(value: str):
        try:
            datetime.strptime(value, Birthday.__FORMAT)
        except ValueError:
            raise ValueError(f"Invalid birthday format: '{value}', expected DD.MM.YYYY")