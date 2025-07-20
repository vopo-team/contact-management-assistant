from commands import *
from models import ContactBook
class CommandDispatcher:
    @staticmethod
    def dispatch(book: ContactBook, name: str, args: list[str]) -> tuple[str, int] | str:
        match name:
            case Command.HELLO:
                return hello()
            case Command.EXIT | Command.CLOSE:
                return close(), 0
            case Command.ADD:
                return add(args, book)
            case Command.CHANGE:
                return change(args, book)
            case Command.FIND:
                return find_by(args, book)
            case Command.ALL:
                return str(book)
            case Command.BIRTHDAYS:
                return birthdays(args, book)
            case Command.DELETE:
                return delete(args, book)
            case Command.FIND_NOTES:
                return find_notes(args, book)
            case _:
                return invalid(name)