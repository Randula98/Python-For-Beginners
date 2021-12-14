
#i = 1
#while i <= 10:
#    print(i)
#    i += 1
#print("End")
#print()

answer = 0
tries = 3
out_of_tries = False
print("What is 2 + 3 * 4 + (2 * 8 / 4) : ")

while answer != 18 and not(out_of_tries):
    if (tries > 0):
        answer = input("Enter answer " + str(tries) + " Tries left : ")
        answer = int(answer)
        tries -= 1
    else:
        out_of_tries = True


if (out_of_tries == False):
    print("Correct")
else:
    print("Wrong")

print()
print()


