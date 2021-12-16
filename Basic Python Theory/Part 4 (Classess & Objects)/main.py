#import file
from student import Student

#create object
student1 = Student("John" , "Software Engineer" , 3.8 , 3 , 1)
student2 = Student("Shyla" , "Graphic Designer" , 3.2 , 2 , 2)

print(student1.name)
print(student1.on_deans_list())

print()

print(student2.name)
print(student2.on_deans_list())

