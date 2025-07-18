class CommandParser:
    cmd: str
    args: list[str]

    def __init__(self, user_string: str):
        parts = user_string.strip().split()
        match parts:
            case []:
                self.cmd, self.args = '', []
            case [cmd, *args]:
                self.cmd, self.args = cmd, args

    def unpack(self) -> tuple[str, list[str]]:
        return self.cmd, self.args