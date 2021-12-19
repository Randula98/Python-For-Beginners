#import file
from student import Student

#create objects and set student details
s1 = Student(1234 , "Kamal" , 0 , 0 , 0)
s2 = Student(4567 , "Saman" , 0 , 0 , 0)
s3 = Student(7891 , "Nimal" , 0 , 0 , 0)
s4 = Student(1212 , "Sunil" , 0 , 0 , 0)

#set marks for s1
s1.setMarksOOC(85)
s1.setMarksSPM(80)
s1.setMarksISDM(75)

#set marks for s2
s2.setMarksOOC(65)
s2.setMarksSPM(50)
s2.setMarksISDM(45)

#set marks for s3
s3.setMarksOOC(98)
s3.setMarksSPM(75)
s3.setMarksISDM(80)

#set marks for s4
s4.setMarksOOC(35)
s4.setMarksSPM(60)
s4.setMarksISDM(40)


#calculate average for each module
avgOOC = (s1.getMarksOOC() + s2.getMarksOOC() + s3.getMarksOOC() + s4.getMarksOOC()) / 4
avgSPM = (s1.getMarksSPM() + s2.getMarksSPM() + s3.getMarksSPM() + s4.getMarksSPM()) / 4
avgISDM = (s1.getMarksISDM() + s2.getMarksISDM() + s3.getMarksISDM() + s4.getMarksISDM()) / 4

#display average marks
print("Average OOC Marks : " + str(avgOOC))
print("Average SPM Marks : " + str(avgSPM))
print("Average ISDM Marks : " + str(avgISDM))