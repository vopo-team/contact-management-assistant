class CommandParser:
    def __init__(self, user_string: str):
        parts = user_string.strip().split()
        self.cmd, *self.args = parts or [""]

    def unpack(self) -> tuple[str, list[str]]:
        return self.cmd, self.args
