import json

#open the record.json and read all the data from file
with open("record.json", "r") as file:
    txt = file.read()

#parse a valid JSON string and convert it into a Python Dictionary.
record = json.loads(txt)

def addQuantToExistingRecord(record,prod_id):
    record[prod_id]["quantity"] += 5


js = json.dumps(record)

with open("record.json", "w") as file:
    file.write(js)
