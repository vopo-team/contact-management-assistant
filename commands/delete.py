from models import Phone, ContactBook


class ActionableItems:
    BIRTHDAY = 'birthday'
    ADDRESS = 'address'
    EMAIL = 'email'
    NOTE = 'note'
    PHONE = 'phone'


def input_error(func: callable) -> callable:
    def inner(*args, **kwargs):
        try:
            if len(args) != 2:
                raise ValueError(
                    "Function must receive two arguments: args (list) and contacts (dict).")
            args_list, book = args
            if not isinstance(args_list, list):
                raise TypeError("First argument must be a list.")
            if not isinstance(book, ContactBook):
                raise TypeError("Second argument must be an ContactBook.")
            if len(args_list) < 1 or len(args_list) > 3:
                raise IndexError(
                    "Usage: delete <name>\nor\ndelete <name> <key>\nor\ndelete <name> <key> <value>")
            return func(*args, **kwargs)

        except (TypeError, ValueError, IndexError) as error:
            return str(error)
    return inner


@input_error
def delete(args: list, book: ContactBook) -> str:
    name, *_args = args
    record = book.find_by("name", name)
    if len(_args) == 0:
        return book.delete_record(name)
    elif len(_args) == 1:
        property, *_ = _args
        if property == ActionableItems.BIRTHDAY:
            return record.delete_birthday()
        if property == ActionableItems.ADDRESS:
            return record.delete_address()
        if property == ActionableItems.EMAIL:
            return record.delete_email()
    else:
        property, item = _args
        if property == ActionableItems.NOTE:
            return record.remove_note(int(item))
        if property == ActionableItems.PHONE:
            return record.remove_phone(Phone(item))
    return "Error: unknown actionable item"
