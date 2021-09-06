import json
import datetime
import stocks


with open("record.json", "r") as file:
    text = file.read()

with open("sales.json","r") as file:
     txt = file.read()

record = json.loads(text)
sales = json.loads(txt)

def display(record):
    print("List Of Products : ")
    for i in record.keys():
        print(i, record[i]["product_name"])

def user_purchase(record):
    dt = str(datetime.datetime.now())
    while True:
        prod_id = input("\nEnter the product_id : ")
        try:
            if prod_id in record.keys():
                user_quan = int(input("Enter the quantity : "))
                print("Product_name : ",record[prod_id]["product_name"])
                print("Price : ",record[prod_id]["price"])
                print("Quantity : ",user_quan)

                if user_quan > record[prod_id]["quantity"]:
                    if user_quan - record[prod_id]["quantity"] <= 5:
                        stocks.addQuantToExistingRecord(record, prod_id)
                    else:
                        print("Sorry we are out of stocks! ")
                        break
                discount = 0
                for i in range(user_quan):
                    discount += ((record[prod_id]["price"])*10/100)
                print("total discount", discount)
                print("Billing Amount with discount : ",total_amount := (user_quan*record[prod_id]["price"]) - discount)
                record[prod_id]["quantity"] = record[prod_id]["quantity"] - user_quan
                sales[len(sales)+1] = {"product_id" : prod_id, "sold quantity" : user_quan, "amount" : total_amount, "DateTime" : dt }
                break

            else:
                print("You have entered invalid product_id...please try again!")
        except ValueError:
                print("please, enter the quantity in number!")
                continue

display(record)
user_purchase(record)

js = json.dumps(sales)
jr = json.dumps(record)

with open("sales.json", "w") as file:
    file.write(js)

with open("record.json", "w") as file:
    file.write(jr)


print("Thanks, for vising us :) ")