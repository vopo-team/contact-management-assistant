from field import Field

class Tag(Field):
    __MIN_TAG_LENGTH = 1
    __MAX_TAG_LENGTH = 30
    
    def __init__(self, value):
        str_value = str(value)
        self.__validate(str_value)
        super().__init__(str_value)
        
    def __eq__(self, other):
        return isinstance(other, Tag) and self.value == other.value

    def __str__(self):
        return f"[{self.value}]"

    @classmethod
    def __validate(cls, value: str):
        if not (cls.__MIN_TAG_LENGTH <= len(value) <= cls.__MAX_TAG_LENGTH):
            raise ValueError(f"Tag must be between {cls.__MIN_TAG_LENGTH} and {cls.__MAX_TAG_LENGTH} characters long.")
