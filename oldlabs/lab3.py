# LAB3

def myName():
    return 'Redacted ForPrivacy'

def addTwoNumbers(f1, f2):
    return(f1 + f2)

def multTwoNumbers(f3, f4):
    return(f3 * f4)

def subTwoNumbers(f5, f6):
    return(f5 - f6)

def mailingCost(d):
    cost = 0.00

    if d > 0 and d <= 50:
        cost = d * 5
        return(cost)
    elif d > 50 and d <= 200:
        cost = d * 4.25
        return(cost)
    elif d > 200 and d <= 500:
        cost = d * 3.95
        return(cost)
    elif d >= 501:
        cost = d * 3.70
        return(cost)

def divTwoNumbers(f7, f8):
    return(f7 / f8)

def squareOrNot(length, width):
    if length == width:
        return(True)
    else:
        return(False)

# I wrote a testing zone here, where I plugged in values from the pdf.
# Uncomment them to test quickly. :)

# print(f"\n myName Results: {myName()}\n")
# print ("\n**************************************\n")

# print(f"\n addTwoNumbers Results: {addTwoNumbers(25.2, 7.3)}\n")
# print ("\n**************************************\n")

# print(f"\n multTwoNumbers Results: {multTwoNumbers(5.2, 2.0)}\n")
# print ("\n**************************************\n")

# print(f"\n subTwoNumbers Results: {subTwoNumbers(6.66, 4.11)}\n")
# print ("\n**************************************\n")

# print(f"\n mailingCost Results: {mailingCost(44)}\n")
# print ("\n**************************************\n")

# print(f"\n divTwoNumbers Results: {divTwoNumbers(55.5, 5.0)}\n")
# print ("\n**************************************\n")

# print(f"\n squareOrNot Results: {squareOrNot(20, 5)}\n")
# print ("\n**************************************\n")