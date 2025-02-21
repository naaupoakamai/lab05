import re
input_file = '/Users/azamatabilda/Desktop/PP2/lab05/row.txt'
output_file = '/Users/azamatabilda/Desktop/PP2/lab05/output.txt'
pattern = r'[ ,.]'

with open(input_file, 'r', encoding='utf-8') as infile:
    text = infile.read()

result = re.sub(pattern, ':', text)

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(result)

print(f"Данные успешно обработаны и сохранены в '{output_file}'.")
