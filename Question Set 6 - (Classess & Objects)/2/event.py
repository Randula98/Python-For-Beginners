#create class
class Event:
    #create class variables
    def __init__(self , eventId , eventType , themeColor , location):
        self.eventId = eventId
        self.eventType = eventType
        self.themeColor = themeColor
        self.location = location

    #define class functions
    def displayEventDetails(self):
        print()
        print("Event Type = " + self.eventType)
        print("Theme Color = " + self.themeColor)
        print("Location = " + self.location)

    def setEventLocation(self):
        self.location = input("Input new location of event " + str(self.eventId) + " : ")