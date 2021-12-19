#import file
from event import Event

#create objects
e1 = Event(1 , "party" , "red" , "Nugegoda")
e2 = Event(2 , "wedding" , "purple" , "Maharagama")
e3 = Event(3 , "party" , "pink" , "Malabe")

#set new locations
e1.setEventLocation()
e2.setEventLocation()
e3.setEventLocation()

#display details
e1.displayEventDetails()
e2.displayEventDetails()
e3.displayEventDetails()