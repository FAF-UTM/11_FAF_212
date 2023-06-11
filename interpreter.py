# interpreter.py

from lexer import Lexer
from parser_1 import Parser

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def interpret(self):
        ast = self.parser.parse()
        for key, value in ast.items():
            print(f"{key}: {value}")
