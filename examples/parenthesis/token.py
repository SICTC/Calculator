import enum


class Tokens(object):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def append(self, token):
        self.data.append(token)

    def consume(self):
        self.data.pop(0)

    def peek(self):
        return self.data[0]



class Token(object):
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __str__(self):
        return "{0}, {1}".format(self.kind, self.value)


class TokenEnum(enum.Enum):
    OPEN_PAREN = enum.auto()
    CLOSE_PAREN = enum.auto()
    OPEN_BRACKET = enum.auto()
    CLOSE_BRACKET = enum.auto()
    EOF = enum.auto()
