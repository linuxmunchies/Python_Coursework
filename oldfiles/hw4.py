import string

def myName():
    return "Redacted ForPrivacy"
def myBlazerID():
    return "Redacted"

print("My name is =", myName(), " and my BlazerId is =",myBlazerID())

# Function: numSteps
""" Takes a positive int n and returns the minimum number of steps
    to reduce it to zero. If it'd odd, subtract 1. If it's even, div by 2.
    Stop when you get to zero.
    Input: 14
    Exoected Output: 6
"""
def numSteps(n):
    stepsTaken = 0
    while n != 0:
        if n % 2 == 0:
            n = n/2
            stepsTaken += 1
        elif n % 2 == 1:
            n = n - 1
            stepsTaken += 1
        else:
            pass
    return stepsTaken

#print(numSteps(14))
#print(numSteps(123))

# Function: genSubStrings(s)
""" Takes string s and returns int. Calculate balanced strings.
    Bal Strings have an equal number of c and s characters. 
    Test with 3 outputs
    sInput = "CSCCSSCSCS"
    sOutput = 4
"""
def genSubStrings(s):
    strList = list(s)
    firstChar = strList[0]
    lenStr = len(strList)

    if firstChar == "C":
        pass
    elif firstChar == "S":
        pass
    else:
        print("There is a non C or S string character detected.")
        quit()

    cList = 0
    sList = 0
    cActive = 0
    sActive = 0
    balStrings = 0
    for x in range(lenStr):
        if x == 0:
            if strList[x] == firstChar and firstChar == "C":
                cList += 1
                cActive = 1
            elif strList[x] == firstChar and firstChar == "S":
                sList += 1
                sActive = 1
        elif x == (lenStr - 1):
            if strList[x] == "C":
                cList += 1
                if cList == sList:
                    balStrings += 1
                    cActive = 1
                    sActive = 0
                    cList = 1
                    sList = 0
            if strList[x] == "S":
                sList += 1
                if cList == sList:
                    balStrings += 1
                    cActive = 1
                    sActive = 0
                    cList = 1
                    sList = 0
        elif strList[x] == "C" and cActive == 1 and sActive == 1:
            if cList == sList:
                balStrings += 1
                cActive = 1
                sActive = 0
                cList = 1
                sList = 0
            else:
                cList += 1
        elif strList[x] == "C" and cActive == 1:
            cList += 1
        elif strList[x] == "C" and cActive == 0:
            cList += 1
            cActive = 1
        elif strList[x] == "S" and cActive == 1 and sActive == 1:
            if cList == sList:
                balStrings += 1
                cActive = 0
                sActive = 1
                cList = 0
                sList = 1
            else:
                sList += 1
        elif strList[x] == "S" and sActive == 1:
            sList += 1
            sActive = 1
        elif strList[x] == "S" and sActive == 0:
            sList += 1
            sActive = 1
        else:
            print("Something went wrong")

    return balStrings

#print(genSubStrings("CSCCSSCSCS"))
#print(genSubStrings("SSSSCCCC"))

# Function: Batman(n2)
""" Takes n2, and prints a list of numbers between 0 and n2.
    Except each number that is a power of 2 gets replaced with the
    string batman.
    sInput = 3
    sOutput = "0batmanbatman3"
"""
def batman(n2):
    oldList = range(int(n2+1))
    newString = ""
    for x in oldList:
        if x == 0:
            newString = newString + '0'
        elif x == 1:
            newString = newString + 'batman'
        elif (x/2).is_integer() == True:
            tempNum = x / 2
            if tempNum == 1:
                newString = newString + ("batman")
                tempNum = 0
            else:
                while tempNum.is_integer() == True and tempNum != 1.0:
                    tempNum = tempNum / 2
                if tempNum == 1:
                    newString = newString + "batman"
                    tempNum = 0
                else:
                    newString = newString + (f"{x}")
                    tempNum = 0
        elif (x/2).is_integer() == False:
            newString = newString + f"{x}"
    return newString
        
#print(batman(3))
#print(batman(7))
#print(batman(10))
#print(batman(1))

# Function: consonantCount(s2)
"""
    Counts how many times a consonant either lower or uppercase occurs in a string.
    Takes string s as input and returns number of consonants in the string.
    limited to for loop
    sInput = "abra cadabra"
    sOutput = 6
"""
def consonantCount(s2):
    # INCLUDES 32 AS WHITESPACE/SPACE VALUE IN ASCII
    vowelVals = [32, 65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121]
    consonAmt = 0
    for x in list(s2):
        if ord(x) not in vowelVals and x.isalpha() == True:
            consonAmt += 1
        else:
            pass
    return consonAmt

#print(consonantCount("abra cadabra"))
#print(consonantCount("how many consonants?"))
#print(consonantCount("This is Hw4, folks"))

# Function: grList(l1)

"""
    Looks at grocery list (l1) and sees if peanut or carrot
    is in the list. if it is, it is replaced in l2 with 
    'orange' instead. then, l2 is printed, then l1 is printed.
"""

def grList(l1):
    l2 = []
    for x in l1:
        if x == "peanut" or x == "carrot":
            l2.append("orange")
        else:
            l2.append(x)
    print(f"My friend needs {l2}")
    print(f"I need {l1}")

#grList(['water', 'chips', 'watermelon', 'peanut', 'napkins'])
#grList(['candy', 'lemonade', 'ginger', 'bread', 'water'])
#grList(['candy', 'peanut', 'carrot', 'bread', 'water'])

# Function: longest(L)
"""
    finds the longest even-length string that ends with -ing.
    If more than 1 string as result, return the first.
    If there are no such strings, return empty string.
    sInput: ["aing","bb","ccing","ddding","zzzzzzzzzz"]
"""

def longest(L):
    tempOne = ''
    tempTwo = ''
    for x in L:
        if len(x) % 2 == 0:
            if x[-3:] == 'ing':
                tempOne = x
                if tempTwo != '':
                    if len(tempOne) > len(tempTwo):
                        tempTwo = tempOne
                else:
                    tempTwo = tempOne
    if tempTwo == "":
        return("")
    else:
        return(tempTwo)

#print(longest(["aing", "bb", "ccing","ddding", "zzzzzzzzzzzz"]))
#print(longest(["swimming", "flying", "coding", "abracadabra UAB CS103", "yoo", "python programming"]))
#print(longest(["robinhood" ,"amazon", "ding", "bing",  ]))
#print(longest(["fishing", "doesn’t", "count", "it", "is", "not even-length"]))
