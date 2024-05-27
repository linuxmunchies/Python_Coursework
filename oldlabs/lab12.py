# Lab 12

import cv2

"""
hailstone: repeats hailstone algorithm until n2 is equal to 1
n2: type(int), input integer
"""
def hailstone(n2):
    while n2 != 1:
        if n2 % 2 == 0:
            n2 = n2 // 2
        else:
            n2 *= 3
            n2 += 1
            print(n2, end=' ')
#hailstone(3)


"""
grayscale2binary: converts a given image into black and white
n: type(int), threshold value
"""
def grayscale2binary(n):

    initial = cv2.imread('grayscale_image.png', cv2.IMREAD_GRAYSCALE)
    binary = cv2.threshold(initial, n, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('binary', binary)
    cv2.waitKey(0)
    cv2.destrayAllWindows()
#grayscale2binary(10)


"""
    interestingSum: takes in a list l
        returns another list that contains n + ... + nFinal in a list L
        sample input: [1,2,3,4]
        sample output: [1,3,6,10]
"""
def interestingSum(l):
    runningList = []
    for x in l:
        if len(runningList) == 0:
            runningList.append(x)
        else:
            runningList.append(runningList[-1] + x)
    return(runningList)
#print(interestingSum([1,2,3,4]))
#print(interestingSum([1,1,1,1,1]))


"""
animalLegs(d2): Takes a dictionary of animals (d2) and prints total num
    of legs of all the animals in d2. 
    sample input: d1 = {"chickens":10, "rabbits":5}
    sample output: 40
"""
def animalLegs(d2):
    chiLegs = 2
    cowLegs = 4
    rabLegs = 4
    dogLegs = 4
    numChi = 0
    numCow = 0
    numRab = 0
    numDog = 0

    if 'chickens' in d1:
        numChi = d1['chickens']
    
    if 'cows' in d1:
        numCow = d1['cows']
    
    if 'rabbits' in d1:
        numRab = d1['rabbits']
    
    if 'dogs' in d1:
        numDog = d1['dogs']
    totalLegs = ((numChi * chiLegs) + (numCow * cowLegs) + (numRab * rabLegs) + (numDog * dogLegs))
    return totalLegs
#d1 = {"chickens":10, "rabbits":5}
#print(animalLegs(d1))