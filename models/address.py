from field import Field
from rapidfuzz import fuzz
from utils import FUZZ_SIMILARITY_THRESHOLD

class Address(Field):
    __MIN_ADDRESS_LENGTH = 10
    __MAX_ADDRESS_LENGTH = 200
    __MIN_ADDRESS_PARTS = 3
    __STRING_SEPARATOR = ','
    

    @classmethod
    def __isalpha(cls,value: str) -> bool:
        return value.replace(" ", "").isalpha()

    @classmethod
    def __address_validation(cls, value: str):
        if not isinstance(value, str):
            raise ValueError("Address must be a string")

        if len(value) < cls.__MIN_ADDRESS_LENGTH or len(value) > cls.__MAX_ADDRESS_LENGTH:
            raise ValueError(f"Address length must be between {cls.__MIN_ADDRESS_LENGTH} and {cls.__MAX_ADDRESS_LENGTH} characters")

        parts = [p.strip() for p in value.split(cls.__STRING_SEPARATOR)]
        if len(parts) < cls.__MIN_ADDRESS_PARTS:
            raise ValueError("Address must include street name, number, and city, separated by commas")

        street, number, city = parts[0], parts[1], parts[2]

        if not cls.__isalpha(street):
            raise ValueError("Street name must contain only alphabetic characters and spaces")

        if not any(char.isdigit() for char in number):
            raise ValueError("Street number must contain at least one digit")

        if not cls.__isalpha(city):
            raise ValueError("City name must contain only alphabetic characters and spaces")

    def has_pattern(self, pattern: str) -> bool:
        return fuzz.partial_ratio(pattern.lower(), self.value.lower()) > FUZZ_SIMILARITY_THRESHOLD
    
    def __init__(self, value: str):
        self.__address_validation(value)
        super().__init__(value)
