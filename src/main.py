import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from commands.dispatcher import CommandDispatcher
from utils import CommandParser, InputNormalizer, PickleReader

load_dotenv()

BOT_GREET_MESSAGE = """
Welcome to the assistant bot!
If you want to see all available commands - use 'help' command.
"""
DB_PATH = (Path(__file__).parent.parent / os.environ["FILE_STORAGE"]).resolve()


def start_bot() -> None:
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


def main() -> None:
    start_bot()


if __name__ == "__main__":
    main()
