from field import Field

class Address(Field):
    __MIN_ADDRESS_LENGTH = 10
    __MAX_ADDRESS_LENGTH = 200
    __MIN_ADDRESS_PARTS = 3
    __STRING_SEPARATOR = ','

    @staticmethod
    def __isalpha(value: str) -> bool:
        return value.replace(" ", "").isalpha()

    @staticmethod
    def __address_validation(value: str):
        if not isinstance(value, str):
            raise ValueError("Address must be a string")

        if len(value) < Address.__MIN_ADDRESS_LENGTH or len(value) > Address.__MAX_ADDRESS_LENGTH:
            raise ValueError(f"Address length must be between {Address.__MIN_ADDRESS_LENGTH} and {Address.__MAX_ADDRESS_LENGTH} characters")

        parts = [p.strip() for p in value.split(Address.__STRING_SEPARATOR)]
        if len(parts) < Address.__MIN_ADDRESS_PARTS:
            raise ValueError("Address must include street name, number, and city, separated by commas")

        street, number, city = parts[0], parts[1], parts[2]

        if not Address._Address__isalpha(street):
            raise ValueError("Street name must contain only alphabetic characters and spaces")

        if not any(char.isdigit() for char in number):
            raise ValueError("Street number must contain at least one digit")

        if not Address._Address__isalpha(city):
            raise ValueError("City name must contain only alphabetic characters and spaces")

    def __init__(self, value: str):
        self.__address_validation(value)
        super().__init__(value)
