import json

sales = { 1 : {"product_id": "1006", "sold quantity": 1, "amount": 5699, "DateTime": "2021-09-06 10:20:03.087110"}}

js = json.dumps(sales)

with open("sales.json","w") as file:
    file.write(js)