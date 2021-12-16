from pet import Pet
from dog import Dog

#super class behavior
pet1 = Pet("Tim" , 5)
pet1.play()
print()

#subclass behavior
dog1 = Dog("Bob" , 2 , "German Shepheard")
dog1.play()
dog1.bark()

