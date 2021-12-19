
#define calculateWeeklySalary function
def calculateWeeklySalary(grade , hrsWorked):
    if grade == "1":
        hRate = 100
    elif grade == "2":
        hRate = 200
    else:
        hRate = 300

    salary = hRate * hrsWorked
    return salary

#define printDetails function
def printDetails(grade , hrsWorked , salary):
    print()
    print("Grade : " + str(grade))
    print("Hours Worked : " + str(hrsWorked))
    print("Salary : " + str(salary))


#get user input for grade
grade = input("Enter Grade : ")
while grade != "1" and grade != "2" and grade != "3":
    print("Invalid input!! Try Again")
    #get user input for grade
    grade = input("Enter Grade : ")

#get user inputs for hours hrsWorked
hrs = input("Enter Hours Worked : ")
hrs = int(hrs)

#pass the given values to calculateWeeklySalary function
salary = calculateWeeklySalary(grade , hrs)

#pass the given values to printDetails function
printDetails(grade , hrs , salary)