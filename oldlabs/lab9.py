# Lab09

# Function: fChecker
# Meaning: Reads inputFile.txt and reads line by line. 

import statistics

def fChecker():
    inputFile = open("inputFile.txt", "r") # Opens the file
    listVals = inputFile.read().splitlines()
    print(f"Hello, {listVals[0]} {listVals[1]}. You will be {int(listVals[2]) + 5} years old in 5 years.")

#fChecker()

# Function: fileAnalyze()
# Meaning: reads inputFile.txt and creates outputFile.txt

def fileAnalyze():
    inputFileTwo = open("inputFile2.txt", "r")
    listVals = inputFileTwo.read().splitlines()
    listNumVals = [int(x) for x in listVals]
    lengthList = len(listNumVals)
    maxNum = max(listNumVals)
    minNum = min(listNumVals)
    avgNum = (sum(listNumVals) / len(listNumVals))
    outputFile = open("outputFile.txt", "w")

    for currentNum in listNumVals:
        #Write the numbers from the list to the txt file.
        outputFile.write(str(currentNum) + "\n")
    outputFile.write("**********\n")
    outputFile.write(f"There are {lengthList} numbers in this file.\n")
    outputFile.write(f"The minimum number is {minNum}.\n")
    outputFile.write(f"The maximum number is {maxNum}.\n")
    outputFile.write(f"The average is {avgNum}.\n")

#fileAnalyze()

# Function: argmin()
# Meaning: Self implementation of argmin.

def argMin(userList):
    for x in range(len(userList)):
        if x != 0:
            if userList[x] < smallestNum:
                smallestNum = userList[x]
                smallestNumIndex = x
        else:
            smallestNum = userList[0]
            smallestNumIndex = x
    print(smallestNum, smallestNumIndex)

#argMin([141, 4, 414, 23, 64, 5, 65, 3, 16, 1, -1, 32, 11])

# Function: triangleChecker()
# Meaning: Reads the three sides of a triangle from a file and determines if its valid triangle

def triangleChecker():
    inputF = open("triangle.txt", "r")
    listVals = inputF.read().splitlines()
    f1 = listVals[0]
    f2 = listVals[1]
    f3 = listVals[2]
    if ((f1 + f2) > f3 or (f2 + f3) > f1 or (f3 + f1) > f2):
        if f1 == f2 == f3:
            print("The triangle is valid. It is am equilateral triangle.")
        elif (f1 != f2 and f2 != f3 and f3 != f1):
            print("The triangle is valid. It is a scalene triangle.")
        elif (f1 == f2 or f2 == f3 or f3 == f1):
            print("The triangle is valid. It is an isosceles triangle.")
        else:
            print("Something's gone wrong!")
    else:
        print("The triangle provided is not valid.")

#triangleChecker()