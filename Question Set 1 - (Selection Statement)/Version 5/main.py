
#get the user input for Position
position = input("Position : ")
while position != "M" and position != "m" and position != "S" and position != "s":
    print("Invalid Input")
    position = input("Position : ")

#get the user input for sales amount
sales = input("Sales amount : ")
sales = float(sales)

#get the basic salary by the user input
if position == "M" or position == "m":
    basic = 50000
else:
    basic = 75000

#check the sales amount for commission
if sales >= 30000:
    commission = sales * 10 / 100
else:
    commission = 0

#calculate the salary
salary = basic + commission

#display the commission and the salary
print("Commission : " + str(commission))
print("Salary : " + str(salary))
