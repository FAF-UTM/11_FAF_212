# interpreter.py

from lexer import Lexer
from parser_1 import Parser

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def interpret(self):
        ast = self.parser.parse()
        cbc_params = ['WBC', 'RBC', 'Hemoglobin']
        reference_range = {
            'WBC': (4.0, 11.0),
            'RBC': (4.5, 5.5),
            'Hemoglobin': (12.0, 16.0)
        }

        result = {}
        comments = []
        for param in cbc_params:
            value = ast.get(param)
            if value is not None:
                result[param] = value
                lower, upper = reference_range[param]
                if value < lower:
                    comments.append(f"{param} value is below normal range.")
                elif value > upper:
                    comments.append(f"{param} value is above normal range.")
                else:
                    comments.append(f"{param} value is within normal range.")

        if not comments:
            comments.append("Normal CBC results")
        
        print("result:")
        for param, value in result.items():
            print(f"  - {param}: {value}")
        
        print("reference_range:")
        for param, (lower, upper) in reference_range.items():
            print(f"  - {param}: {lower} - {upper}")
        
        print("comments:")
        for comment in comments:
            print(f"  - {comment}")

    def __init__(self, parser):
        self.parser = parser

    def interpret(self):
        ast = self.parser.parse()
        cbc_params = ['WBC', 'RBC', 'Hemoglobin']
        reference_range = {
            'WBC': (4.0, 11.0),
            'RBC': (4.5, 5.5),
            'Hemoglobin': (12.0, 16.0)
        }

        result = {}
        for param in cbc_params:
            value = ast.get(param)
            if value is not None:
                result[param] = value

        comments = "Normal CBC results"
        
        print("result:")
        for param, value in result.items():
            print(f"  - {param}: {value}")
        
        print("reference_range:")
        for param, (lower, upper) in reference_range.items():
            print(f"  - {param}: {lower} - {upper}")
        
        print(f"comments: {comments}")