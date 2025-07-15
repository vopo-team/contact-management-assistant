import re
from models.field import Field


class Email(Field):
    def __init__(self, email: str):
        pattern = r'^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError(f"Invalid email format: {email}")
        super().__init__(email)
