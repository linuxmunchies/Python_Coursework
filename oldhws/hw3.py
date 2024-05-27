################################################################################
# HW3
################################################################################
import string

def myName():
    return "Redacted ForPrivacy"

def myBlazerID():
    return "Redaction"

print("My name is =", myName(), " and my BlazerID is =",myBlazerID())



# -------------------------------------------------------------------
# Function: gcDivisor(k,m)
# Meaning: Finds the greatest common divisor of two numbers k and m

def gcDivisor(k, m):
    if k > m or k == m:
        divRange = range(1,k+1)
        gcdList = [x for x in divRange if k % x == 0 if m % x == 0]

    elif k < m:
        divRange = range(1,m+1)
        gcdList = [x for x in divRange if k % x == 0 if m % x == 0]
    
    return(gcdList[-1:])
#print(gcDivisor(54, 81))



# -------------------------------------------------------------------
# Function: lettersOnly(s)
# Meaning: Takes a string and returns a string containing only letters in the string

def lettersOnly(s):
    alphabetList =''.join([x for x in s if x.isalpha()])
    return(alphabetList)
#print(lettersOnly("CS103 is kind of fun."))
#print(lettersOnly("Spaces and punctuation don't count!"))
#print(lettersOnly("This is Hw3"))



# -------------------------------------------------------------------
# Function: listBuilder(l1, length)
# Meaning: Takes a list of strings and a int and returns the strings longer than length

def listBuilder(l1, length):
    newList = []
    for x in range(len(l1)):
        if len(l1[x]) >= length:
            newList.append(l1[x])
    return(newList)
#print(listBuilder(["Hello", "I", "am", "a", "list"],4))
#print(listBuilder(["Homework", "is", "fun"],8))
#print(listBuilder(["CS103", "is", "the", "best"],8))

# -------------------------------------------------------------------
# Function: typeMatters(par)
# Meaning: Takes par of arbitrary type and returns different values dependant on type

def typeMatters(par):
    if isinstance(par, str):
        s = len(par)
        return(par * s)

    elif isinstance(par, int):
        parString = [f"{x} " for x in range(1, par+1)]
        parNewString = ''
        parNewString = parNewString.join(parString)
        return(parNewString)
        
    elif isinstance(par, float):
        return(f"I am a float of value: {par}")

    elif isinstance(par, list):
        par.sort()
        par.reverse()
        return(par)

    else:
        return("I am not a string, int, float, or list.")

#print(typeMatters("hello"))
#print(typeMatters(8))
#print(typeMatters(5.634))
#print(typeMatters([23, 8, 4, 16, 15, 42]))
#print(typeMatters((3,4)))


# -------------------------------------------------------------------
# Function: tCount(s)
# Meaning: Counts number of t's in a string.

def tCount(s):
    iter = 0
    for x in s:
        if x == 'T' or x == 't':
            iter += 1
    return(iter)

#print(tCount('There are 9 ‘t’ letters in this sentence'))
#print(tCount('abra cadabra'))
#print(tCount('Tattooisthas capital T letters'))


# -------------------------------------------------------------------
# Function: listCompare(l1, l2)
# Meaning: Compare two lists and displays all the extra and missing values.

def listCompare(l1, l2):
    missingList = [x for x in l1 if x not in l2]
    extraList = [x for x in l2 if x not in l1]
    print('The missing values: ' + ', '.join(missingList))
    print('The extra values: ' + ', '.join(extraList))

listCompare(["a", "b", "c", "d", "e"], ["b", "d", "e", "f", "g"])
