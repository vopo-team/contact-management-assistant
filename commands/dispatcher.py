from .command import Command

class CommandDispatcher:
    @staticmethod
    def dispatch(book: dict, name: str, args: list[str]) -> str:
        match name:
            case Command.HELLO:
                return ''
            case Command.EXIT | Command.CLOSE:
                return 0
            case Command.ADD:
                return ''
            case Command.CHANGE:
                return ''
            case Command.PHONE:
                return ''
            case Command.ALL:
                return ''
            case Command.ADD_BIRTHDAY:
                return ''
            case Command.BIRTHDAYS:
                return ''
            case Command.SHOW_BIRTHDAY:
                return ''
            case Command.DELETE:
                return ''
            case Command.ADD_ADDRESS:
                return ''
            case Command.SHOW_ADDRESS:
                return ''
            case Command.ADD_EMAIL:
                return ''
            case Command.SHOW_EMAIL:
                return ''
            case Command.ADD_NOTE:
                return ''
            case Command.SHOW_NOTE:
                return ''
            case Command.HELP:
                return ''
            case _:
                return ''