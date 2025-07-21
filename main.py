import sys
from utils import *
from commands.dispatcher import CommandDispatcher
import os 
from dotenv import load_dotenv
from utils.format_message import InlineFormatter

load_dotenv()

def start_bot() -> None:
    DB_PATH = os.getenv("FILE_STORAGE")
    reader = PickleReader()

    book = reader.load_data(DB_PATH)

    print(InlineFormatter("Welcome to the assistant bot!").color("cyan").bold().format())

    while True:
        color_input = InlineFormatter("Enter a command: ").color("cyan").format()
        user_input = InputNormalizer(input(color_input))

        cmd, args = CommandParser(str(user_input)).unpack()

        res = CommandDispatcher().dispatch(book, cmd, args)
        if isinstance(res, tuple):
            if res[1] == 0:
                break
        print(InlineFormatter(str(res)).color("green").format())

    reader.save_data(book, DB_PATH)
    sys.exit(0)

if __name__ == "__main__":
    start_bot()
