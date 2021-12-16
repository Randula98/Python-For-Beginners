#sub class
from pet import Pet

#inheritance
class Dog(Pet):

    #inherit variables from the super class
    def __init__(self , name , age , breed):
        Pet.__init__(self , name , age)
        self.breed = breed

    def bark(self):
        print(self.name + " is Barking")

    #function overriding
    def play(self):
        print(self.name + " the dog is playing with you")