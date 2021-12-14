count = 0
total = 0
marks = 0
average = 0

marks = input("Enter Marks (-10 to end): ")
marks = float(marks)
while (marks != -10):
    if (marks >= 0) and (marks <= 100):
        total += marks
        count += 1
        marks = input("Enter Marks (-10 to end): ")
        marks = int(marks)
    else:
        print("Invalid Value!! Enter a number between 0 - 100")
        marks = input("Enter Marks (-10 to end): ")
        marks = int(marks)

#count = float(count)
average = total / count
#average = float (marks / count)
print()

#average = 1035
print("Total = " + str(total) + " Count = " + str(count))

print("Average is " + str(average))

if (average >= 90):
    grade = "A+"
elif (average >= 80):
    grade = "A"
elif (average >= 75):
    grade = "A-"
elif (average >= 70):
    grade = "B+"
elif (average >= 65):
    grade = "B"
elif (average >= 60):
    grade = "B-"
elif (average >= 55):
    grade = "C+"
elif (average >= 45):
    grade = "C"
elif (average >= 40):
    grade = "C-"
else:
    grade = "D"

print("Grade is : " + grade)
