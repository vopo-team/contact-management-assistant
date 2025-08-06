from models.field import Field


class Tag(Field):
    MIN_TAG_LENGTH = 1
    MAX_TAG_LENGTH = 30

    def __init__(self, value):
        str_value = str(value)
        self._validate(str_value)
        super().__init__(str_value)

    def __eq__(self, other):
        return isinstance(other, Tag) and self.value == other.value

    def __str__(self):
        return f"[{self.value}]"

    @classmethod
    def _validate(cls, value: str):
        if not (cls.MIN_TAG_LENGTH <= len(value) <= cls.MAX_TAG_LENGTH):
            raise ValueError(
                f"Tag must be between {cls.MIN_TAG_LENGTH} "
                f"and {cls.MAX_TAG_LENGTH} characters long."
            )
