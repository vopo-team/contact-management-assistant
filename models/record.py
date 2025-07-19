from typing import Optional
from .name import Name
from .email import Email

class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []
        self.tags = []
        self.email = None
        self.address = None
        self.note = None
        self.birthday = None


      # === Email ===
    def get_email(self) -> Optional[Email]:
        return self._email

    def set_email(self, value: Email) -> str:
        self._email = value
        return f"Email changed to: {value}"

    def delete_email(self) -> str:
        old_value = self._email
        self._email = None
        return f"Email '{old_value}' deleted."