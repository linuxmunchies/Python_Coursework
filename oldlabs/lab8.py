#lab08

import string

# Function: listCheck(l)
# Meaning: Prints all even numbers that are lest than 20

def listCheck(l):
    newList = [x for x in l if x < 20 if x % 2 == 0]
    print(newList)

#listCheck([2,3,6,77,33,14,62,18,99,123,1])



# Function: ssnChecker(s)
# Meaning: Takes s and validates if it's SSN formatted.

def ssnChecker(s):
    # Length must be == 11. Dash must be in s[3] and s[6].
    # numbers must be in spots (0:2), (4:5), and (7:10)
    if len(s) == 11:
        if (s[3] == '-' and s[6] == '-'):
            tempList = [x for x in s if x.isdigit()]
            if len(tempList) == 9:
                return(True)
            else:
                return(False)
        else:
            return(False)
    else:
        return(False)

#ssnChecker('88467-3444')


# Function: notPrimes(t)
# Meaning: Takes tuple t and returns all nums that are not prime.

def notPrimes(t):
    notPrimeList = []
    for y in range(len(t)):
        primeList = [x for x in range(1, t[y]+1) if t[y] % x == 0]
        if len(primeList) > 2:
            notPrimeList.append(t[y])
        elif len(primeList) == 2:
            #PRIME DETECTED
            pass
    return(notPrimeList)

#print(notPrimes((3,4,5)))
#print(notPrimes((3,4,5,6,12,14,21)))
#print(notPrimes((12,17,11,22,24)))


# Function: triangleChecker(f1, f2, f3)
# Meaning: Checks if it is a valid triangle and what type.

def triangleChecker(f1, f2, f3):
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

#triangleChecker(5, 4, 6)

# NEED ISPRIME FUNCTION FOR UABCS FUNCTION!!!
def isPrime(n):
    successList = [x for x in range(1, n+1) if n % x == 0]
    if len(successList) > 2:
        return(False)
    elif len(successList) == 2:
        return(True)
    else:
        print("An error has occured. Please check the isPrime function. :)")

# Function: uabCs(n1)
# Meaning: Takes n1 and returns a string according to conditions in the doc

def uabCs(n1):
    if n1 % 7 == 0 and n1 % 3 == 0:
        return("UAB CS 103")
    elif n1 % 7 == 0:
        return("UAB")
    elif n1 % 3 == 0:
        return("CS")
    elif isPrime(n1) and n1 != 3 and n1 != 7:
        return("Go Blazers")
    else:
        return(n1**3)

#print(uabCs(3))
#print(uabCs(70))
#print(uabCs(4))
#print(uabCs(17))