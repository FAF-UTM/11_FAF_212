'''

The lexer is responsible for tokenizing the input. It will recognize identifiers (like "patient", "dob", "test"), strings, 
numbers, and special symbols (like ":", "{", "}", and newlines).


IDENT: Identifiers, like patient, dob, test, date, cbc, etc.
STRING: String literals, like John Doe, Complete Blood Count, etc.
NUMBER: Numeric literals, like 15.5, 45, 6000, etc.
COLON: The : symbol.
NEWLINE: Line breaks.

'''

# lexer.py

import re


IDENT = 'IDENT'
STRING = 'STRING'
NUMBER = 'NUMBER'
INTEGER = 'INTEGER'  # Add INTEGER token type
COLON = 'COLON'
NEWLINE = 'NEWLINE'
EOF = 'EOF'

class Token:
    def __init__(self, type, literal):
        self.type = type
        self.literal = literal

class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.current_char = self.input[self.position]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.position += 1
        if self.position > len(self.input) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.input[self.position]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def ident(self):
        result = ''
        while self.current_char is not None and self.current_char.isalpha():
            result += self.current_char
            self.advance()
        return result

    def string(self):
        result = ''
        self.advance()  # Skip the initial quote
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # Skip the closing quote
        return result

    def number(self):
        result = ''
        if self.current_char == '-':
            result += self.current_char
            self.advance()
        if self.current_char is None or not self.current_char.isdigit():
            self.error()

        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()
            while (
                self.current_char is not None and
                self.current_char.isdigit()
            ):
                result += self.current_char
                self.advance()
            token_type = NUMBER
        else:
            token_type = INTEGER
        return float(result) if token_type == NUMBER else int(result)

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return Token(IDENT, self.ident())

            if self.current_char == '"':
                return Token(STRING, self.string())

            if self.current_char.isdigit() or self.current_char == '-':
                return Token(NUMBER, self.number())

            if self.current_char == ':':
                self.advance()
                return Token(COLON, ':')

            if self.current_char == '\n':
                self.advance()
                return Token(NEWLINE, '\n')

            self.error(f"Invalid character: {self.current_char}")

        return Token(EOF, None)
