import textwrap
from utils.format_message import FormatMessage

@FormatMessage
def invalid(command: str) -> str:
    return textwrap.dedent(f"Error: Invalid command '{command}'. \n Please use one of the available commands:\n Use 'help' to see the list of commands.")