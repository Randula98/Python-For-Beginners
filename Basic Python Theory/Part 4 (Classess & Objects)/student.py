#create class
class Student:
    #define class variables
    def __init__(self , name , major , gpa , year , semester): #use 2 underscore (_) marks
        self.name = name
        self.major = major
        self.gpa = gpa
        self.year = year
        self.semester = semester

    #define class functions
    def on_deans_list(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False