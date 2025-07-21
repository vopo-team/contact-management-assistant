from models import ContactBook, Note, Tag


INSTRUCTION_MESSAGE = "Usage: find-notes <name> <tag>"


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
                raise IndexError(INSTRUCTION_MESSAGE)
            return func(*args, **kwargs)
        except (TypeError, ValueError, IndexError) as error:
            return str(error)
    return inner


@input_error
def find_notes(args: list, book: ContactBook) -> list[Note]:
    name, tag = args
    record = book.find_by("name", name)
    return " ".join(record.get_notes_by_tag(Tag(tag)))
