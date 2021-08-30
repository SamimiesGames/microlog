from colorama import Style


class Asset:
    def __init__(self, content, *style, reset=True):
        self.content = content
        self.style = style

        self.reset = reset

    def __str__(self):
        before = "".join(self.style)

        after = Style.RESET_ALL if self.reset else ""

        message = f"{before}{self.content}{after}"

        return message
