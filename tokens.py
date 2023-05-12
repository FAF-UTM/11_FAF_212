
'''
ILLEGAL signifies a token/character we don’t know about 
EOF stands for “end of file”, which tells our parser later on that it can stop.



                                         (book reference page 11)

'''
ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers + literals
IDENT = "IDENT"  # x, y, test, temp, ...
INT = "INT"  # 123456789

# OPERATORS
ASSIGN = "="
PLUS = "+"

# Delimiters
COMMA = ","
DOT = "."
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"
COLON = ':'

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"

keywords: dict = {
    "FUNCTION": FUNCTION,
    "LET": LET
}


def lookup_ident(ident: str):
    if ident in keywords:
        return keywords[ident]
    return IDENT

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"

'''
class Token:
    def __init__(self, Type, Literal):
        self.Type = Type
        self.Literal = Literal

TokenType = str

'''
