
#define calcIncrement function
def calcIncrement(salary , noOfYearsWorked):
    if(noOfYearsWorked > 2):
        increment = (salary * 10 / 100)
    else:
        increment = 0

    return increment

#define calcTotalSalary function
def calcTotalSalary(salary , increment):
    total = salary + increment
    return total

#get user inputs for salary
salary = input("Enter Salary : ")
salary = float(salary)

#get user inputs for number of years worked
years = input("Enter no of years worked : ")
years = int(years)

#calculate the increment by passing the given values to the function
increment = calcIncrement(salary , years)

#calculate the total salary by passing the given values to the function
totalSalary = calcTotalSalary(salary , increment)

#display the increment and the total salary
print("Increment : " + str(increment))
print("Total Salary : " + str(totalSalary))
