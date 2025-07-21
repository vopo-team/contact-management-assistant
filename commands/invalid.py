import textwrap
from commands.command import Command
from utils.fuzz_comparator import FuzzComparator


def invalid(command: str) -> str:
    for value in vars(Command).values():
        if isinstance(value, str):
            has_pattern = FuzzComparator(command).matches(value)
            if has_pattern:
                return f"Error: Invalid command '{command}'. Try to start with '{value}' to see the hint"
    return textwrap.dedent(f"Error: Invalid command '{command}'.")
