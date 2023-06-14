# interpreter.py

from lexer import Lexer
from parser_1 import Parser

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def interpret(self):
        ast = self.parser.parse()
        cbc_params = ['WBC', 'RBC', 'Hemoglobin', 'Platelets']
        reference_range = {
            'WBC': (4.0, 11.0),  # White Blood Cell count in 10^9/L
            'RBC': (4.5, 5.5),   # Red Blood Cell count in 10^12/L
            'Hemoglobin': (12.0, 16.0),  # Hemoglobin concentration in g/dL
            'Platelets': (150, 450)  # Platelet count in 10^9/L
        }

        result = {}
        comments = []
        diagnostics = []

        print("Interpreting Medical Results...\n")

        for param in cbc_params:
            value = ast.get(param)
            if value is not None:
                result[param] = value
                lower, upper = reference_range[param]
                if value < lower:
                    comments.append(f"{param} count is below the normal range.")
                    diagnostics.append(f"Low {param} count may indicate anemia or infection.")
                elif value > upper:
                    comments.append(f"{param} count is above the normal range.")
                    diagnostics.append(f"Elevated {param} count may suggest inflammation or a blood disorder.")
                else:
                    comments.append(f"{param} count is within the normal range.")
                    diagnostics.append(f"{param} count is normal.")

        if not comments:
            comments.append("Normal Complete Blood Count (CBC) results")
            diagnostics.append("No abnormalities detected in the CBC.")

        print("Results:")
        for param, value in result.items():
            print(f"  - {param}: {value}")

        print("\nReference Ranges:")
        for param, (lower, upper) in reference_range.items():
            print(f"  - {param}: {lower} - {upper}")

        print("\nComments:")
        for comment in comments:
            print(f"  - {comment}")

        print("\nDiagnostics:")
        for diagnostic in diagnostics:
            print(f"  - {diagnostic}")

