from models import ContactBook

def input_error(func: callable) -> callable:
    def inner(*args, **kwargs):
        try:
            if len(args) != 2:
                raise ValueError("Function must receive two arguments: args (list) and contacts (dict).")
            args_list, book = args
            if not isinstance(args_list, list):
                raise TypeError("First argument must be a list.")
            if not isinstance(book, ContactBook):
                raise TypeError("Second argument must be an ContactBook.")
            if len(args_list) != 1 and int(args_list[0]):
                raise IndexError("Usage: birthdays <days>")
            return func(*args, **kwargs)

        except (TypeError, ValueError, IndexError) as error:
            return str(error)
    return inner

@input_error
def birthdays(args: list, book: ContactBook) -> str:
    return book.get_upcoming_birthdays(int(args[0]))


