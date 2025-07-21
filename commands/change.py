from models import ContactBook, Phone, Address, Note, Record, Email, Birthday


class ActionableItems:
    NOTE = 'note'
    BIRTHDAY = 'birthday'
    EMAIL = 'email'
    ADDRESS = 'address'
    NAME = 'name'


INSTRUCTION_MESSAGE = """
Usage: change <name> <old_phone> <new_phone> or change <name> <property> <old_value> <new_value>
change <name> <old_phone> <new_phone> - change specific phone (contact may have more then 1 phone number) in contact
change <name> note <note_number> <updated_value> - change specific note; please check note's number before starting change it
change <name> birthday <old_value> <new_value> - change contact's birthday
change <name> email <old_value> <new_value> - change contact's email
change <name> address <old_value> <new_value> - change contact's address
change <name> name <old_value> <new_value> - change conctact's name
"""


def input_error(func: callable) -> callable:
    def inner(*args):
        try:
            if len(args) != 2:
                raise ValueError(
                    "Function must receive two arguments: args (list) and contacts (dict)")
            args_list, book = args
            if not isinstance(args_list, list):
                raise TypeError("First argument must be a list")
            if not isinstance(book, ContactBook):
                raise TypeError("Second argument must be an ContactBook")
            if len(args_list) < 3 or len(args_list) > 4:
                raise IndexError(INSTRUCTION_MESSAGE)
            target_record = book.find_by("name", args_list[0])
            if isinstance(target_record, Record):
                return func(args_list, target_record, book)
            else:
                raise ValueError("Contact not found")
        except (TypeError, ValueError, IndexError) as error:
            return str(error)
    return inner


@input_error
def change(args: list, target_record: Record, book: ContactBook) -> str:
    _, *_args = args
    if len(_args) == 2:
        old_phone, new_phone, *_ = _args
        phone = Phone(new_phone)
        old_phone = Phone(old_phone)

        return target_record.edit_phone(old_phone, phone)
    else:
        property, old_value, new_value, *_ = _args
        if property == ActionableItems.NAME:
            old_name = target_record.name.value
            message = target_record.change_name(new_value)
            del book.data[old_name.lower()]
            book.data[new_value.lower()] = target_record
            return message
        if property == ActionableItems.EMAIL:
            return target_record.set_email(Email(new_value))
        if property == ActionableItems.BIRTHDAY:
            return target_record.set_birthday(Birthday(new_value))
        if property == ActionableItems.NOTE:
            return target_record.edit_note(int(old_value), Note(new_value))
        if property == ActionableItems.ADDRESS:
            return target_record.set_address(Address(new_value))
    return "Error: unknown actionable item"
