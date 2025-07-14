from .hello import hello_command
from .close import close_command
from .invalid import invalid_command
from .add import add_contact
from .change import change_contact
from .phone import show_contact
from .all import show_all
from .add_birthday import add_birthday
from .show_birthday import show_birthday
from .birthdays import birthdays

class Command:
    HELLO = "hello"
    CLOSE = "close"
    EXIT = "exit"
    ADD = "add"
    INVALID = "invalid"
    CHANGE = "change"
    PHONE = "phone"
    ALL = "all"
    ADD_BIRTHDAY = "add-birthday"
    BIRTHDAYS = "birthdays"
    SHOW_BIRTHDAY = "show-birthday"

COMMAND_HANDLERS = {
    Command.HELLO: hello_command,
    Command.CLOSE: close_command,
    Command.EXIT: close_command,
    Command.ADD: add_contact,
    Command.INVALID: invalid_command,
    Command.CHANGE: change_contact,
    Command.PHONE: show_contact,
    Command.ALL: show_all,
    Command.ADD_BIRTHDAY: add_birthday,
    Command.SHOW_BIRTHDAY: show_birthday,
    Command.BIRTHDAYS: birthdays
}

__all__ = ["COMMAND_HANDLERS", "Command"]