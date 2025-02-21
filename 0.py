import re
import json

input_file = '/Users/azamatabilda/Desktop/PP2/lab05/row.txt'
output_file = '/Users/azamatabilda/Desktop/PP2/lab05/row.json'

with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

receipt_data = {
    "store": "",
    "bin": "",
    "cashier": "",
    "items": [],
    "total": 0,
    "payment_method": "",
    "date_time": "",
    "address": ""
}

item_pattern = re.compile(r'(\d+)\.\s+(.+)\n([\d.,]+)\s+x\s+([\d\s.,]+)\n([\d\s.,]+)')
store_pattern = re.compile(r'Филиал\s+ТОО\s+(.+)')
bin_pattern = re.compile(r'БИН\s+(\d+)')
cashier_pattern = re.compile(r'Кассир\s+(.+)')
total_pattern = re.compile(r'ИТОГО:\s+([\d\s]+,\d+)')
payment_pattern = re.compile(r'Банковская карта:\s+([\d\s]+,\d+)')
date_pattern = re.compile(r'Время:\s+(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})')
address_pattern = re.compile(r'г\. Нур-султан,(.+)')

for line in lines:
    store_match = store_pattern.search(line)
    if store_match:
        receipt_data["store"] = store_match.group(1).strip()

    bin_match = bin_pattern.search(line)
    if bin_match:
        receipt_data["bin"] = bin_match.group(1)

    cashier_match = cashier_pattern.search(line)
    if cashier_match:
        receipt_data["cashier"] = cashier_match.group(1).strip()

    item_match = item_pattern.search(line)
    if item_match:
        item = {
            "number": int(item_match.group(1)),
            "name": item_match.group(2).strip(),
            "quantity": float(item_match.group(3).replace(',', '.')),
            "price_per_unit": float(item_match.group(4).replace(' ', '').replace(',', '.')),
            "total_price": float(item_match.group(5).replace(' ', '').replace(',', '.'))
        }
        receipt_data["items"].append(item)

    total_match = total_pattern.search(line)
    if total_match:
        receipt_data["total"] = float(total_match.group(1).replace(' ', '').replace(',', '.'))

    payment_match = payment_pattern.search(line)
    if payment_match:
        receipt_data["payment_method"] = "Банковская карта"
        receipt_data["payment_amount"] = float(payment_match.group(1).replace(' ', '').replace(',', '.'))

    date_match = date_pattern.search(line)
    if date_match:
        receipt_data["date_time"] = date_match.group(1)

    address_match = address_pattern.search(line)
    if address_match:
        receipt_data["address"] = address_match.group(1).strip()

with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(receipt_data, json_file, indent=4, ensure_ascii=False)

print(f"Данные успешно сохранены в '{output_file}'.")
