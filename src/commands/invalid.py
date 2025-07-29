import textwrap

from commands.command import Command
from utils.fuzz_comparator import FuzzComparator


def invalid(command: str) -> str:
    for value in vars(Command).values():
        if isinstance(value, str):
            has_pattern = FuzzComparator(command).matches(value)
            if has_pattern:
                return f"""
Error: Invalid command '{command}'.
Maybe you mean '{value}' command, try use it to see the hint.
If you want to see all available commands - use 'help' command.
                        """
    return textwrap.dedent(f"Error: Invalid command '{command}'.")
