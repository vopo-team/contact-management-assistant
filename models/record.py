from typing import Optional
from .name import Name
from .address import Address

class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []
        self.tags = []
        self.email = None
        self._address = None
        self.note = None
        self.birthday = None


         # === Address ===
    def get_address(self) -> Optional[Address]:
        return self._address

    def set_address(self, value: Address) -> str:
        self._address = value
        return f"Address changed to: {value}"

    def delete_address(self) -> str:
        old_value = self._address
        self._address = None
        return f"Address '{old_value}' deleted."