# Lab05

def starLine(n):
    iter = 0
    for x in range(1,n+1):
        iter = 0
        while x > iter:
            print("*", end = '')
            iter += 1
        print("\n")

def cashier(c):
    total = 0
    for x in range(c):
        price = 0
        taxRate = 0
        
        print(f"For item {x+1}")
        
        price = int(input("Enter the price: "))
        taxRate = int(input("Enter the tax rate: "))
        total += price + price * (taxRate * 0.01)

    print(f"Your total price is {total}")

def stringChanger(userString):
    if len(userString) >= 3:
        if userString[-3:] == 'ing':
            return(userString + 'ly')
        else:
            return(userString + 'ing')
    else:
        return(userString)

def smallestSum(listOne, listTwo):
    listThree = []
    for x in range(len(listOne)):
        listThree.append(listOne[x] + listTwo[x])
    return(min(listThree))

def averageList(listOne):
    tempVal = 0
    for x in listOne:
        tempVal += x
    return(tempVal / len(listOne))
