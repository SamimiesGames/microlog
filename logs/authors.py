from logs.assets import UNSPECIFIED


def create_author(name):
    def wrapper(cls):
        setattr(cls, "__author__", name)
        setattr(cls, "rename_author", rename_author)

        return cls

    return wrapper


def rename_author(self, name):
    self.__author__ = name


def block_sniffing(_bool: bool):
    def wrapper(cls):
        setattr(cls, "__no_sniff__", _bool)

        return cls

    return wrapper


@create_author(name=UNSPECIFIED)
class UnspecifiedAuthor:
    ...


UNSPECIFIED_AUTHOR = UnspecifiedAuthor()
