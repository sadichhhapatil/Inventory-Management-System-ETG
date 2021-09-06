import json

#open the record.json and read all the data from file
with open("record.json", "r") as file:
    txt = file.read()

#parse a valid JSON string and convert it into a Python Dictionary.
record = json.loads(txt)


#add new products to inventory----
def addNewProductsToInventory(record):
    while True:
        prod_id = str(input("Enter the product id : "))
        if prod_id in record.keys():
            try:
                prod_quant = int(input("Enter the quantity of product : "))
                record[prod_id]["quantity"] +=  prod_quant
            except ValueError:
                print("please, enter the quantity in number!")
                continue
        else:
            prod_na = str(input("Enter the product name : "))
            prod_pr = int(input("Enter the price of product : "))
            prod_cl = str(input("Enter the colour of the product : "))
            prod_wr = str(input("If product have warrenty then enter otherwiswe enter NA : "))
            prod_mt = str(input("Enter the material used for product : "))
            prod_quant = int(input("Enter the quantity of product : "))
            record[prod_id] = {"product_name" : prod_na, "price" : prod_pr, "colour" : prod_cl, "warrenty" : prod_wr, "material" : prod_mt, "quantity": prod_quant}
        ans = str(input("Do you want to add more products then type 'yes' else type 'no' : "))
        if ans == 'yes':
            return True
        elif ans =='no':
            return False
        else:
            return False

addNewProductsToInventory(record)

js = json.dumps(record)

with open("record.json","w") as file:
    file.write(js)

