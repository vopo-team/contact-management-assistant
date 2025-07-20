from typing import Optional
from .name import Name
from .address import Address
from .note import Note
from .phone import Phone

class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []
        self.notes = []
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
      
    def get_note(self) -> Optional[Note]:
        return self._note

    def set_note(self, value: Note) -> str:
        return f"Note changed to: {value}"

    def delete_note(self) -> str:
        old_value = self._note
        self._note = None
        return f"Note '{old_value}' deleted."
        self.birthday = None
    
    def has_phone(self, phone: Phone) -> bool:
        return phone in self.phones

    def add_phone(self, phone: Phone) -> str:
        if self.has_phone(phone):
            return 'This phone number already exists.'
        self.phones.append(phone)
        return 'Phone number added.'
    
    def remove_phone(self, phone: Phone) -> str:
        if not self.has_phone(phone):
            return "Record hasn't this phone number"
        self.phones.remove(phone)
        return "Phone number removed."
    
    def edit_phone(self, target_phone: Phone, new_phone: Phone) -> str:
        if not self.has_phone(target_phone):
            return "Target phone number doesn't exist"
        if self.has_phone(new_phone):
            return "The new phone number already exists in this contact."
        target_index = self.phones.index(target_phone)
        self.tags[target_index] = new_phone

