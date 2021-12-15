
#take user inputs for Item code
itemCode = input("Item Code : ")
while itemCode != "1" and itemCode != "2" and itemCode != "3":
    print("Invalid Input!! Try again")
    itemCode = input("Item Code : ")

#take user inputs for quantity
quantity = input("Quantity : ")
quantity = float(quantity)

#take user inputs for customer type
cType = input("Customer Type (L / N) : ")
while cType != "L" and cType != "l" and cType != "N" and cType != "n":
    print("Invalid Input!! Try again")
    cType = input("Customer Type (L / N) : ")

#calculate basic price
if itemCode == "1":
    total = 530 * quantity
elif itemCode == "2":
    total = 300 * quantity
elif itemCode == "3":
    total = 950 * quantity

#calculate discount
if cType == "L" or cType == "l":
    discount = float(total * 25 / 100)
else:
    discount = float(total * 5 / 100)

#calculate total price
total = total - discount

#display the discount and total
print("Discount : " + str(discount))
print("Total bill after the discount : " + str(total))