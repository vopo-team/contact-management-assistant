from collections import UserDict
from models.record import Record
from datetime import datetime, timedelta
from models.name import Name
from models.phone import Phone
from models.email import Email
from models.address import Address
from models.birthday import Birthday
from models.tag import Tag
import os
from utils import FuzzComparator


class SearchCriterios:
    NAME = 'name'
    BIRTHDAY = 'birthday'
    EMAIL = 'email'
    PHONE = 'phone'
    ADDRESS = 'address'
    TAG = 'tag'
    NOTE = 'note'
    NOTE_PATTERN = 'note-pattern'


class ContactBook(UserDict):
    __SATURDAY_NUMBER = 5
    __REQUIRED_NAME_ATTR = 'name'

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"***\n{'***\n'.join(str(p) for p in self.data.values())}***"

    def add_record(self, record: Record) -> str:
        self.data[record.name.value.lower()] = record
        return "Record added."

    @staticmethod
    def __get_next_user_birthday(current_date: datetime.date, user_birthday: datetime.date) -> datetime.date:
        birthday_this_year = user_birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            next_year = current_date.year + 1
            user_birthday_next = birthday_this_year.replace(year=next_year)
        else:
            user_birthday_next = birthday_this_year

        return user_birthday_next

    @staticmethod
    def __get_number_of_days_to_birthday(user_birthday_next: datetime.date, current_date: datetime.date) -> int:
        return (user_birthday_next - current_date).days

    @staticmethod
    def __get_accurate_date_considering_weekends(user_birthday_next: datetime.date) -> datetime.date:
        celebration_date = user_birthday_next

        if celebration_date.weekday() >= ContactBook.__SATURDAY_NUMBER:
            celebration_date += timedelta(days=7 - celebration_date.weekday())
        return celebration_date

    def get_upcoming_birthdays(self, days_to_birthday: int) -> list[Record]:
        res = []
        current_date = datetime.today().date()

        for user in self.data.values():
            if user._birthday is None:
                continue
            if not hasattr(user, ContactBook.__REQUIRED_NAME_ATTR) or user.name is None:
                raise ValueError("Missing 'name'")

            datetime_pattern = os.getenv("DATETIME_OBJECT_PATTERN")

            user_birthday = datetime.strptime(
                user._birthday.value, datetime_pattern).date()

            birthday_this_year = user_birthday.replace(year=current_date.year)

            user_next_birthday = self.__get_next_user_birthday(
                current_date, birthday_this_year)

            days_diff = self.__get_number_of_days_to_birthday(
                user_next_birthday, current_date)

            if days_diff <= days_to_birthday:
                celebration_date = self.__get_accurate_date_considering_weekends(
                    user_next_birthday)
                res.append({"name": user.name.value,
                           "congratulation_date": celebration_date})

        return res

    def find_by(self, criteria: str, value: str | int | Name | Phone | Email | Address | Tag | Birthday) -> Record | list[Record] | None:
        match criteria:
            case SearchCriterios.NAME:
                return self.data.get(value)
            case SearchCriterios.BIRTHDAY:
                Record.validate_birthday(value)
                for record in self.data.values():
                    if record.get_birthday() == value:
                        return record
            case SearchCriterios.EMAIL:
                Record.validate_email(value)
                for record in self.data.values():
                    if record.get_email() == value:
                        return record
            case SearchCriterios.PHONE:
                Record.validate_phone(value)
                for record in self.data.values():
                    if record.has_phone(value):
                        return record
            case SearchCriterios.ADDRESS:
                Record.validate_address(value)
                for record in self.data.values():
                    has_pattern = FuzzComparator(
                        record.get_address()).matches(value)
                    if has_pattern:
                        return record
            case SearchCriterios.TAG:
                Record.validate_tag(value)
                result = []

                for record in self.data.values():

                    notes = record.get_notes_by_tag(value)

                    if len(notes) != 0:
                        result.append(record)

                return " ".join(str(p) for p in result)
            case SearchCriterios.NOTE_PATTERN:
                result = []
                for record in self.data.values():
                    for note in record.notes:
                        has_pattern = FuzzComparator(note).matches(value)
                        if has_pattern:
                            result.append(record)
                return " ".join(str(p) for p in result)
            case _:
                return 'Error: Invalid criteria'

    def delete_record(self, name: str) -> str:
        try:
            del self.data[name]
            return 'Record deleted'
        except KeyError:
            raise ValueError(f"{name} not found in AddressBook")
