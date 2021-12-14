
file = open ("employees.txt" , "r")

if(file.readable()):
    print("Success")
else:
    print("Error")
print()

#read the whole file
print(file.read())

#rewind file pointer
file.seek(0)

print()
#read individual line
print(file.readline())

#rewind file pointer
file.seek(0)
print()

#read the whole file and set as lists
print(file.readlines())

#rewind file pointer
file.seek(0)
print()

#access specific list set
print(file.readlines()[1])

#rewind file pointer
file.seek(0)
print()

#read the lists using a for loop
for employee in file.readlines():
    print(employee)

file.close()