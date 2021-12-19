#create class
class Student:
    #define class variables
    def __init__(self , studentID , studentName, marksOOC , marksSPM , marksISDM):
        self.studentID = studentID
        self.studentName = studentName
        self.marksOOC = marksOOC
        self.marksSPM = marksSPM
        self.marksISDM = marksISDM

    #define class functions
    def setMarksOOC(self , mOOC):
        self.marksOOC = mOOC

    def getMarksOOC(self):
        return (self.marksOOC)

    def setMarksSPM(self , mSPM):
        self.marksSPM = mSPM

    def getMarksSPM(self):
        return (self.marksSPM)

    def setMarksISDM(self , mISDM):
        self.marksISDM = mISDM

    def getMarksISDM(self):
        return (self.marksISDM)