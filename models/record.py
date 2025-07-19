from typing import Optional
from .name import Name
from .note import Note

class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []
        self.tags = []
        self.email = None
        self.address = None
        self.note = None
        self.birthday = None

         # === Note ===
    def get_note(self) -> Optional[Note]:
        return self._note

    def set_note(self, value: Note) -> str:
        self._note = value
        return f"Note changed to: {value}"

    def delete_note(self) -> str:
        old_value = self._note
        self._note = None
        return f"Note '{old_value}' deleted."