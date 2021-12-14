print("Start")
list = ['One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten']
number = [1 , 4 , 8 , 6 , 9 , 7 , 3 , 10 , 2 , 5]
same = [1 , 5 , 3 , 1 , 5 , 6 , 4 , 1 , 8]

print(list)
print(number)
print()

print("Extend")
#combine lists(extend)
list.extend(number)
print(list)
list = ['One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten']
print()

print("Append")
#insert new data at the end (append)
list.append("Add")
print(list)
print()

print("Insert")
#insert new data to the middle (insert)
list.insert(1 , "Break")
print(list)
print()

print("Remove")
#remove data (remove)
list.remove("Add")
list.remove("Break")
print(list)
print()

print("Clear")
#remove all data (clear)
list.clear()
print(list)
list = ['One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten']
#remove last one
list.pop()
print(list)
print()
list = ['One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten']

#index check
print(list.index('One'))
print(number.index(10))
print()

#count elements
print(same)
print(same.count(1))
print()

#sort element
same.sort()
print(same)
print()

#reverse order
same.reverse()
print(same)
print()

#copy a list
number_set = same.copy()
print(number_set)
print()

number_set.reverse()
print(number_set)