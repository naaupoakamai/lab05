import re
def camel_to_snake(camel_str):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
    return snake_str

camel_case_string = "CamelCaseExampleString"
snake_case_string = camel_to_snake(camel_case_string)

print(f"Original camel case: {camel_case_string}")
print(f"Converted to snake case: {snake_case_string}")
