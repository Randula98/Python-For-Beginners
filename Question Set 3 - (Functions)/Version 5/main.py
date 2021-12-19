
#define findRadianValue function
def findRadianValue(angleInDegree):
    angleInRadian = float(angleInDegree / 180 * 22 / 7)
    return angleInRadian

#define printRadianValues function
def printRadianValues():
    print("Angle(degrees)\tAngle(Radians)")
    for degree in range(100 , 210 , 20):
        radian = findRadianValue(degree)
        radian = float(radian)
        radian = round(radian , 2)
        print(str(degree) + "\t\t\t\t" + str(radian))


#call the printRadianValues function
printRadianValues()