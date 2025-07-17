from field import Field

class Tag(Field):
    def __init__(self, value):
        str_value = str(value)
        if not (1 <= len(str_value) <= 30):
            raise ValueError("Tag must be between 1 and 30 characters long.")
        super().__init__(str_value)

    def __str__(self):
        return f"[{self.value}]"