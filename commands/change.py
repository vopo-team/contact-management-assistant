from models import ContactBook, Phone, Address, Note, Record, Email, Birthday


class ActionableItems:
    NOTE = 'note'
    BIRTHDAY = 'birthday'
    EMAIL = 'email'
    ADDRESS = 'address'
    NAME = 'name'
    PHONE = 'phone'


INSTRUCTION_MESSAGE = """
Usage: change <order> <new_value> or change <order> <property> <old_value> <new_value>
change <order> birthday <new_value> - change contact's birthday
change <order> email <new_value> - change contact's email
change <order> address <new_value> - change contact's address
change <order> name <new_value> - change conctact's name
change <order> note <note_number> <updated_value> - change specific note; please check note's number before starting change it
change <order> phone <old_phone> <new_phone> - change specific phone (contact may have more then 1 phone number) in contact

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
            target_record = book.find_by("order", int(args_list[0]))
            if isinstance(target_record, Record):
                return func(args_list, target_record, book)
            else:
                raise ValueError("Contact not found")
        except (TypeError, ValueError, IndexError) as error:
            return str(error)
    return inner


@input_error
def change(args: list, target_record: Record, book: ContactBook) -> str:
    _, property, old_value, new_value, *_ = args
    if property == ActionableItems.NAME:
        return target_record.set_name(new_value)
    if property == ActionableItems.EMAIL:
        return target_record.set_email(Email(new_value))
    if property == ActionableItems.BIRTHDAY:
        return target_record.set_birthday(Birthday(new_value))
    if property == ActionableItems.ADDRESS:
        return target_record.set_address(Address(new_value))
    if property == ActionableItems.NOTE:
        note_number = int(old_value)
        return target_record.edit_note(note_number, Note(new_value))
    if property == ActionableItems.PHONE:
        old_phone = Phone(old_value)
        new_phone = Phone(new_value)
        return target_record.edit_phone(old_phone, new_phone)
    return "Error: unknown actionable item"
