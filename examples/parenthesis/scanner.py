from parenthesis.token import Token, TokenEnum, Tokens
import string


def scanner(line):
    tokens = Tokens()
    failed = False
    for c in line:
        token = None
        if c in string.whitespace:
            continue
        elif c in ["("]:
            token = Token(TokenEnum.OPEN_PAREN, c)
        elif c in [")"]:
            token = Token(TokenEnum.CLOSE_PAREN, c)
        elif c in ["["]:
            token = Token(TokenEnum.OPEN_BRACKET, c)
        elif c in ["]"]:
            token = Token(TokenEnum.CLOSE_BRACKET, c)
        else:
            print("Error: Illegal character {0}.".format(c))
            failed = True
            break

        tokens.append(token)

    if not failed:
        tokens.append(Token(TokenEnum.EOF, "$"))
        return tokens
    else:
        return False
