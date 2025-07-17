from field import Field

class Tag(Field):
    def __init__(self, value):
        str_value = str(value)
        self.__validate(str_value)
        super().__init__(str_value)

    @classmethod
    def __validate(cls, value: str):
        if not (1 <= len(value) <= 30):
            raise ValueError("Tag must be between 1 and 30 characters long.")

    def __str__(self):
        return f"[{self.value}]"
