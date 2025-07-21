from models import ContactBook, Tag, Record, Phone, Name, Birthday, Email, Address


class ActionableItems:
    BIRTHDAY = 'birthday'
    ADDRESS = 'address'
    EMAIL = 'email'
    PHONE = 'phone'
    NAME = 'name'
    TAG = 'tag'
    NOTE_PATTERN = 'note-pattern'


def input_error(func: callable) -> callable:
    def inner(*args, **kwargs):
        try:
            if len(args) != 2:
                raise ValueError(
                    "Function must receive two arguments: args (list) and contacts (dict)")
            args_list, book = args
            if not isinstance(args_list, list):
                raise TypeError("First argument must be a list")
            if not isinstance(book, ContactBook):
                raise TypeError("Second argument must be an ContactBook")
            if len(args_list) != 2:
                raise ValueError("Usage: find <property> <name>")
            return func(*args, **kwargs)
        except (TypeError, ValueError, IndexError) as error:
            return str(error)
    return inner


@input_error
def find_by(args: list, book: ContactBook) -> str | Record | list[Record]:
    property, value = args
    if property == ActionableItems.NAME:
        return book.find_by(ActionableItems.NAME, Name(value))
    elif property == ActionableItems.BIRTHDAY:
        return book.find_by(ActionableItems.BIRTHDAY, Birthday(value))
    elif property == ActionableItems.EMAIL:
        return book.find_by(ActionableItems.EMAIL, Email(value))
    elif property == ActionableItems.ADDRESS:
        return book.find_by(ActionableItems.ADDRESS, Address(value))
    elif property == ActionableItems.PHONE:
        return book.find_by(ActionableItems.PHONE, Phone(value))
    elif property == ActionableItems.TAG:
        return book.find_by(ActionableItems.TAG, Tag(value))
    elif property == ActionableItems.NOTE_PATTERN:
        return book.find_by(ActionableItems.NOTE_PATTERN, value)
    return 'Error: Unknown action item.'
