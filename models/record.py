from .name import Name
from .phone import Phone
class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []
        self.notes = []
        self.email = None
        self.address = None
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

        return f"The phone number {target_index} renamed to {new_phone}"