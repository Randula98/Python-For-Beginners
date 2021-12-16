#import files
from train import Train

#create objects set vales for objects
t1 = Train(1 , 200 , "6:00AM" , "Kandy")
t2 = Train(2 , 150 , "7:30AM" , "Galle")
t3 = Train(3 , 300 , "4:00AM" , "Jaffna")

#set new start time to objects
t1.setStartTime()
t2.setStartTime()
t3.setStartTime()

#display the details of the objects
t1.displayTrainDetails()
t2.displayTrainDetails()
t3.displayTrainDetails()
