#LAB 06

# Function: mOfThree
# Meaning: Takes all integers between 1 and n that are multiples are three.

def mOfThree(n):
    iterCount = 0
    while iterCount != n:
        for x in range(1, n+1):
            if x % 3 == 0:
                print(x)
            else:
                pass
        iterCount = n

#(mOfThree(14))

# Function: tupleCheck
# Meaning: Takes tuple t and checks for which nunmbers in the tuple are even or odd.
def tupleCheck(t):
    evenNums = [x for x in t if x % 2 == 0]
    oddNums = [x for x in t if x % 2 == 1]
    print(f"Number of even numbers : {len(evenNums)}")
    print(f"Number of odd numbers : {len(oddNums)}")

#tupleCheck((3,4,5,6,7,8,12,12,12,12))

# Function: caseCheck
# Meaning: Checks if the currently selected character in s is uppercase or lowercase.
def caseCheck(s):
    listLower = [x for x in s if ord(x) >= 97 if ord(x) <= 122]
    listUpper = [x for x in s if ord(x) >= 65 if ord(x) <= 90]
    print(f"Number of Upper case characters : {len(listUpper)}")
    print(f"Number of Lower case characters : {len(listLower)}")

#caseCheck('The quick Brown Fox')

# Function: iCube
# Meaning: Takes int n and prints i^3 for all positive integers 1 < n

def iCube(n):
    for x in range(1, n):
        print(x**3)

#iCube(5)

# Function: mTable
# Meaning: Takes an integer n2 and prints the multiplication table of it.

def mTable(n2):
    for x in range(1, 11):
        print(f"{n2} x {x} = {x * n2}")

#mTable(6)