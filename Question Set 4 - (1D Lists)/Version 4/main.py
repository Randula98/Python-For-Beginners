
#define the array
num = [0 for i in range(8)]

#define an integer to count the pattern
pattern = 0

#get user inputs
for i in range(8):
    num[i] = input("Enter a number : ")

print()
#display the user input
print("num array : " , end = " ")
for i in range(8):
    print(num[i] , end = " ")
print()

#check the array for the pattern
for i in range(1 , 8):
    if num[i] == "3" and num[i - 1] == "1":
        pattern = pattern + 1

#display the number of patters appear
print("Number of time the pattern '1 3 ' appear : " + str(pattern))


