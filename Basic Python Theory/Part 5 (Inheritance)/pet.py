#super class
class Pet:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def play(self):
        print(self.name + " is playing with you")