import re

text = "SplitThisStringByUpperCaseLetters"
pattern = r'(?=[A-Z])'
result = re.split(pattern, text)
print("Исходная строка:", text)
print("Результат разделения:", result)
