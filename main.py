import sys
from utils import *
from commands.dispatcher import CommandDispatcher

def start_bot() -> None:
    contact_book = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = InputNormalizer(input("Enter a command: "))

        cmd, args = CommandParser(user_input).unpack()

        res = CommandDispatcher().dispatch(contact_book, cmd, args)
        if res == 0:
            break
        
        print(res)

    sys.exit(0)

if __name__ == "__main__":
    start_bot()
