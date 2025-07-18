from .name import Name

class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []
        self.tags = []
        self.email = None
        self.address = None
        self.note = None
        self.birthday = None