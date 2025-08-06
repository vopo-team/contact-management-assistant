import os

from rapidfuzz import fuzz

from models.field import Field


class Address(Field):
    MIN_ADDRESS_LENGTH = 10
    MAX_ADDRESS_LENGTH = 200
    MIN_ADDRESS_PARTS = 3
    STRING_SEPARATOR = ","

    @classmethod
    def _isalpha(cls, value: str) -> bool:
        return value.replace(" ", "").isalpha()

    @classmethod
    def _address_validation(cls, value: str):
        if not isinstance(value, str):
            raise ValueError("Address must be a string")

        if (
            len(value) < cls.MIN_ADDRESS_LENGTH
            or len(value) > cls.MAX_ADDRESS_LENGTH
        ):
            raise ValueError(
                f"Address length must be between {cls.MIN_ADDRESS_LENGTH} "
                f"and {cls.MAX_ADDRESS_LENGTH} characters"
            )

        parts = [p.strip() for p in value.split(cls.STRING_SEPARATOR)]
        if len(parts) < cls.MIN_ADDRESS_PARTS:
            raise ValueError(
                "Address must include street name, number, and city, "
                "separated by commas"
            )

        street, number, city = parts[0], parts[1], parts[2]

        if not cls._isalpha(street):
            raise ValueError(
                "Street name must contain only alphabetic "
                "characters and spaces"
            )

        if not any(char.isdigit() for char in number):
            raise ValueError("Street number must contain at least one digit")

        if not cls._isalpha(city):
            raise ValueError(
                "City name must contain only alphabetic characters and spaces"
            )

    def has_pattern(self, pattern: str) -> bool:
        fuzz_threshold = os.getenv("FUZZ_SIMILARITY_THRESHOLD")
        return fuzz.partial_ratio(pattern.lower(), self.value.lower()) > float(
            fuzz_threshold
        )

    def __init__(self, value: str):
        self._address_validation(value)
        super().__init__(value)
