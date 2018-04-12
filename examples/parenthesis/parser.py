from parenthesis.token import TokenEnum
from parenthesis.scanner import scanner

tokens = None
token = None


def match(expected):
    global token
    global tokens

    if token.kind is expected:
        tokens.consume()
        token = tokens.peek()
        return True
    else:
        print("Expected {0} but got {1}".format(expected, token.kind))
        return False


# expression  ::= parenthesis
#               | brackets
#               | \epsilon
def expression():
    global token

    if token.kind is TokenEnum.OPEN_PAREN:
        return parenthesis()
    elif token.kind is TokenEnum.OPEN_BRACKET:
        return brackets()
    else:
        return True


# parenthesis ::= ( expression )
def parenthesis():
    print("parenthesis")
    return match(TokenEnum.OPEN_PAREN) and expression() and match(TokenEnum.CLOSE_PAREN)


# brackets    ::= [ expression ]
def brackets():
    return match(TokenEnum.OPEN_BRACKET) and expression() and match(TokenEnum.CLOSE_BRACKET)


def parser():
    if expression():
        if token.kind is TokenEnum.EOF:
            return True
        else:
            print("Expected {0} but got {1}".format(TokenEnum.EOF, token.kind))
            return False
    else:
        return False


def setup():
    # set up the environment
    global token
    global tokens

    line = input("Please enter a line to parse.\n")

    tokens = scanner(line)
    if tokens:
        token = tokens.peek()
        print(parser())
    else:
        print(False)


if __name__ == "__main__":
    while True:
        setup()
