import textwrap

def invalid(command: str) -> str:
    return textwrap.dedent(f"""\
        Error: Invalid command '{command}'. To see available commands please use: 
            'help'
    """)