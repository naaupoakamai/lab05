import re
file_path = '/Users/azamatabilda/Desktop/PP2/lab05/row.txt'
pattern=r'\b[A-Z][a-z]+\b'
count=0
matches=[]

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

for index, line in enumerate(lines, start=1):
    if re.search(pattern, line):
        count += 1
        matches.append(f"Строка {index}: {line.strip()}")

print(f"Количество строк, соответствующих шаблону: {count}")
if matches:
    print("Совпадения найдены в следующих строках:")
    for match in matches:
        print(match)
else:
    print("Совпадений не найдено.")