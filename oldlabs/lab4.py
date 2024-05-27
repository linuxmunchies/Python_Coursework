# Lab04

import random
import math

def evenNumbers(x):
    tempList = list(range(x+1))
    newList = [x for x in tempList if x % 2 == 0]
    print(newList)

def factorial(f):
    tempList = range(1,f)
    finalNum = 1
    for x in tempList:
        finalNum += finalNum * x
    return(finalNum)

def randNumbers(r):
    tempList = [random.randint(0,10) for x in range(r)]
    tempNum = 0
    for x in tempList:
        tempNum += x
        print(f"\nRandom Number: {x}\n")
    finalNum = tempNum / r
    return(finalNum)

def letterCount(s1, s2):
    count = 0
    for s in s2:
        print(s)
        for i in s1:
            print(i)
            if i == s:
                count += 1
        print(s, count)
        count = 0

def fibonacci(n):
    aList = range(n)
    bList = []
    #Turn it into a Fibonacci sequence.
    for x in aList:
        if x == 0:
            bList.append(0)
        elif x == 1:
            bList.append(1)
        else:
            bList.append(bList[x-1] + bList[x-2])
    print(bList)

def listSum(l):
    tempList = [x for x in l[1:7]]
    return(sum(tempList))

