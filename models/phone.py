import re
from models.field import Field


class Phone(Field):
    __PHONE_REG_EXP = r"\+380\d{9}"

    def __init__(self, value):
        self.__validate(value)
        super().__init__(value)

    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value

    @classmethod
    def __validate(cls, value: str) -> None:
        if not re.fullmatch(cls.__PHONE_REG_EXP, value):
            raise ValueError(
                "Phone number must be in the format +380XXXXXXXXX.")
