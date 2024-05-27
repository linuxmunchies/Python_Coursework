#Lab 7

import math

# Function: volCylinder(r,h)
# Meaning: Takes two floats and returns the volume of a generated cylinder.

def volCylinder(r,h):
    return(math.pi * r**2 * h)

#print(volCylinder(2.5,14))
#print(volCylinder(10,10))

# ------------------------------------------------------------------------

# Function: cCount(s)
# Meaning: Prints number of letters, digits, spaces, and symbols.

def cCount(s):
    stringList = list(s)
    letterNum, digitNum, spaceNum, symbolNum = 0, 0, 0, 0
    for x in stringList:
        if ord(x) > 64 and ord(x) < 91 or ord(x) > 96 and ord(x) < 123:
            letterNum += 1
        elif ord(x) > 47 and ord(x) < 58:
            digitNum += 1
        elif ord(x) == 32:
            spaceNum += 1
        else:
            symbolNum += 1
    print(f"Number of letters: {letterNum}")
    print(f"Number of digits: {digitNum}")
    print(f"Number of symbols: {symbolNum}")
    print(f"Number of spaces: {spaceNum}")

#cCount("hello CLASS! 123 *")

# ------------------------------------------------------------------------

# Function: isPrime(n)
# Meaning: Check if n is a prime number.

def isPrime(n):
    successList = [x for x in range(1, n+1) if n % x == 0]
    if len(successList) > 2:
        return(False)
    elif len(successList) == 2:
        return(True)
    else:
        print("An error has occured. Please check the isPrime function. :)")

#print(isPrime(11))
#print(isPrime(17))
#print(isPrime(33))

# ------------------------------------------------------------------------

# Function: finalGrade(classList)
# Meaning: Takes a list with each student sublist and return avg of each elemen

def finalGrade(classList):
    attendVal, examVal, homeworkVal = 0, 0, 0
    for x in range(len(classList)):
        attendVal += classList[x][0]
        examVal += classList[x][1]
        homeworkVal += classList[x][2]
    attendVal = attendVal / len(classList)
    examVal = examVal / len(classList)
    homeworkVal = homeworkVal / len(classList)
    return((attendVal, examVal, homeworkVal))

#print(finalGrade([[20,80,90],[10,60,40],[17,77,56],[21,99,99]]))

# ------------------------------------------------------------------------

# Function: isPrimeList(l)
# Meaning: prints all prime numbers in the list in ascending order.

def isPrimeList(l):
    finalList = []
    for x in range(len(l)):
        primeList = [y for y in range(1, l[x]+1) if l[x] % y == 0]
        if len(primeList) == 2:
            finalList.append(l[x])
    return(finalList)

#print(isPrimeList([11, 4, 8, 90, 87, 111, 17]))