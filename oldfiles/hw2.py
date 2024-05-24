################################################################################
# HW2
################################################################################
import math

def myName():
 return "Redacted ForPrivacy"

def myBlazerID():
 return "Redaction"

def isOdd(n1):
    try:
        n1 / 2
    except:
        return(False)
    else:
        if n1 % 2 != 0:
            return(True)
        elif n1 % 2 == 0:
            return(False)

def tupleCounter(t):
    tempCounter = 0
    for x in t:
        if (x % 2 != 0):
            tempCounter += 1
        else:
            pass
    return(tempCounter)

def cubeOfOdd(n2):
    for x in range(1,n2):
        if x % 2 != 0:
            print(x**3)
        else:
            pass

def paintTheRoom(length, width, height):
    totArea = (length * height * 2) + (width * height * 2) + (length * width)
    return(math.ceil(totArea / 400))

def stringMerge(s1):
    if len(s1) < 2:
        return('')
    else:
        return(s1[:2] + s1[-2:])

def interestingMerge(l2, l3):
    newList = [(x, y) for x in l2 for y in l3 if y % x == 0]
    return(newList)

print(cubeOfOdd(8))