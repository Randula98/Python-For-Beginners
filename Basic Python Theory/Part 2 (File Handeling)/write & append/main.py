#create or overwrite
#file = open("contact.txt" , "w")

#append
file = open("contact.txt" , "a")

name = input("Enter Name : ")
contact = input("Enter Contact No : ")

file.write("\n" + name + " - " + contact)

file.close()