from typing import Optional
from .name import Name
from .birthday import Birthday

class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []
        self.tags = []
        self.email = None
        self.address = None
        self.note = None
        self._birthday = None 

    def get_birthday(self) -> Optional[Birthday]:
        return self._birthday

    def set_birthday(self, value: Birthday) -> str:
        self._birthday = value
        return f"Birthday changed to: {value}"

    def delete_birthday(self) -> str:
        old_value = self._birthday
        self._birthday = None
        return f"Birthday '{old_value}' deleted."
