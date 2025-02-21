import re

def snake_to_camel(snake_str):
    return re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), snake_str)

text = "my_variable_name"
result = snake_to_camel(text)

print(f"Snake case: {text}")
print(f"Camel case: {result}")
