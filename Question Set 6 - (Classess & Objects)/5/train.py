#define class
class Train:
    #define class variables
    def __init__(self , trainID , capacity , startTime , destination):
        self.trainID = trainID
        self.capacity = capacity
        self.startTime = startTime
        self.destination = destination

    #define class functions
    def displayTrainDetails(self):
        print()
        print("Train ID = " + str(self.trainID))
        print("Capacity = " + str(self.capacity))
        print("Start Time = " + self.startTime)
        print("Destination = " + self.destination)

    def setStartTime(self):
        self.startTime = input("Input new start time of train " + str(self.trainID) + " : ")