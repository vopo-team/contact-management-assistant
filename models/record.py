from typing import Optional
from .name import Name
from .birthday import Birthday
from .email import Email
from .address import Address
from .note import Note
from .phone import Phone
from .tag import Tag
from utils.format_message import FormatMessage

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.notes = []
        self._email = None
        self._address = None
        self._birthday = None 

    def __str__(self):
        return f"""
Contact name: {self.name},
Phones: {', '.join(p.value for p in self.phones)};
Birthday: {self._birthday};
Address: {self._address};
Email: {self._email};
Notes:\n{'\n'.join(f"[{i+1}] {str(p)}" for i, p in enumerate(self.notes))}"""
    
    @classmethod
    def validate_birthday(cls, value: Birthday) -> str:
        if not isinstance(value, Birthday):
            raise TypeError("Birthday value should be object of Birthday class.")
    
    @classmethod
    def validate_email(cls, value: Email) -> str:
        if not isinstance(value, Email):
            raise TypeError("Email value should be object of Email class.")
    
    @classmethod
    def validate_address(cls, value: Address) -> str:
        if not isinstance(value, Address):
                raise TypeError("Address value should be object of Address class.")
    
    @classmethod
    def validate_name(cls, value: Name) -> str:
        if not isinstance(value, Name):
            raise TypeError("Name value should be object of Name class.")
    
    @classmethod
    def validate_note(cls, value: Note) -> str:
        if not isinstance(value, Note):
                raise TypeError("Note value should be object of Note class.")
        
    @classmethod
    def validate_phone(cls, value: Phone) -> str:
        if not isinstance(value, Phone):
            raise TypeError("Phone value should be object of Phone class.")

    @classmethod
    def validate_tag(cls, value: Tag) -> str:
        if not isinstance(value, Tag):
            raise TypeError("Tag value should be object of Tag class.")

    def get_birthday(self) -> Optional[Birthday]:
        return self._birthday

    def set_birthday(self, value: Birthday) -> str:
        Record.validate_birthday(value)
        self._birthday = value
        return f"Birthday changed to: {value}."

    def delete_birthday(self) -> str:
        old_value = self._birthday
        self._birthday = None
        return f"Birthday '{old_value}' deleted."

    def get_email(self) -> Optional[Email]:
        return self._email

    def set_email(self, value: Email) -> str:
        Record.validate_email(value)
        self._email = value
        return f"Email changed to: {value}."

    def delete_email(self) -> str:
        old_value = self._email
        self._email = None
        return f"Email '{old_value}' deleted."

    def get_address(self) -> Optional[Address]:
        return self._address

    def set_address(self, value: Address) -> str:
        Record.validate_address(value)
        self._address = value
        return f"Address changed to: {value}."

    def delete_address(self) -> str:
        old_value = self._address
        self._address = None
        return f"Address '{old_value}' deleted."
    
    def has_phone(self, phone: Phone) -> bool:
        return phone in self.phones

    def add_phone(self, phone: Phone) -> str:
        Record.validate_phone(phone)
        if self.has_phone(phone):
            return 'This phone number already exists.'
        self.phones.append(phone)
        return 'Phone number added.'
    
    def remove_phone(self, phone: Phone) -> str:
        Record.validate_phone(phone)
        if not self.has_phone(phone):
            return "Record hasn't this phone number."
        self.phones.remove(phone)
        return "Phone number removed."
    
    def edit_phone(self, target_phone: Phone, new_phone: Phone) -> str:
        Record.validate_phone(target_phone)
        Record.validate_phone(new_phone)

        if not self.has_phone(target_phone):
            return "Target phone number doesn't exist."
        if self.has_phone(new_phone):
            return "The new phone number already exists in this contact."
        target_index = self.phones.index(target_phone)
        self.phones[target_index] = new_phone
        return 'Phone edited.'
    
    def add_note(self, note: Note) -> str:
        Record.validate_note(note)
        self.notes.append(note)
        return 'Note added.'
    
    def get_note(self, num: int) -> Note | str:
        if isinstance(num, int):
            index = num - 1
            if 0 <= index < len(self.notes):
                return self.notes[index]
            return "Note number out of range."
        return "Argument must be int."
    
    def get_notes_by_tag(self, target_tag: Tag) -> list[Note]:
        list = []

        for note in self.notes:
            if note.has_tag(target_tag):
                list.append(str(note))
        
        return list

    def remove_note(self, value: int) -> str:
        target_note = self.get_note(value)
        if not isinstance(target_note, Note):
            return target_note
        self.notes.remove(target_note)
        return "Note removed."
    
    def edit_note(self, num: int, new_note: Note) -> str:
        Record.validate_note(new_note)
        target_note = self.get_note(num)
        if not isinstance(target_note, Note):
            return target_note
        target_index = self.notes.index(target_note)
        self.notes[target_index] = new_note
        return "Note edited."

    def change_name(self, new_name: str) -> str:
        self.name = Name(new_name)
        return 'Name changed.'