from models import ContactBook, Phone


class ActionableItems:
    BIRTHDAY = "birthday"
    ADDRESS = "address"
    EMAIL = "email"
    NOTE = "note"
    PHONE = "phone"
    CONTACT = "contact"
    NAME = "name"


INSTRUCTION_MESSAGE = """
Usage: delete contact <order> or delete <order> <property> or delete <order> <property> <value>
delete contact <order> - delete specific contact by name
delete <order> birthday - delete birthday in specific contact
delete <order> address - delete address in specific contact
delete <order> email - delete email in specific contact
delete <order> name - delete name in specific contact
delete <order> note <note_number> - delete specific note by note's number in specific contact
delete <order> phone <phone_number> - delete specific number in specific contact
"""


def input_error(func: callable) -> callable:
    def inner(*args, **kwargs):
        try:
            if len(args) != 2:
                raise ValueError(
                    "Function must receive two arguments: args (list) and contacts (dict)."
                )
            args_list, book = args
            if not isinstance(args_list, list):
                raise TypeError("First argument must be a list.")
            if not isinstance(book, ContactBook):
                raise TypeError("Second argument must be an ContactBook.")
            if len(args_list) < 2 or len(args_list) > 3:
                raise IndexError(INSTRUCTION_MESSAGE)

            return func(*args, **kwargs)

        except (TypeError, ValueError, IndexError) as error:
            return str(error)

    return inner


@input_error
def delete(args: list, book: ContactBook) -> str:
    if args[0] == ActionableItems.CONTACT:
        order = args[1]
        return book.delete_record(order)
    order = args[0]
    record = book.find_by("order", int(order))

    if len(args) == 2:
        order, property = args
        if property == ActionableItems.BIRTHDAY:
            return record.delete_birthday()
        if property == ActionableItems.ADDRESS:
            return record.delete_address()
        if property == ActionableItems.EMAIL:
            return record.delete_email()
        if property == ActionableItems.NAME:
            print("ewrwer)")
            return record.delete_name()
    else:
        _, property, item = args
        if property == ActionableItems.NOTE:
            return record.remove_note(int(item))
        if property == ActionableItems.PHONE:
            return record.remove_phone(Phone(item))
    return "Error: unknown actionable item"
