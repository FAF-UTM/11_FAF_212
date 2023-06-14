# interpreter.py

from lexer import Lexer
from parser_1 import Parser

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def interpret(self):
        ast = self.parser.parse()
        cbc_params = ['WBC', 'RBC', 'Hemoglobin', 'Platelets', 'Neutrophils', 'Lymphocytes', 'Monocytes', 'Eosinophils', 'Basophils']
        lipid_params = ['Total Cholesterol', 'HDL Cholesterol', 'LDL Cholesterol', 'Triglycerides']
        cmp_params = ['Glucose', 'Albumin', 'Total Protein', 'AST', 'ALT', 'Alkaline Phosphatase']

        reference_range_cbc = {
            'WBC': (4.0, 11.0),                 # White Blood Cell count in 10^9/L
            'RBC': (4.5, 5.5),                  # Red Blood Cell count in 10^12/L
            'Hemoglobin': (12.0, 16.0),         # Hemoglobin concentration in g/dL
            'Platelets': (150, 450),            # Platelet count in 10^9/L
            'Neutrophils': (40, 75),            # Neutrophil percentage
            'Lymphocytes': (20, 40),            # Lymphocyte percentage
            'Monocytes': (2, 10),               # Monocyte percentage
            'Eosinophils': (1, 6),              # Eosinophil percentage
            'Basophils': (0, 2)                 # Basophil percentage
        }

        reference_range_lipid = {
            'Total Cholesterol': (125, 200),     # Total Cholesterol level in mg/dL
            'HDL Cholesterol': (40, 60),         # HDL Cholesterol level in mg/dL
            'LDL Cholesterol': (0, 130),         # LDL Cholesterol level in mg/dL
            'Triglycerides': (0, 150)            # Triglycerides level in mg/dL
        }

        reference_range_cmp = {
            'Glucose': (70, 100),                # Glucose level in mg/dL
            'Albumin': (3.5, 5.0),               # Albumin level in g/dL
            'Total Protein': (6.0, 8.0),         # Total Protein level in g/dL
            'AST': (10, 40),                     # Aspartate Aminotransferase level in U/L
            'ALT': (10, 40),                     # Alanine Aminotransferase level in U/L
            'Alkaline Phosphatase': (30, 120)    # Alkaline Phosphatase level in U/L
        }

        result = {}
        comments = []
        diagnostics = []

        print("Interpreting Medical Results...\n")

        for param in cbc_params:
            value = ast.get(param)
            if value is not None:
                result[param] = value
                lower, upper = reference_range_cbc[param]
                if value < lower:
                    comments.append(f"{param} count is below the normal range.")
                    diagnostics.append(f"Low {param} count may indicate anemia, infection, or bone marrow suppression.")
                elif value > upper:
                    comments.append(f"{param} count is above the normal range.")
                    diagnostics.append(f"Elevated {param} count may suggest inflammation, infection, or certain blood disorders.")
                else:
                    comments.append(f"{param} count is within the normal range.")
                    diagnostics.append(f"{param} count is normal.")

        for param in lipid_params:
            value = ast.get(param)
            if value is not None:
                result[param] = value
                lower, upper = reference_range_lipid[param]
                if value < lower:
                    comments.append(f"{param} level is below the normal range.")
                    diagnostics.append(f"Low {param} level may indicate a risk of cardiovascular disease or metabolic disorders.")
                elif value > upper:
                    comments.append(f"{param} level is above the normal range.")
                    diagnostics.append(f"Elevated {param} level may suggest an increased risk of cardiovascular disease.")
                else:
                    comments.append(f"{param} level is within the normal range.")
                    diagnostics.append(f"{param} level is normal.")

        for param in cmp_params:
            value = ast.get(param)
            if value is not None:
                result[param] = value
                lower, upper = reference_range_cmp[param]
                if value < lower:
                    comments.append(f"{param} level is below the normal range.")
                    diagnostics.append(f"Low {param} level may indicate liver or kidney dysfunction, malnutrition, or metabolic disorders.")
                elif value > upper:
                    comments.append(f"{param} level is above the normal range.")
                    diagnostics.append(f"Elevated {param} level may suggest liver or kidney disease, or other metabolic conditions.")
                else:
                    comments.append(f"{param} level is within the normal range.")
                    diagnostics.append(f"{param} level is normal.")

        if not comments:
            comments.append("Normal Test Results")
            diagnostics.append("No abnormalities detected in the tests.")

        print("Results:")
        for param, value in result.items():
            print(f"  - {param}: {value}")

        print("\nReference Ranges:")
        for param, (lower, upper) in reference_range_cbc.items():
            print(f"  - {param}: {lower} - {upper}")
        for param, (lower, upper) in reference_range_lipid.items():
            print(f"  - {param}: {lower} - {upper}")
        for param, (lower, upper) in reference_range_cmp.items():
            print(f"  - {param}: {lower} - {upper}")

        print("\nComments:")
        for comment in comments:
            print(f"  - {comment}")

        print("\nDiagnostics:")
        for diagnostic in diagnostics:
            print(f"  - {diagnostic}")

        print("\nHealth Care Tips:")
        print("- Maintain a balanced diet and limit intake of saturated and trans fats to maintain healthy cholesterol levels.")
        print("- Engage in regular physical exercise to improve cardiovascular health and manage weight.")
        print("- Monitor blood sugar levels and adopt a healthy lifestyle to prevent diabetes or manage existing diabetes.")
        print("- Follow a healthy diet, exercise regularly, and limit alcohol consumption for optimal liver and kidney function.")
        print("- Consult a healthcare professional for personalized advice and treatment options.")

        print("\nSuggested Curing Method:")
        print("The suggested curing method may vary depending on the specific abnormalities detected in the test results. It is recommended to consult a healthcare professional for a proper diagnosis and treatment plan. The estimated time for recovery will depend on the underlying conditions and the prescribed interventions.")

