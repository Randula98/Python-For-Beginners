

try:
    answer = 10 / 0
    input = input("Enter a number : ")
    input = int(input)

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Error")