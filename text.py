# Import the metamodel_from_file function from the textx library
from textx import metamodel_from_file

# Define the metamodel using the grammar file
mm = metamodel_from_file('grammar.tx')

# Load the model from the input file
model = mm.model_from_file('test.med')

# Access the contents of the model

# Get the Description object from the model
description = model.Description

# Get the glucose, units, stage, and reference range attributes from the Description object
glucose = description.glucose
units = description.units
stage = description.stage
reference_range = description.range

# Get the Setting object from the model
setting = model.Setting

# Get the patient, age, gender, weight, and height attributes from the Setting object
patient = setting.patient
age = setting.age
gender = setting.gender
weight = setting.weight
height = setting.height

# Get the Response object from the model
response = model.Response

# Get the query_type and patient_data attributes from the Response object
query_type = response.query_type
patient_data = response.patient_data

# Print some of the contents of the model
print(f"Patient: {patient}, Age: {age}")
print(f"Test: glucose={glucose}, units={units}, stage={stage}, reference range={reference_range}")
print(f"Query: query_type={query_type}, patient_data={patient_data}")
