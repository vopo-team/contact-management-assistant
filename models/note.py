from field import Field

class Note(Field):
    __MIN_NOTE_LENGTH = 1
    __MAX_NOTE_LENGTH = 200

    def __init__(self, text: str):
        self.__validate(text)
        super().__init__(text)

    @classmethod
    def __validate(cls, value: str):
        if len(value) >= cls.__MAX_NOTE_LENGTH:
            raise ValueError(f"Note cannot exceed {cls.__MAX_NOTE_LENGTH} characters")
        if len(value) <= cls.__MIN_NOTE_LENGTH:
            raise ValueError(f"Note cannot be less than {cls.__MIN_NOTE_LENGTH} character")
