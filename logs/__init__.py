from .authors import *
from .assets import *
from .wraps import *

LOG_PATH = None
VERBOSE = True


def attempt_log(message):
    if isinstance(LOG_PATH, str):
        with open(LOG_PATH, "a") as fh:
            fh.write(message)
            fh.close()


def log(*args, emphasis=False, author=UNSPECIFIED_AUTHOR):
    if author:
        sniffing_blocked = hasattr(author, "__no_sniff__")

        assert hasattr(author, "__author__")
        assert not sniffing_blocked

    author = f"[{important_data_item(author.__author__, quote=False)}] " if author else ""

    if VERBOSE:
        args = [str(arg) for arg in args]
        message = " ".join(args)
        message = f"{author}{message}"

        if emphasis:
            message = message.upper()

        attempt_log(message)

        return print(message)


def flush_log():
    attempt_log("\n")
    print()
