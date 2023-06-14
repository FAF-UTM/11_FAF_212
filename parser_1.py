# parser.py

from lexer import Lexer, IDENT, STRING, NUMBER, COLON, NEWLINE, EOF

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
           self.error(f"Expected {token_type}, found {self.current_token.type}")

    def parse(self):
        results = {}

        while self.current_token.type != EOF:
            if self.current_token.type == IDENT:
                ident = self.current_token.literal
                self.eat(IDENT)

                self.eat(COLON)

                if self.current_token.type == NUMBER:
                    results[ident] = self.current_token.literal
                    self.eat(NUMBER)
                elif self.current_token.type == STRING:
                    results[ident] = self.current_token.literal
                    self.eat(STRING)
                else:
                    self.error(f"Invalid value type: {self.current_token.type}")

                if self.current_token.type == NEWLINE:  # Only eat a newline if one exists
                    self.eat(NEWLINE)
                else:
                    self.error("Expected newline after value")

            else:
                self.error(f"Invalid token: {self.current_token.type}")

        return results
