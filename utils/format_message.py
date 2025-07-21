from utils.color_message import ColorMessage
from colorama import init

init(autoreset=True)


class FormatMessage:
    def __init__(self, func):
        self.func = func
        self.rules = [
            ("Usage", lambda msg: ColorMessage(msg).black().on_yellow().bold()),
            ("Function must", lambda msg: ColorMessage(msg).white().on_blue()),
            ("First argument", lambda msg: ColorMessage(msg).white().on_blue()),
            ("Second argument", lambda msg: ColorMessage(msg).white().on_magenta()),
            ("Error:", lambda msg: ColorMessage(msg).white().on_red().bold()),
            ("Contact added", lambda msg: ColorMessage(
                msg).on_green().white().bold()),
            ("Contact updated", lambda msg: ColorMessage(
                msg).on_cyan().black().bold()),
        ]

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        if not isinstance(result, str):
            return result

        for start, style_fn in self.rules:
            if result.startswith(start) or start in result:
                return style_fn(result)

        return result


class InlineFormatter:
    def __init__(self, text: str):
        self.msg = ColorMessage(text)

    def color(self, fore_color: str = "white"):
        color_map = {
            "black": self.msg.black,
            "red": self.msg.red,
            "green": self.msg.green,
            "yellow": self.msg.yellow,
            "blue": self.msg.blue,
            "magenta": self.msg.magenta,
            "cyan": self.msg.cyan,
            "white": self.msg.white,
        }
        if fore_color in color_map:
            self.msg = color_map[fore_color]()
        return self

    def background(self, back_color: str = None):
        back_map = {
            "black": self.msg.on_black,
            "red": self.msg.on_red,
            "green": self.msg.on_green,
            "yellow": self.msg.on_yellow,
            "blue": self.msg.on_blue,
            "magenta": self.msg.on_magenta,
            "cyan": self.msg.on_cyan,
            "white": self.msg.on_white,
        }
        if back_color in back_map:
            self.msg = back_map[back_color]()
        return self

    def style(self, style: str = None):
        if style == "bold":
            self.msg = self.msg.bold()
        elif style == "dim":
            self.msg = self.msg.dim()
        elif style == "normal":
            self.msg = self.msg.normal()
        return self

    def bold(self):
        self.msg = self.msg.bold()
        return self

    def format(self) -> str:
        return str(self.msg)
