import re

text = "InsertSpacesBetweenCapitalWords"
pattern = r'(?<!^)([A-Z])'
result = re.sub(pattern,r' ', text)
print("Исходная строка:", text)
print("Результат разделения:", result)