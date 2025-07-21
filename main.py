import sys
from utils import *
from commands.dispatcher import CommandDispatcher
import os
from dotenv import load_dotenv

load_dotenv()

BOT_GREET_MESSAGE = """
Welcome to the assistant bot! 
If you want to see all available commands - use 'help' command.
"""

def start_bot() -> None:
    DB_PATH = os.getenv("FILE_STORAGE")
    reader = PickleReader()

    book = reader.load_data(DB_PATH)

    print(BOT_GREET_MESSAGE)

    while True:
        user_input = InputNormalizer(input("Enter a command: "))

        cmd, args = CommandParser(str(user_input)).unpack()

        res = CommandDispatcher().dispatch(book, cmd, args)
        if isinstance(res, int) and res == 0:
            break

        print(res)

    reader.save_data(book, DB_PATH)
    sys.exit(0)


if __name__ == "__main__":
    start_bot()
