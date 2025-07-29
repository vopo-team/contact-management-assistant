from colorama import Back, Fore, Style, init

init(autoreset=True)


class ColorMessage:
    def __init__(self, text):
        self.text = text

    # Foreground colors
    def black(self):
        self.text = f"{Fore.BLACK}{self.text}"
        return self

    def red(self):
        self.text = f"{Fore.RED}{self.text}"
        return self

    def green(self):
        self.text = f"{Fore.GREEN}{self.text}"
        return self

    def yellow(self):
        self.text = f"{Fore.YELLOW}{self.text}"
        return self

    def blue(self):
        self.text = f"{Fore.BLUE}{self.text}"
        return self

    def magenta(self):
        self.text = f"{Fore.MAGENTA}{self.text}"
        return self

    def cyan(self):
        self.text = f"{Fore.CYAN}{self.text}"
        return self

    def white(self):
        self.text = f"{Fore.WHITE}{self.text}"
        return self

    def reset_fore(self):
        self.text = f"{Fore.RESET}{self.text}"
        return self

    # Background colors
    def on_black(self):
        self.text = f"{Back.BLACK}{self.text}"
        return self

    def on_red(self):
        self.text = f"{Back.RED}{self.text}"
        return self

    def on_green(self):
        self.text = f"{Back.GREEN}{self.text}"
        return self

    def on_yellow(self):
        self.text = f"{Back.YELLOW}{self.text}"
        return self

    def on_blue(self):
        self.text = f"{Back.BLUE}{self.text}"
        return self

    def on_magenta(self):
        self.text = f"{Back.MAGENTA}{self.text}"
        return self

    def on_cyan(self):
        self.text = f"{Back.CYAN}{self.text}"
        return self

    def on_white(self):
        self.text = f"{Back.WHITE}{self.text}"
        return self

    def reset_back(self):
        self.text = f"{Back.RESET}{self.text}"
        return self

    # Styles
    def dim(self):
        self.text = f"{Style.DIM}{self.text}"
        return self

    def normal(self):
        self.text = f"{Style.NORMAL}{self.text}"
        return self

    def bold(self):
        self.text = f"{Style.BRIGHT}{self.text}"
        return self

    def reset_style(self):
        self.text = f"{Style.RESET_ALL}{self.text}"
        return self

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text
