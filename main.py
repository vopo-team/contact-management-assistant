import sys
from utils import *
from commands.dispatcher import CommandDispatcher
import os 
from dotenv import load_dotenv

load_dotenv()

def start_bot() -> None:
    DB_PATH = os.getenv("FILE_STORAGE")
    print(DB_PATH)
    reader = PickleReader()

    book = reader.load_data(DB_PATH)

    print("Welcome to the assistant bot!")

    while True:
        user_input = InputNormalizer(input("Enter a command: "))

        cmd, args = CommandParser(str(user_input)).unpack()

        res = CommandDispatcher().dispatch(book, cmd, args)
        if isinstance(res, tuple):
            print(res[0])
            if res[1] == 0:
                break
        
        print(res)

    reader.save_data(book, DB_PATH)
    sys.exit(0)

if __name__ == "__main__":
    start_bot()
