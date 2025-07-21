from models import Phone, Tag, Record, ContactBook, Note


class ActionableItems:
    NOTE = 'note'
    TAG = 'tag'


INSTRUCTION_MESSAGE = """
Usage: add <name> <phone> or add <name> <item> <value>
add <name> <phone> - add phone to contact by contact's name
add <name> tag <note_number> <tag_name> - add tag to specific note by contact's name and note number
add <name> note <word1> <word2> ... - add note to the contact (unlimited variables after 'note')
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
    name, *_args = args
    if len(_args) == 1:
        __phone, *_ = _args
        record = book.find_by("name", name)
        new_phone = Phone(__phone)
        message = "Contact updated."
        if not isinstance(record, Record):
            record = Record(name)
            book.add_record(record)
            message = "Contact added."
        record.add_phone(new_phone)
        return message
    else:
        item, *_args = _args
        record = book.find_by("name", name)
        if item == ActionableItems.NOTE:
            return record.add_note(Note(" ".join(_args)))
        if item == ActionableItems.TAG:
            note = record.get_note(int(_args[0]))
            return note.add_tag(Tag(_args[1]))
    return "Error: unknown actionable item"
