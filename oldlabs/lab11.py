# Lab 11

import numpy as np
import statistics

"""
fileExtension: Returns the extension of the file input
s: type(str), filename
"""
def fileExtension(s):
    index = 0
    for i in range(len(s)):
        if s[i] == ".":
            index = i + 1
            break
    return s[index:]

print("The result of fileExtension is: ")
print(fileExtension("Lab13_103sp19.pdf"))

"""
basicStats: returns a list with mean, standard deviation
npArray: numpy array
"""
def basicStats(npArray):
    stats_list = []
    stats_list.append(np.mean(npArray))
    stats_list.append(np.std(npArray))
    stats_list.append(np.var(npArray))
    return stats_list

print("The output of basicStats is: ")
print(basicStats([0,1,2,3,4,5]))

"""
keysToRemove: returns a new dictionary
d: dictionary
l: list, keys to remove.
"""

def keysToRemove(d,l):
    for i in l:
        if i in d:
            del d[i]
    return d

l = {"Salary", "Company"}
d = {"FirstName": "Mark", "LastName": "Zuckerberg", "City": "Palo Alto"}
print("The output of keysToRemove is: ")
print(keysToRemove(d,l))

"""
takes in list l and returns tuple containing:
    number of elements in list
    minimum value
    minimum value's index
    mean
    max val
    max val's index
"""
print("The output of listDetails is: ")
def listDetails(l):
    detailList = []
    detailList.append(len(l))
    detailList.append(np.amin(l))
    detailList.append(l.index(np.amin(l)))
    detailList.append(round(statistics.mean(l), 2))
    detailList.append(np.max(l))
    detailList.append(l.index(np.max(l)))
    return tuple(detailList)

print(listDetails([-8,-23,18,103,0,1,-4,631,3,-41,5]))

"""
minSum: Takes a list and finds the two smallest numbers
    then adds them together
"""
def minSum(L2):
    tempNumSmall = 0
    tempNumSmallest = 0
    for x in L2:
        if L2[0] == x:
            #tempNumSmall = 0
            tempNumSmallest = x
        elif L2[1] == x:
            if x < tempNumSmallest:
                tempNumSmall = tempNumSmallest
                tempNumSmallest = x
            elif x > tempNumSmallest:
                tempNumSmall = x
        else:
            if x < tempNumSmall:
                if x < tempNumSmallest:
                    tempNumSmall = tempNumSmallest
                    tempNumSmallest = x
                elif x > tempNumSmallest:
                    tempNumSmall = x
    return(f"[{L2.index(tempNumSmallest)},{L2.index(tempNumSmall)}]\nSUM:{tempNumSmallest + tempNumSmall}")

print("The output of minSum is:")
print(minSum([2,78,9,21,4,99]))