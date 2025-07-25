from models import Phone, Tag, Record, ContactBook, Note


class ActionableItems:
    NOTE = 'note'
    TAG = 'tag'
    CONTACT = 'contact'


INSTRUCTION_MESSAGE = """
Usage: add contact <name> <phone> or add <order> <item> <value>
add contact <name> <phone> - create new contact
add <order> tag <note_number> <tag_name> - add tag to specific note by contact's name and note number
add <order> note <word1> <word2> ... - add note to the contact (unlimited variables after 'note')
"""


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
            if len(args_list) < 2:
                raise IndexError(INSTRUCTION_MESSAGE)
            return func(*args, **kwargs)

        except (TypeError, ValueError, IndexError) as error:
            return str(error)
    return inner


@input_error
def add(args: list, book: ContactBook) -> str:
    if args[0] == ActionableItems.CONTACT:
        _, name, __phone = args
        new_phone = Phone(__phone)    
        record = Record(name)
        book.add_record(record)
        record.add_phone(new_phone)
        return "Contact added."
    else:
        order, item, *_args = args
        record = book.find_by("order", int(order))
        if item == ActionableItems.NOTE:
            return record.add_note(Note(" ".join(_args)))
        if item == ActionableItems.TAG:
            note = record.get_note(int(_args[0]))
            if isinstance(note, str):
                return "Selected note doesn't exist."
            return note.add_tag(Tag(_args[1]))
    return "Error: unknown actionable item."
